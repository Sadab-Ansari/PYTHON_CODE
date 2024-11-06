# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector

# def insert_data():
#     emp_id = entry_emp_id.get()
#     emp_name = entry_emp_name.get()
#     salary = entry_salary.get()
#     desig = entry_desig.get()

#     try:
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",
#             database="connection_python"
#         )
#         cursor = conn.cursor()
#         query = "INSERT INTO employee (emp_id, emp_name, salary, desig) VALUES (%s, %s, %s, %s)"
#         cursor.execute(query, (emp_id, emp_name, salary, desig))
#         conn.commit()
#         messagebox.showinfo("Success", "Data inserted successfully")
#     except mysql.connector.Error as err:
#         messagebox.showerror("Error", f"Error: {err}")
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# root = tk.Tk()
# root.title("Employee Data Entry")

# tk.Label(root, text="Employee ID").grid(row=0, column=0)
# entry_emp_id = tk.Entry(root)
# entry_emp_id.grid(row=0, column=1)

# tk.Label(root, text="Employee Name").grid(row=1, column=0)
# entry_emp_name = tk.Entry(root)
# entry_emp_name.grid(row=1, column=1)

# tk.Label(root, text="Salary").grid(row=2, column=0)
# entry_salary = tk.Entry(root)
# entry_salary.grid(row=2, column=1)

# tk.Label(root, text="Designation").grid(row=3, column=0)
# entry_desig = tk.Entry(root)
# entry_desig.grid(row=3, column=1)

# insert_button = tk.Button(root, text="Insert Data", command=insert_data)
# insert_button.grid(row=4, column=0, columnspan=2)

# root.mainloop()


















import tkinter as tk
from tkinter import messagebox
import mysql.connector

def insert_data():
    emp_id = entry_emp_id.get()
    emp_name = entry_emp_name.get()
    salary = entry_salary.get()
    desig = entry_desig.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connection_python"
        )
        cursor = conn.cursor()
        query = "INSERT INTO employee (emp_id, emp_name, salary, desig) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (emp_id, emp_name, salary, desig))
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def retrieve_data():
    emp_name = entry_emp_name.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connection_python"
        )
        cursor = conn.cursor()
        query = "SELECT emp_id, salary, desig FROM employee WHERE emp_name = %s"
        cursor.execute(query, (emp_name,))
        result = cursor.fetchone()

        if result:
            entry_emp_id.delete(0, tk.END)
            entry_emp_id.insert(0, result[0])

            entry_salary.delete(0, tk.END)
            entry_salary.insert(0, result[1])

            entry_desig.delete(0, tk.END)
            entry_desig.insert(0, result[2])

            messagebox.showinfo("Success", "Data retrieved successfully")
        else:
            messagebox.showinfo("Not Found", "No record found for the provided name")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

root = tk.Tk()
root.title("Employee Data Entry")
root.configure(bg="#f0f0f5")
root.geometry("400x300")

# Label and Entry styling
label_style = {"bg": "#f0f0f5", "fg": "#333333", "font": ("Arial", 12)}
entry_style = {"bg": "#ffffff", "fg": "#333333", "font": ("Arial", 12)}

tk.Label(root, text="Employee ID", **label_style).grid(row=0, column=0, pady=5, padx=5, sticky="e")
entry_emp_id = tk.Entry(root, **entry_style)
entry_emp_id.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Employee Name", **label_style).grid(row=1, column=0, pady=5, padx=5, sticky="e")
entry_emp_name = tk.Entry(root, **entry_style)
entry_emp_name.grid(row=1, column=1, pady=5, padx=5)

tk.Label(root, text="Salary", **label_style).grid(row=2, column=0, pady=5, padx=5, sticky="e")
entry_salary = tk.Entry(root, **entry_style)
entry_salary.grid(row=2, column=1, pady=5, padx=5)

tk.Label(root, text="Designation", **label_style).grid(row=3, column=0, pady=5, padx=5, sticky="e")
entry_desig = tk.Entry(root, **entry_style)
entry_desig.grid(row=3, column=1, pady=5, padx=5)

# Button styling
button_style = {"bg": "#4CAF50", "fg": "white", "font": ("Arial", 12), "width": 12, "height": 1}

insert_button = tk.Button(root, text="Insert Data", command=insert_data, **button_style)
insert_button.grid(row=4, column=0, pady=10, padx=10)

retrieve_button = tk.Button(root, text="Retrieve Data", command=retrieve_data, **button_style)
retrieve_button.grid(row=4, column=1, pady=10, padx=10)

root.mainloop()