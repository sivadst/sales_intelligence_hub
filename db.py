import os
import sqlite3
import logging
from typing import Optional, Tuple, List
from contextlib import contextmanager
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "sales_hub.db")

def init_db():
    """Initialize the SQLite database with the required schema."""
    try:
        if not os.path.exists(DB_PATH):
            logger.info(f"Database {DB_PATH} does not exist. Initializing schema.")
            with sqlite3.connect(DB_PATH) as conn:
                # Enable foreign key support in SQLite
                conn.execute("PRAGMA foreign_keys = ON;")
                
                schema_path = os.path.join(BASE_DIR, "schema_sqlite.sql")
                if os.path.exists(schema_path):
                    with open(schema_path, "r") as f:
                        schema_sql = f.read()
                    # Execute script
                    conn.executescript(schema_sql)
                    conn.commit()
                    logger.info("Database initialized successfully.")
                else:
                    logger.error(f"Schema file {schema_path} not found.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")

# Initialize the database immediately when module is imported
init_db()

@contextmanager
def get_connection():
    """Context manager for safely acquiring and releasing a connection."""
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        # Force SQLite to enforce foreign keys
        conn.execute("PRAGMA foreign_keys = ON;")
        # Allow accessing columns by name
        conn.row_factory = sqlite3.Row
        yield conn
    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise
    finally:
        if conn:
            conn.close()

def _convert_query(query: str) -> str:
    """Convert MySQL placeholders (%s) to SQLite placeholders (?)."""
    # Replace all occurrences of %s with ?
    return query.replace("%s", "?")

def fetch_query(query: str, params: Optional[tuple] = None) -> pd.DataFrame:
    """
    Execute a SELECT query and return the results as a pandas DataFrame.
    """
    query = _convert_query(query)
    try:
        with get_connection() as conn:
            # Using pandas read_sql
            import warnings
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore', 'User provided connection.*')
                df = pd.read_sql(query, conn, params=params)
            return df
    except Exception as e:
        logger.error(f"Error fetching data with query: {e}")
        return pd.DataFrame()

def execute_query(query: str, params: Optional[tuple] = None) -> Tuple[bool, str]:
    """
    Execute an INSERT, UPDATE, or DELETE query safely.
    """
    query = _convert_query(query)
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, params or ())
                conn.commit()
                return True, "Success"
            except sqlite3.IntegrityError as e:
                conn.rollback()
                logger.warning(f"Integrity error: {e}")
                return False, f"Integrity Error: {e}"
            except sqlite3.Error as e:
                conn.rollback()
                logger.error(f"Transaction failed, rolled back. Error: {e}")
                return False, str(e)
    except Exception as e:
        logger.error(f"Failed to execute query: {e}")
        return False, str(e)

def execute_many(query: str, param_list: List[tuple]) -> Tuple[bool, str]:
    """
    Execute a query multiple times with a list of parameters (e.g., for bulk inserts).
    """
    query = _convert_query(query)
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.executemany(query, param_list)
                conn.commit()
                return True, f"Success. {cursor.rowcount} rows affected."
            except sqlite3.Error as e:
                conn.rollback()
                logger.error(f"Bulk execution failed, rolled back. Error: {e}")
                return False, str(e)
    except Exception as e:
        logger.error(f"Failed to bulk execute query: {e}")
        return False, str(e)
