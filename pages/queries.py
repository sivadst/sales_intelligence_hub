import streamlit as st
import pandas as pd
from db import fetch_query
import logging

logger = logging.getLogger(__name__)

def render(user: dict):
    st.title("🔍 Queries")
    st.markdown("Search for specific customers and view their complete sales and payment history.")

    role = user.get("role", "")
    branch_id = user.get("branch_id")

    search_term = st.text_input("Search by Customer Name or Mobile Number", placeholder="e.g. John Doe or 1234567890")

    if not search_term:
        st.info("Enter a name or mobile number to search.")
        return

    # Build Query
    where_clause = "(customer_name LIKE %s OR mobile_number LIKE %s)"
    params = [f"%{search_term}%", f"%{search_term}%"]

    if role != "Super Admin":
        where_clause += " AND branch_id = %s"
        params.append(branch_id)

    search_query = f"""
        SELECT sale_id, branch_id, sale_date, customer_name, mobile_number, product_name, 
               gross_sales, received_amount, pending_amount, status
        FROM customer_sales
        WHERE {where_clause}
        ORDER BY sale_date DESC
    """

    try:
        df_results = fetch_query(search_query, tuple(params))
    except Exception as e:
        st.error("Error executing search query.")
        logger.error(f"Search query error: {e}")
        return

    if df_results.empty:
        st.warning("No customers found matching the search criteria.")
        return

    st.subheader(f"Search Results ({len(df_results)} found)")
    
    # Display each result in an expander
    for _, row in df_results.iterrows():
        with st.expander(f"{row['customer_name']} - {row['product_name']} ({row['sale_date']})"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Mobile:** {row['mobile_number']}")
                st.write(f"**Branch ID:** {row['branch_id']}")
                st.write(f"**Status:** {row['status']}")
            with col2:
                st.write(f"**Gross Sales:** ${row['gross_sales']:,.2f}")
                st.write(f"**Received:** ${row['received_amount']:,.2f}")
                st.write(f"**Pending:** ${row['pending_amount']:,.2f}")
                
                # Progress bar for payment completion
                if row['gross_sales'] > 0:
                    progress = min(row['received_amount'] / row['gross_sales'], 1.0)
                    st.progress(progress, text=f"Payment Progress: {progress*100:.1f}%")

            # Fetch payment history for this sale
            payments_query = """
                SELECT payment_date as 'Date', amount_paid as 'Amount Paid ($)', payment_method as 'Method'
                FROM payment_splits 
                WHERE sale_id = %s 
                ORDER BY payment_date DESC
            """
            try:
                df_payments = fetch_query(payments_query, (row['sale_id'],))
                if not df_payments.empty:
                    st.write("**Payment Splits**")
                    st.dataframe(df_payments, use_container_width=True, hide_index=True)
                else:
                    st.write("*No payment splits recorded for this sale.*")
            except Exception as e:
                st.error("Error loading payments.")
                logger.error(f"Payment load error in queries: {e}")
