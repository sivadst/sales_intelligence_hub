import streamlit as st
import datetime
from db import execute_query, fetch_query
import logging

logger = logging.getLogger(__name__)

def render(user: dict):
    st.title("👤 Add Customer & Sale")
    st.markdown("Register a new customer and log their initial sale.")

    role = user.get("role", "")
    user_branch_id = user.get("branch_id")

    # If Super Admin, fetch branches so they can choose
    branches = []
    if role == "Super Admin":
        try:
            df_branches = fetch_query("SELECT branch_id, branch_name FROM branches")
            branches = df_branches.to_dict('records') if not df_branches.empty else []
        except Exception as e:
            st.error("Error fetching branches.")
            logger.error(f"Error fetching branches: {e}")
            return

    with st.form("add_customer_form", clear_on_submit=True):
        st.subheader("Customer Details")
        customer_name = st.text_input("Customer Name", max_chars=100)
        mobile_number = st.text_input("Mobile Number", max_chars=15, help="Must be unique. Format: digits only.")

        st.subheader("Sale Details")
        
        # Branch Selection
        selected_branch_id = user_branch_id
        if role == "Super Admin" and branches:
            branch_options = {f"{b['branch_name']} (ID: {b['branch_id']})": b['branch_id'] for b in branches}
            selected_branch_name = st.selectbox("Branch", options=list(branch_options.keys()))
            selected_branch_id = branch_options[selected_branch_name]
        elif role == "Super Admin" and not branches:
            st.warning("No branches found in database. Cannot add sale.")
            st.form_submit_button("Submit")
            return
            
        sale_date = st.date_input("Sale Date", datetime.date.today())
        product_name = st.text_input("Product Name", max_chars=30)
        gross_sales = st.number_input("Gross Sales ($)", min_value=0.0, format="%.2f")
        received_amount = st.number_input("Initial Received Amount ($)", min_value=0.0, format="%.2f")
        status = st.selectbox("Sale Status", options=["Open", "Close"])

        submit = st.form_submit_button("Register Customer & Sale")

        if submit:
            # Validation
            if not customer_name or not mobile_number or not product_name:
                st.error("Customer Name, Mobile Number, and Product Name are required.")
                return
            if received_amount > gross_sales:
                st.error("Received amount cannot exceed gross sales.")
                return

            try:
                # Insert Query
                insert_query = """
                    INSERT INTO customer_sales 
                    (branch_id, sale_date, customer_name, mobile_number, product_name, gross_sales, received_amount, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                params = (
                    selected_branch_id,
                    sale_date,
                    customer_name,
                    mobile_number,
                    product_name,
                    gross_sales,
                    received_amount,
                    status
                )
                
                success, message = execute_query(insert_query, params)
                
                if success:
                    st.success(f"Successfully added customer {customer_name} and recorded sale.")
                    logger.info(f"User {user.get('username')} added a new sale for {customer_name}.")
                else:
                    if "Duplicate entry" in message and "mobile_number" in message:
                        st.error("A customer with this mobile number already exists.")
                    else:
                        st.error(f"Failed to add customer: {message}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
                logger.error(f"Add customer exception: {e}")
