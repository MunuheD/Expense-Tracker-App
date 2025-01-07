import sqlite3
import os
# Path to the database file
DB_PATH = "E:/Coding and Data/PYTHON-APP DEV/expense tracker app/database/app.db" #"E:/expense tracker app/database/app.db" # Adjust to your correct directory, for instance "E:/expense tracker app/database/app.db". Remember, this database is automatically created, so the path must end with "...expense track app/database/app.db"


def initialize_db():
    """Create the database and initialize the tables."""
    try:
        # Check if the directory exists, if not create it
        db_dir = os.path.dirname(DB_PATH)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        # Connect to the SQLite database (this will create the database file if it doesn't exist)
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create the tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')
        print("Users table checked/created.")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                category TEXT,
                description TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
        ''')
        print("Expenses table checked/created.")

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        print("Database and tables initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def connect_db():
    """Connect to the SQLite database."""
    try:
        if not os.path.exists(DB_PATH):
            print("Database file not found, creating database...")
            initialize_db()

        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        print("Connected to the database.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    # Now initialize the database and create tables
    initialize_db()
    
