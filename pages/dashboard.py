import streamlit as st
import pandas as pd
import plotly.express as px
from db import fetch_query
import logging

logger = logging.getLogger(__name__)

def render(user: dict):
    st.title("📊 Dashboard")
    st.markdown("Overview of Key Performance Indicators and Sales Trends.")

    role = user.get("role", "")
    branch_id = user.get("branch_id")

    # Branch filter based on role
    where_clause = ""
    params = []
    if role != "Super Admin":
        where_clause = "WHERE branch_id = %s"
        params.append(branch_id)

    # Fetch KPIs
    kpi_query = f"""
        SELECT 
            COUNT(sale_id) as total_sales_count,
            COALESCE(SUM(gross_sales), 0) as total_gross,
            COALESCE(SUM(received_amount), 0) as total_received,
            COALESCE(SUM(pending_amount), 0) as total_pending
        FROM customer_sales
        {where_clause}
    """
    try:
        df_kpi = fetch_query(kpi_query, tuple(params))
        if not df_kpi.empty:
            kpi_data = df_kpi.iloc[0]
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Sales (Count)", f"{int(kpi_data['total_sales_count'])}")
            col2.metric("Gross Sales", f"${kpi_data['total_gross']:,.2f}")
            col3.metric("Received Amount", f"${kpi_data['total_received']:,.2f}")
            col4.metric("Pending Amount", f"${kpi_data['total_pending']:,.2f}")
        else:
            st.info("No sales data available for KPIs.")
    except Exception as e:
        st.error("Failed to load KPIs.")
        logger.error(f"Error loading KPIs: {e}")

    st.divider()

    # Fetch Sales over time
    sales_time_query = f"""
        SELECT sale_date, SUM(gross_sales) as daily_sales
        FROM customer_sales
        {where_clause}
        GROUP BY sale_date
        ORDER BY sale_date ASC
    """
    try:
        df_time = fetch_query(sales_time_query, tuple(params))
        if not df_time.empty:
            df_time['sale_date'] = pd.to_datetime(df_time['sale_date'])
            fig_time = px.line(df_time, x='sale_date', y='daily_sales', title='Daily Gross Sales Trend', markers=True)
            st.plotly_chart(fig_time, use_container_width=True)
        else:
            st.info("No daily sales data available for chart.")
    except Exception as e:
        st.error("Failed to load sales trend chart.")
        logger.error(f"Error loading sales trend: {e}")

    # Fetch Product distribution
    product_query = f"""
        SELECT product_name, COUNT(sale_id) as count
        FROM customer_sales
        {where_clause}
        GROUP BY product_name
        ORDER BY count DESC
    """
    try:
        df_product = fetch_query(product_query, tuple(params))
        if not df_product.empty:
            fig_product = px.pie(df_product, names='product_name', values='count', title='Sales by Product', hole=0.4)
            st.plotly_chart(fig_product, use_container_width=True)
    except Exception as e:
        st.error("Failed to load product distribution chart.")
        logger.error(f"Error loading product chart: {e}")

    # Export option
    st.divider()
    st.subheader("Data Export")
    export_query = f"SELECT * FROM customer_sales {where_clause} ORDER BY sale_date DESC"
    df_export = fetch_query(export_query, tuple(params))
    if not df_export.empty:
        csv = df_export.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Full Sales Data as CSV",
            data=csv,
            file_name='sales_data.csv',
            mime='text/csv',
        )
