from auth import hash_password
from db import execute_query

hashed_password = hash_password("admin123")

query = """
INSERT INTO users
(username, email, password_hash, branch_id, role)

VALUES (%s, %s, %s, %s, %s)
"""

execute_query(
query,
(
"superadmin",
"[superadmin@gmail.com](mailto:superadmin@gmail.com)",
hashed_password,
None,
"Super Admin"
)
)

print("User created successfully")
