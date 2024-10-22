import mysql.connector
from tkinter import *
from tkinter import messagebox

def insert_data():
    studentid = studentid_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    phonenumber = phonenumber_entry.get()

    if studentid == "" or name == "" or email == "" or phonenumber == "":
        messagebox.showerror("Input Error", "All fields are required")
        return

    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connection_python"
        )
        cursor = conn.cursor()

        insert_query = "INSERT INTO students (studentid, name, email, phonenumber) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (studentid, name, email, phonenumber))
        conn.commit()

        messagebox.showinfo("Success", "Data inserted successfully")

        studentid_entry.delete(0, END)
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        phonenumber_entry.delete(0, END)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

root = Tk()
root.title("Student Data Entry Form")

Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=10)
studentid_entry = Entry(root)
studentid_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Email").grid(row=2, column=0, padx=10, pady=10)
email_entry = Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=10)

Label(root, text="Phone Number").grid(row=3, column=0, padx=10, pady=10)
phonenumber_entry = Entry(root)
phonenumber_entry.grid(row=3, column=1, padx=10, pady=10)

submit_btn = Button(root, text="Submit", command=insert_data)
submit_btn.grid(row=4, columnspan=2, pady=10)

root.mainloop()
