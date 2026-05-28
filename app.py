import logging
import importlib
import sys
from typing import Dict, Any

import streamlit as st
from auth import authenticate_user

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
def configure_page() -> None:
    """Configure the Streamlit page layout and settings."""
    st.set_page_config(
        page_title="Sales Intelligence Hub",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Hide default Streamlit sidebar navigation to use custom routing
    hide_default_format = """
       <style>
       [data-testid="stSidebarNav"] {display: none;}
       </style>
       """
    st.markdown(hide_default_format, unsafe_allow_html=True)

# --- SESSION STATE ---
def init_session_state() -> None:
    """Initialize essential session state variables."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user" not in st.session_state:
        st.session_state.user = None
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Dashboard"

def login(email: str, password: str) -> None:
    """
    Handle user login attempt.
    
    Args:
        email (str): The provided email.
        password (str): The provided password.
    """
    try:
        user_data = authenticate_user(email, password)
        if user_data:
            st.session_state.authenticated = True
            st.session_state.user = user_data
            logger.info(f"User {user_data.get('username')} logged in successfully.")
            st.rerun()
        else:
            st.error("Invalid email or password. Please try again.")
            logger.warning(f"Failed login attempt for email: {email}")
    except Exception as e:
        logger.error(f"Login exception: {e}")
        st.error("An error occurred during authentication. Please try again later.")

def logout() -> None:
    """Clear session state and log out the user."""
    logger.info(f"User {st.session_state.user.get('username') if st.session_state.user else 'Unknown'} logged out.")
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.current_page = "Dashboard"
    st.rerun()

# --- UI COMPONENTS ---
def render_login_screen() -> None:
    """Render the enterprise login UI."""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.write("")
        st.write("")
        st.markdown("<h1 style='text-align: center;'>🚀 Sales Intelligence Hub</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: gray;'>Enterprise Authentication</h4>", unsafe_allow_html=True)
        st.write("")
        
        with st.form("login_form"):
            email = st.text_input("Email Address", placeholder="user@company.com")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            submit_button = st.form_submit_button("Secure Login", use_container_width=True)
            
            if submit_button:
                if not email or not password:
                    st.warning("Please enter both email and password.")
                else:
                    with st.spinner("Authenticating..."):
                        login(email, password)

def render_sidebar() -> None:
    """Render the authenticated user's sidebar with role-based routing."""
    user = st.session_state.user
    role = user.get("role", "Unknown")
    username = user.get("username", "User")
    branch_id = user.get("branch_id", "All")
    
    with st.sidebar:
        st.markdown("### 🏢 Intelligence Hub")
        st.divider()
        
        st.markdown(f"**User:** {username}")
        st.markdown(f"**Role:** {role}")
        st.markdown(f"**Branch:** {branch_id}")
        st.divider()
        
        # Define available pages based on role
        pages = {
            "Dashboard": {"icon": "📊", "module": "pages.dashboard"},
            "Add Customer": {"icon": "👤", "module": "pages.add_customer"},
            "Payments": {"icon": "💳", "module": "pages.payments"},
            "Reports": {"icon": "📈", "module": "pages.reports"},
            "Queries": {"icon": "🔍", "module": "pages.queries"}
        }
        
        # Super Admin access everything; Admin restricted if needed.
        # For demonstration, both see all but modules can enforce internal restrictions.
        allowed_pages = list(pages.keys())
        if role.lower() != "super admin":
            # Example restriction: Remove specific modules for lower roles if necessary
            # allowed_pages.remove("Queries")
            pass
            
        st.markdown("**Navigation**")
        for page in allowed_pages:
            button_label = f"{pages[page]['icon']} {page}"
            if st.button(button_label, use_container_width=True):
                st.session_state.current_page = page
                st.rerun()
                
        st.divider()
        if st.button("🚪 Logout", use_container_width=True, type="primary"):
            logout()

def load_page_module(page_name: str) -> None:
    """
    Dynamically load and render the selected page module.
    
    Args:
        page_name (str): The display name of the page to load.
    """
    module_mapping = {
        "Dashboard": "pages.dashboard",
        "Add Customer": "pages.add_customer",
        "Payments": "pages.payments",
        "Reports": "pages.reports",
        "Queries": "pages.queries"
    }
    
    module_name = module_mapping.get(page_name)
    if not module_name:
        st.error(f"Page module for '{page_name}' not configured.")
        return
        
    try:
        # Dynamically import the module
        page_module = importlib.import_module(module_name)
        # Attempt to run a render() or main() function if it exists
        if hasattr(page_module, "render"):
            page_module.render(st.session_state.user)
        elif hasattr(page_module, "main"):
            page_module.main(st.session_state.user)
        else:
            # Fallback: just show a placeholder if module has no entry point yet
            st.info(f"{page_name} loaded, but missing 'render(user)' function.")
    except ModuleNotFoundError:
        st.warning(f"Module '{module_name}' not found. Please create {module_name.replace('.', '/')}.py")
        logger.error(f"Module {module_name} not found.")
    except Exception as e:
        st.error(f"Failed to load {page_name}. See logs for details.")
        logger.error(f"Error loading {module_name}: {e}")

# --- MAIN APP ENTRY POINT ---
def main() -> None:
    """Main execution flow for the Streamlit application."""
    configure_page()
    init_session_state()
    
    if not st.session_state.authenticated:
        render_login_screen()
    else:
        render_sidebar()
        load_page_module(st.session_state.current_page)

if __name__ == "__main__":
    main()
