
# Expense Tracker App

## Overview
The Expense Tracker App is a desktop application built using Python and Tkinter that helps users manage their daily expenses. The application supports user registration, login, and the ability to add, view, update, delete, and search expenses. The app is powered by SQLite for database management and implements a simple, user-friendly graphical interface.

This repository contains the full source code for the Expense Tracker App. Below is a description of the project structure, installation instructions, and how to run the app.

---

## Project Structure
expense_tracker_app/
│
├── database/
│   └── app.db (SQLite Database File)
│
├── models/
│   ├── user_model.py
│   └── expense_model.py
│
├── utils/
│   └── db_manager.py
│
├── views/
│   ├── auth_view.py
│   └── expense_view.py
│
└── main.py
└── README.md

### Directory Breakdown:

- **database/**: Contains the SQLite database file (`app.db`) where user and expense data are stored.
- **models/**:
  - `user_model.py`: Defines the `UserModel` class for user-related operations such as registration, login, and password hashing.
  - `expense_model.py`: Defines the `ExpenseModel` class for operations related to expenses such as adding, viewing, updating, and deleting expenses.
- **utils/**:
  - `db_manager.py`: Handles database connections and initialization. It ensures the SQLite database and tables are set up correctly.
- **views/**:
  - `auth_view.py`: Manages the authentication views for signing up and logging in users.
  - `expense_view.py`: Manages the views for managing expenses, including adding, viewing, updating, and deleting expenses.
- **main.py**: The entry point for the application. It initializes the database and starts the authentication window.

## Features

- **User Authentication**:
  - Sign up and log in functionality.
  - Passwords are securely hashed using SHA-256.

- **Expense Management**:
  - Add new expenses with these details amount, category, description, and date.
  - View all recorded expenses.
  - Update and delete existing expenses.
  - Search for expenses by date.

- **Database**:
  - SQLite is used to manage user and expense data.
  - The app ensures the database and necessary tables are created during the first run.

---

## Installation

To get started with the Expense Tracker App, follow the steps below:

### Prerequisites

- Python 3.x
- Tkinter (Typically comes with Python)
- SQLite (Already included in Python's standard library)

### Steps

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd expense_tracker_app
   ```

2. **Install dependencies** (if needed):

   No external dependencies are required, as the app uses built-in Python libraries (Tkinter, SQLite3, hashlib).

3. **Initialize the database**:

   The first time the application is run, the `initialize_db()` function will automatically create the database and necessary tables.

4. **Run the application**:

   To start the application, run the following command:

   ```bash
   python main.py
   ```

   This will launch the authentication window, where you can sign up or log in.

---

## Usage

### 1. **User Registration**:
   - Enter a unique username and password to register.
   - The password is hashed using SHA-256 for security.
   - If the username already exists, an error message will be displayed.

### 2. **User Login**:
   - Enter your registered username and password to log in.
   - If authentication is successful, you will be redirected to the main expense management interface.

### 3. **Expense Management**:
   After logging in, you can:
   - **Add Expense**: Enter these expense details: amount, category, description, and date.
   - **View Expenses**: View a list of all recorded expenses.
   - **Search Expenses**: Search for expenses by date.
   - **Update Expense**: Modify an existing expense.
   - **Delete Expense**: Remove an expense from the database.

---

## Database

The SQLite database used by the app contains two tables:

1. **users**: Stores user data (username, password).
2. **expenses**: Stores expense data (amount, category, description, date, user_id).

---

## Contributing

We welcome contributions to improve the app. Feel free to fork the repository, submit issues, and make pull requests. When contributing, please follow these guidelines:

- Write clear commit messages.
- Ensure code adheres to PEP 8 standards.
- Ensure all tests pass (if applicable).


---

## Acknowledgements

- Tkinter for the GUI.
- SQLite for the lightweight database management.
- SHA-256 for secure password hashing.
