import os
import logging
from typing import Optional, Tuple, List
from contextlib import contextmanager
import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

# Global connection pool
_pool = None

def get_connection_pool() -> pooling.MySQLConnectionPool:
    """Initialize and return the global database connection pool."""
    global _pool
    if _pool is None:
        try:
            pool_name = "sales_hub_pool"
            pool_size = int(os.getenv("DB_POOL_SIZE", "5"))
            
            dbconfig = {
                "host": os.getenv("DB_HOST", "localhost"),
                "user": os.getenv("DB_USER", "root"),
                "password": os.getenv("DB_PASS", ""),
                "database": os.getenv("DB_NAME", "sales_hub"),
                "charset": "utf8mb4",
                "collation": "utf8mb4_unicode_ci",
            }
            
            _pool = pooling.MySQLConnectionPool(
                pool_name=pool_name,
                pool_size=pool_size,
                pool_reset_session=True,
                **dbconfig
            )
            logger.info(f"Database connection pool '{pool_name}' created successfully with size {pool_size}.")
        except Error as e:
            logger.critical(f"Failed to create database connection pool: {e}")
            raise
    return _pool

@contextmanager
def get_connection():
    """Context manager for safely acquiring and releasing a connection from the pool."""
    pool = get_connection_pool()
    conn = None
    try:
        conn = pool.get_connection()
        if conn.is_connected():
            yield conn
        else:
            raise Error("Connection acquired from pool is not connected.")
    except Error as e:
        logger.error(f"Error getting connection from pool: {e}")
        raise
    finally:
        if conn and conn.is_connected():
            conn.close()

def fetch_query(query: str, params: Optional[tuple] = None) -> pd.DataFrame:
    """
    Execute a SELECT query and return the results as a pandas DataFrame.
    """
    try:
        with get_connection() as conn:
            # Suppress pandas UserWarning about using raw DBAPI connection instead of SQLAlchemy
            import warnings
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore', 'User provided connection.*')
                df = pd.read_sql(query, conn, params=params)
            return df
    except Exception as e:
        logger.error(f"Error fetching data with query: {e}")
        # Return an empty dataframe to avoid breaking downstream code that expects a DataFrame
        return pd.DataFrame()

def execute_query(query: str, params: Optional[tuple] = None) -> Tuple[bool, str]:
    """
    Execute an INSERT, UPDATE, or DELETE query safely.
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, params or ())
                conn.commit()
                return True, "Success"
            except Error as e:
                conn.rollback()
                logger.error(f"Transaction failed, rolled back. Error: {e}")
                return False, str(e)
            finally:
                cursor.close()
    except Exception as e:
        logger.error(f"Failed to execute query: {e}")
        return False, str(e)

def execute_many(query: str, param_list: List[tuple]) -> Tuple[bool, str]:
    """
    Execute a query multiple times with a list of parameters (e.g., for bulk inserts).
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.executemany(query, param_list)
                conn.commit()
                return True, f"Success. {cursor.rowcount} rows affected."
            except Error as e:
                conn.rollback()
                logger.error(f"Bulk execution failed, rolled back. Error: {e}")
                return False, str(e)
            finally:
                cursor.close()
    except Exception as e:
        logger.error(f"Failed to bulk execute query: {e}")
        return False, str(e)
