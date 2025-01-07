# This script provide a graphical user interface (GUI) for users to manage their expenses, including adding, viewing, searching, updating, and deleting records in the expense tracker.
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from models.expense_model import ExpenseModel

# Main interface for managing expenses
def manage_expenses(user_id):
    """Main expense management interface."""
    app = tk.Toplevel()
    app.title("Expense Management")
    
    # Buttons to navigate different expense management features
    tk.Button(app, text="Add Expense", command=lambda: add_expense_window(user_id)).pack(pady=5)
    tk.Button(app, text="View Expenses", command=lambda: view_expenses_window(user_id)).pack(pady=5)
    tk.Button(app, text="Search Expenses", command=lambda: search_expenses_window(user_id)).pack(pady=5)
    tk.Button(app, text="Update Expense", command=lambda: update_expense_window(user_id)).pack(pady=5)
    tk.Button(app, text="Delete Expense", command=lambda: delete_expense_window(user_id)).pack(pady=5)
    tk.Button(app, text="Close", command=app.destroy).pack(pady=10)

# Window for adding a new expense
def add_expense_window(user_id):
    """Window for adding a new expense."""
    def save_expense():
        # Collect user input and save the expense
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()
        date = date_entry.get()
        
        ExpenseModel.add_expense(user_id, amount, category, description, date)
        messagebox.showinfo("Success", "Expense added successfully!")
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add Expense")

    # Input fields for expense details
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

    # Save button to trigger expense saving
    tk.Button(add_window, text="Save", command=save_expense).pack(pady=10)


# Window for viewing all expenses
def view_expenses_window(user_id):
    expenses = ExpenseModel.get_expenses(user_id)

    view_window = tk.Toplevel()
    view_window.title("View Expenses")

    # Create a canvas to hold everything
    canvas = tk.Canvas(view_window)
    canvas.grid(row=0, column=0, sticky="news")  # grid layout

    # Add a vertical scrollbar that will be linked to the canvas
    scrollbar = ttk.Scrollbar(view_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")  # grid layout

    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to contain the expense items
    scrollable_frame = tk.Frame(canvas)

    # Create a window inside the canvas to hold the scrollable_frame
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Fill the frame with expense items
    for expense in expenses:
        expense_info = f"ID: {expense[0]}, Amount: {expense[2]}, Date: {expense[3]}, Category: {expense[4]}, Description: {expense[5]}"
        tk.Label(scrollable_frame, text=expense_info).grid(sticky="w", padx=10, pady=2)

    # This ensures the scroll region of the canvas is updated after widgets are added
    def update_scroll_region(event=None):
        canvas.config(scrollregion=canvas.bbox("all"))

    # Binding the resize event to update the scrollable area
    scrollable_frame.bind("<Configure>", update_scroll_region)

    # Ensure canvas and scrollbar are resized as window is resized
    view_window.grid_rowconfigure(0, weight=1)
    view_window.grid_columnconfigure(0, weight=1)




# Window for searching expenses by date
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
    # Search button to initiate the search
    tk.Button(search_window, text="Search", command=perform_search).pack(pady=10)

# Window for updating an existing expense
def update_expense_window(user_id):
    def update_expense():
        # Collect user input and update the expense
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

    # Input fields for expense details
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

    # Update button to trigger expense updating
    tk.Button(update_window, text="Update", command=update_expense).pack(pady=10)

# Window for deleting an expense
def delete_expense_window(user_id):
    def delete_expense():
        # Delete the expense with the provided ID
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

    # Delete button to trigger expense deletion
    tk.Button(delete_window, text="Delete", command=delete_expense).pack(pady=10)
