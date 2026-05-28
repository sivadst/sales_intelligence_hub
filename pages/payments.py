import streamlit as st
import datetime
import pandas as pd
from db import execute_query, fetch_query
import logging

logger = logging.getLogger(__name__)

def render(user: dict):
    st.title("💳 Payments")
    st.markdown("Record new payments for existing open sales.")

    role = user.get("role", "")
    branch_id = user.get("branch_id")

    # Branch filter based on role
    where_clause = "WHERE pending_amount > 0 AND status = 'Open'"
    params = []
    if role != "Super Admin":
        where_clause += " AND branch_id = %s"
        params.append(branch_id)

    # Fetch open sales
    sales_query = f"""
        SELECT sale_id, customer_name, mobile_number, product_name, gross_sales, received_amount, pending_amount
        FROM customer_sales
        {where_clause}
        ORDER BY sale_date DESC
    """
    try:
        df_sales = fetch_query(sales_query, tuple(params))
    except Exception as e:
        st.error("Error fetching open sales.")
        logger.error(f"Error fetching sales in payments: {e}")
        return

    if df_sales.empty:
        st.info("No open sales with pending amounts found.")
        return

    st.subheader("Record Payment")
    
    # Select Sale
    sale_options = {
        f"{row['customer_name']} - {row['product_name']} (Pending: ${row['pending_amount']:,.2f})": row
        for _, row in df_sales.iterrows()
    }
    
    selected_sale_label = st.selectbox("Select Customer & Sale", options=list(sale_options.keys()))
    selected_sale = sale_options[selected_sale_label]

    st.write(f"**Gross Sales:** ${selected_sale['gross_sales']:,.2f} | **Received:** ${selected_sale['received_amount']:,.2f} | **Pending:** ${selected_sale['pending_amount']:,.2f}")

    with st.form("add_payment_form", clear_on_submit=True):
        payment_date = st.date_input("Payment Date", datetime.date.today())
        amount_paid = st.number_input("Payment Amount ($)", min_value=0.01, max_value=float(selected_sale['pending_amount']), format="%.2f")
        payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Bank Transfer", "Cheque", "Other"])
        
        # Optional: Auto close if full payment
        mark_closed = st.checkbox("Mark sale as Closed after this payment?", value=False)

        submit = st.form_submit_button("Record Payment")

        if submit:
            if amount_paid <= 0:
                st.error("Amount must be greater than zero.")
                return
            if amount_paid > selected_sale['pending_amount']:
                st.error("Payment cannot exceed the pending amount.")
                return

            try:
                # Insert Payment
                payment_query = """
                    INSERT INTO payment_splits (sale_id, payment_date, amount_paid, payment_method)
                    VALUES (%s, %s, %s, %s)
                """
                success, message = execute_query(payment_query, (int(selected_sale['sale_id']), payment_date, amount_paid, payment_method))
                
                if success:
                    st.success(f"Payment of ${amount_paid:,.2f} recorded for {selected_sale['customer_name']}.")
                    logger.info(f"Payment recorded: {amount_paid} for sale {selected_sale['sale_id']}")
                    
                    # Update status if requested or fully paid
                    new_pending = float(selected_sale['pending_amount']) - float(amount_paid)
                    if mark_closed or new_pending <= 0:
                        update_status_query = "UPDATE customer_sales SET status = 'Close' WHERE sale_id = %s"
                        execute_query(update_status_query, (int(selected_sale['sale_id']),))
                        st.info("Sale status updated to Closed.")
                        
                    st.rerun()
                else:
                    st.error(f"Failed to record payment: {message}")
            except Exception as e:
                st.error(f"Unexpected error: {e}")
                logger.error(f"Payment error: {e}")

    # Payment History for the selected sale
    st.divider()
    st.subheader(f"Payment History: {selected_sale['customer_name']}")
    history_query = "SELECT payment_date, amount_paid, payment_method FROM payment_splits WHERE sale_id = %s ORDER BY payment_date DESC"
    df_history = fetch_query(history_query, (int(selected_sale['sale_id']),))
    
    if not df_history.empty:
        st.dataframe(df_history, use_container_width=True)
    else:
        st.write("No payment history for this sale yet.")
