














import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Login Page")
window.geometry("300x200")

# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "user" and password == "pass":
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Create and place labels and entry widgets
tk.Label(window, text="Username").pack(pady=5)
username_entry = tk.Entry(window)
username_entry.pack(pady=5)

tk.Label(window, text="Password").pack(pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

# Create and place login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
window.mainloop()

    
    
