import sqlite3 as sql
import tkinter as tk
from tkinter import ttk



# Create the SQLite database and tables (use your own createusers and createattable functions)
#def create_database():
#    createusers()
#    createattable()

# Function to fetch and display attendance for a specific user by their username
def show_attendance():
    conn = sql.connect('user_database.db')
    c = conn.cursor()
    
    # Fetch user ID based on the username
    c.execute("SELECT * FROM attable ")
    user_id = c.fetchone()
    
    # If there are user IDs, fetch attendance data and display it
    if user_id:
        # Reset the cursor to the first row
        c.execute("SELECT * FROM attable")
        
        # Fetch all attendance data
        attendance_data = c.fetchall()
        
        # Clear any previous data in the table
        for row in attendance_tree.get_children():
            attendance_tree.delete(row)
        
        # Display attendance data in the table
        for row in attendance_data:
             attendance_tree.insert('', 'end', values=row)
    else:
        print("User not found")
    
    conn.close()


# Create the main window
root = tk.Tk()
root.title("Student Attendance Viewer")
width=1200
height=300
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
        

# Create and configure the Treeview widget to display attendance data
attendance_tree = ttk.Treeview(root, columns=("Subject ID", "Subject", "Attended", "Bunked", "Percentage"))
attendance_tree.heading("#1", text="Subject ID")
attendance_tree.heading("#2", text="Subject")
attendance_tree.heading("#3", text="Attended")
attendance_tree.heading("#4", text="Bunked")
attendance_tree.heading("#5", text="Percentage")
attendance_tree.pack()

# # Create an entry field to input user's username
# username_label = tk.Label(root, text="Enter User Name:")
# username_label.pack()
# username_entry = tk.Entry(root)
# username_entry.pack()

# Create a button to display attendance
show_attendance_button = tk.Button(root, text="Show Attendance", command=show_attendance)
show_attendance_button.pack()

# Create the database and tables if they don't exist
#create_database()

root.mainloop()
