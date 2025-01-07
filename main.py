# This script launches the application
from utils.db_manager import initialize_db
from views.auth_view import login_window

if __name__=="__main__":
    # Initialize the database
    initialize_db()
    #start the login window
    login_window.mainloop()




    
    
