# This script contains static methods for managing expenses in the application. These methods interact with the SQLite database to add, retrieve, search, update, and delete expenses.
from utils.db_manager import connect_db

class ExpenseModel:
    # Add a new expense to the database
    @staticmethod
    def add_expense(user_id, amount, category, description, date):
        conn = connect_db()   # Establish database connection
        cursor = conn.cursor()
        cursor.execute('INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?, ?, ?, ?, ?)',
                       (user_id, amount, category, description, date))
        conn.commit() # Save changes
        conn.close() # Close connection
    # Retrieve all expenses for a specific user
    @staticmethod
    def get_expenses(user_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses WHERE user_id = ?', (user_id,))
        expenses = cursor.fetchall() # Fetch all results
        conn.close()
        return expenses
    
    # Search expenses by date for a specific user
    @staticmethod
    def search_expenses_by_date(user_id, date):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses WHERE user_id = ? AND date = ?', (user_id, date))
        expenses = cursor.fetchall() # Fetch matching results
        conn.close()
        return expenses
    
    # Update an existing expense
    @staticmethod
    def update_expense(expense_id, amount, category, description, date):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('UPDATE expenses SET amount = ?, category = ?, description = ?, date = ? WHERE id = ?',
                       (amount, category, description, date, expense_id))
        conn.commit() # Save changes
        conn.close()

    # Delete an expense by ID
    @staticmethod
    def delete_expense(expense_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit() # Save changes
        conn.close()
