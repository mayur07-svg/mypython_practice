import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    age = age_entry.get()
    city = city_entry.get()

    # You can also add validation here
    messagebox.showinfo("Form Data", f"Name: {name}\nAge: {age}\nCity: {city}")

# Create the main window
root = tk.Tk()
root.title("Simple Form")
root.geometry("300x200")

# Name
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Age
tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5, sticky="w")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

# City
tk.Label(root, text="City").grid(row=2, column=0, padx=10, pady=5, sticky="w")
city_entry = tk.Entry(root)
city_entry.grid(row=2, column=1)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Run the app
root.mainloop()
