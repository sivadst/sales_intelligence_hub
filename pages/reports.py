import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
from db import fetch_query
import logging

logger = logging.getLogger(__name__)

def render(user: dict):
    st.title("📈 Reports")
    st.markdown("Generate and export detailed sales reports.")

    role = user.get("role", "")
    user_branch_id = user.get("branch_id")

    # Filters
    st.sidebar.header("Report Filters")
    
    # Date Range
    today = datetime.date.today()
    first_day = today.replace(day=1)
    start_date = st.sidebar.date_input("Start Date", first_day)
    end_date = st.sidebar.date_input("End Date", today)

    # Branch Filter
    selected_branch_id = None
    if role == "Super Admin":
        try:
            df_branches = fetch_query("SELECT branch_id, branch_name FROM branches")
            if not df_branches.empty:
                branch_options = {"All Branches": None}
                for _, row in df_branches.iterrows():
                    branch_options[row['branch_name']] = row['branch_id']
                
                selected_branch_name = st.sidebar.selectbox("Branch", list(branch_options.keys()))
                selected_branch_id = branch_options[selected_branch_name]
        except Exception as e:
            logger.error(f"Error loading branches for reports: {e}")
    else:
        selected_branch_id = user_branch_id

    # Status Filter
    status_filter = st.sidebar.selectbox("Status", ["All", "Open", "Close"])

    # Build Query
    base_query = """
        SELECT s.sale_id, b.branch_name, s.sale_date, s.customer_name, s.mobile_number, 
               s.product_name, s.gross_sales, s.received_amount, s.pending_amount, s.status
        FROM customer_sales s
        JOIN branches b ON s.branch_id = b.branch_id
        WHERE s.sale_date BETWEEN %s AND %s
    """
    params = [start_date, end_date]

    if selected_branch_id is not None:
        base_query += " AND s.branch_id = %s"
        params.append(selected_branch_id)

    if status_filter != "All":
        base_query += " AND s.status = %s"
        params.append(status_filter)
        
    base_query += " ORDER BY s.sale_date DESC"

    # Fetch Data
    with st.spinner("Generating report..."):
        try:
            df_report = fetch_query(base_query, tuple(params))
        except Exception as e:
            st.error("Failed to generate report.")
            logger.error(f"Report generation error: {e}")
            return

    if df_report.empty:
        st.warning("No records found for the selected filters.")
        return

    # Display Metrics
    st.subheader("Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records", len(df_report))
    col2.metric("Total Gross Sales", f"${df_report['gross_sales'].sum():,.2f}")
    col3.metric("Total Received", f"${df_report['received_amount'].sum():,.2f}")
    col4.metric("Total Pending", f"${df_report['pending_amount'].sum():,.2f}")

    # Visual Analytics
    st.subheader("Analytics")
    df_report['sale_date'] = pd.to_datetime(df_report['sale_date'])
    sales_trend = df_report.groupby(['sale_date', 'branch_name'])['gross_sales'].sum().reset_index()
    fig = px.bar(sales_trend, x='sale_date', y='gross_sales', color='branch_name', 
                 title="Daily Gross Sales by Branch", labels={'gross_sales': 'Gross Sales ($)', 'sale_date': 'Date', 'branch_name': 'Branch'})
    st.plotly_chart(fig, use_container_width=True)

    # Display DataGrid
    st.subheader("Detailed Data")
    st.dataframe(df_report, use_container_width=True, hide_index=True)

    # Export
    st.divider()
    csv = df_report.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Report as CSV",
        data=csv,
        file_name=f'sales_report_{start_date}_to_{end_date}.csv',
        mime='text/csv',
    )
