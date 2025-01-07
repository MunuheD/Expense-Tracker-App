# This script is is responsible for handling user registration, login, and authentication.
import hashlib
from utils.db_manager import connect_db
import sqlite3

class UserModel:
    # Hash the password using SHA-256 encryption
    @staticmethod
    def hash_password(password):
        """Hash the password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    # Register a new user in the database
    @staticmethod
    def register_user(username, password):
        """Register a new user."""
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
             # Check if the username already exists
            cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                conn.close()
                return "Username already exists!"
            
            # Hash the password before saving it
            hashed_password = UserModel.hash_password(password)
            try:
                # Insert the new user into the database
                cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, hashed_password))
                conn.commit()
                conn.close()
                return f"User {username} registered successfully!"
            except sqlite3.IntegrityError: # Handle database errors
                conn.close()
                return "Error during registration!"
        return "Failed to connect to the database."

    # Authenticate user login
    @staticmethod
    def login_user(username, password):
        """Authenticate user login."""
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            # Hash the entered password for comparison
            hashed_password = UserModel.hash_password(password)
            # Query for a matching username and password
            cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, hashed_password))
            user = cursor.fetchone() # Fetch user data if exists
            conn.close()
            return user # Return user data if authentication succeeds
        return None # Return None if authentication fails