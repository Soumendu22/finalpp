import sqlite3 as sql
import tkinter as tk
from tkinter import ttk

# Function to fetch and display attendance for a specific user by their username
def show_attendance():
    # Get the username entered by the user
    username = username_entry.get()

    conn = sql.connect('user_database.db')
    c = conn.cursor()

    # Fetch user ID based on the username
    c.execute("SELECT id FROM users WHERE username = ?", (username,))
    user_id = c.fetchone()

    # If the user exists, fetch their attendance data and display it
    if user_id:
        user_id = user_id[0]  # Extract the user ID from the tuple
        # Fetch attendance data for the user
        c.execute("SELECT * FROM attable WHERE user_id = ?", (user_id,))
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

# Function to fetch and display attendance for all users
def show_all_attendance():
    conn = sql.connect('user_database.db')
    c = conn.cursor()

    # Fetch all attendance data
    c.execute("SELECT attable.id, users.username, attable.percentage FROM attable JOIN users ON attable.id = users.id")
    attendance_data = c.fetchall()

    # Clear any previous data in the table
    for row in attendance_tree.get_children():
        attendance_tree.delete(row)

    # Display attendance data in the table
    for row in attendance_data:
        attendance_tree.insert('', 'end', values=row)

    conn.close()

# Function to fetch and display attendance for each user
def show_attendance_for_each_user():
    conn = sql.connect('user_database.db')
    c = conn.cursor()

    # Fetch all users and their attendance data
    c.execute("SELECT users.id, users.username, attable.percentage FROM users LEFT JOIN attable ON users.id = attable.id")
    user_data = c.fetchall()

    # Clear any previous data in the table
    for row in attendance_tree.get_children():
        attendance_tree.delete(row)

    # Display attendance data for each user in the table
    for row in user_data:
        attendance_tree.insert('', 'end', values=row)

    conn.close()

# Create the main window
root = tk.Tk()
root.title("Student Attendance Viewer")
width = 1200
height = 300
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# Create and configure the Treeview widget to display attendance data
attendance_tree = ttk.Treeview(root, columns=("ID", "Username", "Percentage"))
attendance_tree.heading("#1", text="ID")
attendance_tree.heading("#2", text="Username")
attendance_tree.heading("#3", text="Percentage")
attendance_tree.pack()

# Create an entry field to input user's username
username_label = tk.Label(root, text="Enter User Name:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create buttons to display attendance for specific user, all users, and for each user
show_attendance_button = tk.Button(root, text="Show Attendance for User", command=show_attendance)
show_attendance_button.pack()

fetch_all_button = tk.Button(root, text="Show All Users' Attendance", command=show_all_attendance)
fetch_all_button.pack()

fetch_each_user_button = tk.Button(root, text="Show Attendance for Each User", command=show_attendance_for_each_user)
fetch_each_user_button.pack()

root.mainloop()
