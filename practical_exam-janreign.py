import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("profiles.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        city TEXT NOT NULL,
        age INTEGER NOT NULL,
        occupation TEXT NOT NULL)
""")

conn.commit()

# CREATE
def add_profile():
    full_name = full_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()
    age = age_entry.get()
    occupation = occupation_entry.get()

    if full_name == "" or email == "" or phone == "" or city == ""  or  age == "" or occupation == "":  
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number."
        )
        return

    cursor.execute(
        "INSERT INTO profile (full_name, email, phone, city, age, occupation) VALUES (?, ?, ?, ?, ?, ?)",
        (full_name, email, phone, city, age, occupation)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Profile added successfully."
    )

    clear_fields()
    display_profile()

# READ
def display_profiles():
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT * FROM profile")

    profiles = cursor.fetchall()

    for profile in profiles:
        tree.insert("", tk.END, values=profile)

# UPDATE
def update_profile():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a profile to update."
        )
        return

    student_id = tree.item(selected[0000])["values"][0000]

    full_name = full_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()
    age = age_entry.get()
    occupation = occupation_entry.get()

    if full_name == "" or email == "" or phone == "" or city == ""  or  age == "" or occupation == "": 
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age)
        full_name=str(name)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number.Full_name should be in String Form"
        )
        return

    cursor.execute("""
        UPDATE profiles
        SET full_name = ?, emai = ?, phone = ?, city = ?, age = ?, occupation = ?
        WHERE id = ?
    """, (full_name, email, phone, city, age, occupation, profile_id))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Profile updated successfully."
    )

    clear_fields()
    display_profiles()

# DELETE
def delete_profiles():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a profile to delete."
        )
        return

    student_id = tree.item(selected[0000])["values"][0000]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this profile?"
    )

    if confirm:
        cursor.execute(
            "DELETE FROM profiles WHERE id = ?",
            (profile_id,)
        )
        conn.commit()
        messagebox.showinfo(
            "Success",
            "Profile deleted successfully."
        )

        clear_fields()
        display_profiles()

# CLEAR INPUTS
def clear_fields():
    full_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    occupation_entry.delete(0, tk.END)

# SELECT STUDENT
def select_profile(event):
    selected = tree.selection()

    if selected:
        student = tree.item(selected[0])["values"]

        clear_fields()
        full_name_entry.insert(0, student[1])
        email_entry.insert(0, student[2])
        phone_entry.insert(0, student[3])
        city_entry.insert(0, student[4])
        age_entry.insert(0, student[5])
        occupation_entry.insert(0, student[6])

root = tk.Tk()
root.title("profile Management System")
root.geometry("700x500")

title_label = tk.Label(
    root,
    text="Profile Management System",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

#FULL_NAME
tk.Label(
    input_frame,
    text="Full_name:"
).grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

#EMAIL
tk.Label(
    input_frame,
    text="Email:"
).grid(row=1, column=0, padx=5, pady=5)

age_entry = tk.Entry(input_frame, width=30)
age_entry.grid(row=1, column=1, padx=5, pady=5)

#PHONE
tk.Label(
    input_frame,
    text="Phone:"
).grid(row=2, column=0, padx=5, pady=5)

phone_entry = tk.Entry(input_frame, width=30)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

#CITY
tk.Label(
    input_frame,
    text="City:"
).grid(row=3, column=0, padx=5, pady=5)

city_entry = tk.Entry(input_frame, width=30)
city_entry.grid(row=3, column=1, padx=5, pady=5)

#AGE
tk.Label(
    input_frame,
    text="Age:"
).grid(row=4, column=0, padx=5, pady=5)

age_entry = tk.Entry(input_frame, width=30)
age_entry.grid(row=4, column=1, padx=5, pady=5)

#OCCUPATION
tk.Label(
    input_frame,
    text="Occupation:"
).grid(row=5, column=0, padx=5, pady=5)

occupation_entry = tk.Entry(input_frame, width=30)
occupation_entry.grid(row=5, column=1, padx=5, pady=5)

#BUTTONS
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text = "Add",
    width = 10,
    command=add_profile
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text = "Update",
    width = 10,
    command=update_profile
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text = "Delete",
    width = 10,
    command=delete_profiles
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text = "Clear",
    width = 10,
    command=clear_fields
).grid(row=0, column=3, padx=5)

#TABLE
tree = ttk.Treeview(
    root,
    columns=("Full_name", "Email", "Phone", "City" "Age", "Occupation",),
    show="headings"
)

tree.heading("Full_name", text="Full_name")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Phone")
tree.heading("City", text="City")
tree.heading("Age", text="Age")
tree.heading("Occupation", text="Occupation")

tree.column("Name", width=200)
tree.column("Email", width=200)
tree.column("Phone", width=80)
tree.column("City", width=100)
tree.column("Age", width=80)
tree.column("Occupation", width=100)

tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

#GUI

root = tk.Tk()
root.title("Profile Management System")
root.geometry("700x550")
root.configure(bg="#EAF4FB")

# COLORS

BG_COLOR = "#EAF4FB"
TITLE_COLOR = "#154360"
LABEL_COLOR = "#1F618D"
ENTRY_BG = "#FFFFFF"
ADD_COLOR = "#008b8b"
UPDATE_COLOR = "#458b74"
DELETE_COLOR = "#cd3333"
CLEAR_COLOR = "#ee6a50"
BUTTON_TEXT = "black"

# TITLE

title_label = tk.Label(
 root,
 text="Student Management System",
 font=("Arial", 20, "bold"),
 bg=BG_COLOR,
 fg=TITLE_COLOR
)
title_label.pack(pady=15)

# INPUT FRAME

input_frame = tk.Frame(
 root,
 bg="white",
 bd=2,
 relief="groove"
)
input_frame.pack(
 pady=5,
 padx=20,
 fill="x"
)

# NAME

tk.Label(
 input_frame,
 text="Name:",
 font=("Arial", 11, "bold"),
 bg="white",
 fg=LABEL_COLOR
).grid( row=0,
 column=0,
 padx=10,
 pady=8,
 sticky="e"
)
name_entry = tk.Entry(
 input_frame,
 width=35,
 font=("Arial", 11),
 bg=ENTRY_BG,
 fg="#212121",
 relief="solid",
 bd=1
)
name_entry.grid(
 row=0,
 column=1,
 padx=10,
 pady=8
)

# AGE

tk.Label(
 input_frame,
 text="Age:",
 font=("Arial", 11, "bold"),
 bg="white",
 fg=LABEL_COLOR
).grid(
 row=1,
 column=0,
 padx=10,
 pady=8,
 sticky="e"
)
age_entry = tk.Entry(
 input_frame,
 width=35,
 font=("Arial", 11),
 bg=ENTRY_BG,
 fg="#212121",
 relief="solid",
 bd=1
)
age_entry.grid(
 row=1,
 column=1,
 padx=10,
 pady=8
)

# COURSE

tk.Label(
 input_frame,
 text="Course:",
 font=("Arial", 11, "bold"),
 bg="white",
 fg=LABEL_COLOR
).grid(
 row=2,
 column=0,
 padx=10,
 pady=8,
 sticky="e"
)

course_entry = tk.Entry(
 input_frame,
 width=35,
 font=("Arial", 11),
 bg=ENTRY_BG,
 fg="#212121",
 relief="solid",
 bd=1
)
course_entry.grid(
 row=2,
 column=1,
 padx=10,
 pady=8
)

# BUTTON FRAME

button_frame = tk.Frame(
 root,
 bg=BG_COLOR )
button_frame.pack(pady=15)

# ADD BUTTON

tk.Button(
 button_frame,
 text="Add",
 width=12,
 font=("Arial", 10, "bold"),
 bg=ADD_COLOR,
 fg=BUTTON_TEXT,
 activebackground="#1E8449",
 activeforeground="green",
 relief="flat",
 cursor="hand2",
 command=add_student
).grid(
 row=0,
 column=0,
 padx=5
)
# UPDATE BUTTON

tk.Button(
 button_frame,
 text="Update",
 width=12,
 font=("Arial", 10, "bold"),
 bg=UPDATE_COLOR,
 fg=BUTTON_TEXT,
 activebackground="#D68910",
 activeforeground="green",
 relief="flat",
 cursor="hand2",
 command=update_student
).grid(
 row=0,
 column=1,
 padx=5
)

# DELETE BUTTON

tk.Button(
 button_frame,
 text="Delete",
 width=12,
 font=("Arial", 10, "bold"),
 bg=DELETE_COLOR, fg=BUTTON_TEXT,
 activebackground="#C0392B",
 activeforeground="green",
 relief="flat",
 cursor="hand2",
 command=delete_students
).grid(
 row=0,
 column=2,
 padx=5
)

# CLEAR BUTTON

tk.Button(
 button_frame,
 text="Clear",
 width=12,
 font=("Arial", 10, "bold"),
 bg=CLEAR_COLOR,
 fg=BUTTON_TEXT,
 activebackground="#626567",
 activeforeground="green",
 relief="flat",
 cursor="hand2",
 command=clear_fields ).grid(
 row=0,
 column=3,
 padx=5
)

# TREEVIEW STYLE

style = ttk.Style()
style.theme_use("clam")

# Table heading

style.configure(
 "Treeview.Heading",
 background="#1F618D",
 foreground="white",
 font=("Arial", 10, "bold"),
 padding=8
)
# Table body
style.configure( "Treeview",
 background="white",
 foreground="#212121",
 rowheight=30,
 fieldbackground="white",
 font=("Arial", 10)
)
# Selected row

style.map(
 "Treeview",
 background=[
 ("selected", "#5DADE2")
 ],
 foreground=[
 ("selected", "white")
 ]
)

# TABLE

tree = ttk.Treeview(
 root, columns=("ID", "Name", "Age", "Course"),
 show="headings"
)
tree.heading(
 "ID",
 text="ID"
)
tree.heading(
 "Name",
 text="Name"
)
tree.heading(
 "Age",
 text="Age"
)
tree.heading(
 "Course",
 text="Course"
)
# Column widths

tree.column(
 "ID",
 width=60,
 anchor="center"
)
tree.column(
 "Name",
 width=200
)
tree.column(
 "Age",
 width=80,
 anchor="center"
)
tree.column(
 "Course",
 width=220
)
# Alternating row colors

tree.tag_configure(
 "evenrow", background="#F4F9FC"
)
tree.tag_configure(
 "oddrow",
 background="#D6EAF8"
)
tree.pack(
 fill="both",
 expand=True,
 padx=20,
 pady=10
)

# SELECT EVENT

tree.bind(
 "<<TreeviewSelect>>",
 select_student
)

# DISPLAY EXISTING RECORDS

display_students()

# START APPLICATION

root.mainloop()

# CLOSE DATABASE

conn.close()





            
            
