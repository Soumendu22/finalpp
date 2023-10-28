import sqlite3 as sql
import tkinter as tk
from tkinter import ttk

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

# Create a Tkinter window
root = tk.Tk()
root.title("Attendance Viewer")

# Add a button to fetch and display attendance for all users
fetch_all_button = tk.Button(root, text="Show All Users' Attendance", command=show_all_attendance)
fetch_all_button.pack()

fetch_each_user_button = tk.Button(root, text="Show Attendance for Each User", command=show_attendance_for_each_user)
fetch_each_user_button.pack()

# Create a Treeview widget to display attendance data
attendance_tree = ttk.Treeview(root, columns=("ID", "Username", "Percentage"))
attendance_tree.heading("#1", text="ID")
attendance_tree.heading("#2", text="Username")
attendance_tree.heading("#3", text="Percentage")
attendance_tree.pack()

fetch_each_user_button = tk.Button(root, text="Show Attendance for Each User", command=show_attendance_for_each_user)
fetch_each_user_button.pack()

root.mainloop()
