import argparse
from auth import hash_password
from db import execute_query

def create_super_admin(email, password):
    hashed_password = hash_password(password)

    query = """
    INSERT INTO users 
    (username, email, password_hash, branch_id, role)
    VALUES (%s, %s, %s, %s, %s)
    """

    success, message = execute_query(
        query,
        (
            "superadmin",
            email,
            hashed_password,
            None,
            "Super Admin"
        )
    )

    if success:
        print(f"Super Admin user created successfully with email: {email}")
    else:
        print(f"Failed to create user: {message}")

if __name__ == "__main__":
    create_super_admin("superadmin@gmail.com", "admin123")
