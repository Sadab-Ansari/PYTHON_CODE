import mysql.connector
from tkinter import *

def connect_db():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",  
        password="", 
        database="company",
    )
    return conn

def fetch_employee_by_name():
    name = e_name.get().strip()  
    if not name:
        l_message.config(text="Please enter an employee name!", fg="red")
        return

    conn = connect_db()
    if conn is None:
        return 

    cursor = conn.cursor()
    
    sql = "SELECT * FROM employees WHERE name = %s"
    cursor.execute(sql, (name,))
    employee = cursor.fetchone()
    
    if employee:
        e_position.delete(0, END)
        e_position.insert(0, employee[2])
        e_salary.delete(0, END)
        e_salary.insert(0, employee[3])
        l_message.config(text="Employee found!", fg="green")
    else:
        e_position.delete(0, END)
        e_salary.delete(0, END)
        l_message.config(text="Employee not found.", fg="red")

    cursor.close()
    conn.close()

root = Tk()
root.geometry("600x800+150+150")
root.title("Employee Management System")

l1 = Label(root, text="Employee Name:", font=('Arial', 12))
l1.place(x=50, y=100)
e_name = Entry(root, font=('Arial', 12))
e_name.place(x=250, y=100)

l2 = Label(root, text="Position:", font=('Arial', 12))
l2.place(x=50, y=150)
e_position = Entry(root, font=('Arial', 12))
e_position.place(x=250, y=150)

l3 = Label(root, text="Salary:", font=('Arial', 12))
l3.place(x=50, y=200)
e_salary = Entry(root, font=('Arial', 12))
e_salary.place(x=250, y=200)

b2 = Button(root, text="Fetch Employee", font=('Arial', 12), command=fetch_employee_by_name)
b2.place(x=250, y=250)

l_message = Label(root, text="", font=('Arial', 12))
l_message.place(x=50, y=300)

b3 = Button(root, text="Exit", font=('Arial', 12), command=root.destroy)
b3.place(x=250, y=400)

root.mainloop()