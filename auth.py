import logging
import bcrypt
from typing import Optional, Dict, Any
import pandas as pd
from db import fetch_query

# Configure logging for the authentication module
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def hash_password(password: str) -> str:
    """
    Generate a secure bcrypt hash for a given plaintext password.
    
    Args:
        password (str): The plaintext password to hash.
        
    Returns:
        str: The decoded utf-8 string of the generated bcrypt hash.
    """
    try:
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_bytes.decode('utf-8')
    except Exception as e:
        logger.error(f"Error occurred during password hashing: {e}")
        raise

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Securely verify a plaintext password against a stored bcrypt hash.
    
    Args:
        plain_password (str): The provided plaintext password.
        hashed_password (str): The stored bcrypt hash.
        
    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    try:
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
    except Exception as e:
        logger.error(f"Error occurred during password verification: {e}")
        return False

def authenticate_user(email: str, password: str) -> Optional[Dict[str, Any]]:
    """
    Authenticate a user by email and password.
    
    Args:
        email (str): The user's email address.
        password (str): The provided plaintext password.
        
    Returns:
        Optional[Dict[str, Any]]: A dictionary containing user details on successful 
                                  authentication, or None if authentication fails.
    """
    try:
        query = """
            SELECT user_id, username, email, password_hash, role, branch_id 
            FROM users 
            WHERE email = %s
            LIMIT 1
        """
        
        df = fetch_query(query, params=(email,))
        
        if df is None or df.empty:
            logger.warning(f"Authentication failed: No user found with email {email}")
            return None
            
        user_record = df.iloc[0]
        stored_hash = user_record.get('password_hash')
        
        if not stored_hash:
            logger.error(f"Authentication failed: Missing password hash for email {email}")
            return None
            
        is_valid = verify_password(password, stored_hash)
        
        if is_valid:
            logger.info(f"User authenticated successfully: {email}")
            return {
                "user_id": int(user_record['user_id']),
                "username": str(user_record['username']),
                "role": str(user_record['role']),
                "branch_id": int(user_record['branch_id']) if pd.notna(user_record['branch_id']) else None
            }
        else:
            logger.warning(f"Authentication failed: Invalid password provided for {email}")
            return None
            
    except Exception as e:
        logger.error(f"System error during authentication flow for {email}: {e}")
        return None
