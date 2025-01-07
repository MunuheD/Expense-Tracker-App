# This script creates a GUI for user authentication and allows users to interact with an expense tracker application using Tkinter.
# After successful login, the user is redirected to the main expense tracker interface, which is managed by expense_view.py.

import tkinter as tk
from tkinter import messagebox
from models.user_model import UserModel
from models.expense_model import ExpenseModel


## Register a new user
def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    result = UserModel.register_user(username, password)
    messagebox.showinfo("Sign Up", result)

# Log in an existing user
def login():
    username = username_entry.get()
    password = password_entry.get()
    user = UserModel.login_user(username, password)

    if user:
        messagebox.showinfo("Login", f"Welcome {username}!")
        main_window(user[0])  # Pass user ID to the main window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Main dashboard window after login
def main_window(user_id):
    login_window.destroy() # Close the login window

    app = tk.Tk()
    app.title("Expense Tracker")

    tk.Label(app, text="Expense Tracker", font=("Arial", 16)).pack(pady=10)
    # Manage expenses button
    tk.Button(app, text="Manage Expenses", command=lambda: manage_expenses(user_id)).pack(pady=5)
    # logout button
    tk.Button(app, text="Logout", command=app.quit).pack(pady=10)

    app.mainloop()

# Expense management interface
def manage_expenses(user_id):
    app = tk.Toplevel()
    app.title("Expense Management")
    
    # Buttons for expense expense-related operations
    tk.Button(app, text="Add Expense", command=lambda: add_expense_window(user_id)).pack(pady=5)
    tk.Button(app, text="View Expenses", command=lambda: view_expenses_window(user_id)).pack(pady=5)
    tk.Button(app, text="Search Expenses", command=lambda: search_expenses_window(user_id)).pack(pady=5)
    tk.Button(app, text="Update Expense", command=lambda: update_expense_window(user_id)).pack(pady=5)
    tk.Button(app, text="Delete Expense", command=lambda: delete_expense_window(user_id)).pack(pady=5)
    tk.Button(app, text="Close", command=app.destroy).pack(pady=10)

# Add a new expense
def add_expense_window(user_id):
    def save_expense():
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()
        date = date_entry.get()
        
        ExpenseModel.add_expense(user_id, amount, category, description, date)
        messagebox.showinfo("Success", "Expense added successfully!")
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add Expense")

    # Form fields for adding an expense
    tk.Label(add_window, text="Amount:").pack()
    amount_entry = tk.Entry(add_window)
    amount_entry.pack()

    tk.Label(add_window, text="Category:").pack()
    category_entry = tk.Entry(add_window)
    category_entry.pack()

    tk.Label(add_window, text="Description:").pack()
    description_entry = tk.Entry(add_window)
    description_entry.pack()

    tk.Label(add_window, text="Date (YYYY-MM-DD):").pack()
    date_entry = tk.Entry(add_window)
    date_entry.pack()

    # Save expense button
    tk.Button(add_window, text="Save", command=save_expense).pack(pady=10)


# View all expenses
def view_expenses_window(user_id):
    expenses = ExpenseModel.get_expenses(user_id)
    
    view_window = tk.Toplevel()
    view_window.title("View Expenses")

    # Create a canvas and scrollbar
    canvas = tk.Canvas(view_window)
    scrollbar = tk.Scrollbar(view_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the expense information
    expense_frame = tk.Frame(canvas)

    # Display each expense inside the frame
    for expense in expenses:
        expense_info = f"ID: {expense[0]}, Amount: {expense[2]}, Date: {expense[3]}, Category: {expense[4]}, Description: {expense[5]}"
        tk.Label(expense_frame, text=expense_info).pack(pady=2)

    # Create a window in the canvas to hold the frame
    canvas.create_window((0, 0), window=expense_frame, anchor="nw")

    # Update the canvas scroll region
    expense_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Show the window
    view_window.mainloop()


# Search expenses by date
def search_expenses_window(user_id):
    def perform_search():
        date = date_entry.get()
        if not date:
            messagebox.showwarning("Input Required", "Please enter a date to search!")
            return
        results = ExpenseModel.search_expenses_by_date(user_id, date)
        result_window = tk.Toplevel()
        result_window.title("Search Results")
        # Display search results
        if results:
            for expense in results:
                tk.Label(result_window, text=f"ID: {expense[0]}, Amount: {expense[2]}, Date: {expense[3]}, Category: {expense[4]}, Description: {expense[5]}").pack()
        else:
            tk.Label(result_window, text="No expenses found for the given date.").pack()

    search_window = tk.Toplevel()
    search_window.title("Search Expenses")

    # Input field for date
    tk.Label(search_window, text="Enter Date (YYYY-MM-DD):").pack()
    date_entry = tk.Entry(search_window)
    date_entry.pack()

    # Search button
    tk.Button(search_window, text="Search", command=perform_search).pack(pady=10)

# Update an existing expense
def update_expense_window(user_id):
    def update_expense():
        expense_id = int(expense_id_entry.get())
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()
        date = date_entry.get()
        
        ExpenseModel.update_expense(expense_id, amount, category, description, date)
        messagebox.showinfo("Success", "Expense updated successfully!")
        update_window.destroy()

    update_window = tk.Toplevel()
    update_window.title("Update Expense")

    # Form fields for updating an expense
    tk.Label(update_window, text="Expense ID:").pack()
    expense_id_entry = tk.Entry(update_window)
    expense_id_entry.pack()

    tk.Label(update_window, text="Amount:").pack()
    amount_entry = tk.Entry(update_window)
    amount_entry.pack()

    tk.Label(update_window, text="Category:").pack()
    category_entry = tk.Entry(update_window)
    category_entry.pack()

    tk.Label(update_window, text="Description:").pack()
    description_entry = tk.Entry(update_window)
    description_entry.pack()

    tk.Label(update_window, text="Date (YYYY-MM-DD):").pack()
    date_entry = tk.Entry(update_window)
    date_entry.pack()

    # Save button
    tk.Button(update_window, text="Update", command=update_expense).pack(pady=10)

# Delete an expense
def delete_expense_window(user_id):
    def delete_expense():
        expense_id = int(expense_id_entry.get())
        ExpenseModel.delete_expense(expense_id)
        messagebox.showinfo("Success", "Expense deleted successfully!")
        delete_window.destroy()

    delete_window = tk.Toplevel()
    delete_window.title("Delete Expense")

    # Input field for expense ID
    tk.Label(delete_window, text="Expense ID:").pack()
    expense_id_entry = tk.Entry(delete_window)
    expense_id_entry.pack()
    # Delete button
    tk.Button(delete_window, text="Delete", command=delete_expense).pack(pady=10)

# Login window setup
login_window = tk.Tk()
login_window.title("User Authentication")

# Login form fields
tk.Label(login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Sign-up and login buttons
tk.Button(login_window, text="Sign Up", command=sign_up).pack()
tk.Button(login_window, text="Login", command=login).pack()

# Start the Tkinter main loop
login_window.mainloop()
