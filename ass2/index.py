from tkinter import *

root = Tk()
root.geometry("500x500+150+150")
root.title("Semester IV Result Calculator")

# Labels and Entries
l1 = Label(root, font=('arial', 12, 'bold'), text="maths ", fg="black")
l1.place(x=50, y=50)
e1 = Entry(root, font=("arial", 12, 'bold'), fg="black")
e1.place(x=300, y=50)

l2 = Label(root, font=('arial', 12, 'bold'), text="oops with java", fg="black")
l2.place(x=50, y=100)
e2 = Entry(root, font=("arial", 12, 'bold'), fg="black")
e2.place(x=300, y=100)

l3 = Label(root, font=('arial', 12, 'bold'), text="Digital Electronics", fg="black")
l3.place(x=50, y=150)
e3 = Entry(root, font=("arial", 12, 'bold'), fg="black")
e3.place(x=300, y=150)

l4 = Label(root, font=('arial', 12, 'bold'), text="DAA ", fg="black")
l4.place(x=50, y=200)
e4 = Entry(root, font=("arial", 12, 'bold'), fg="black")
e4.place(x=300, y=200)

l5 = Label(root, font=('arial', 12, 'bold'), text="Law", fg="black")
l5.place(x=50, y=250)
e5 = Entry(root, font=("arial", 12, 'bold'), fg="black")
e5.place(x=300, y=250)

l6 = Label(root, font=('arial', 12, 'bold'), text="Disaster Management", fg="black")
l6.place(x=50, y=300)
e6 = Entry(root, font=("arial", 12, 'bold'), fg="black")
e6.place(x=300, y=300)

l7 = Label(root, font=('arial', 12, 'bold'), text="Enterpreneurship", fg="black")
l7.place(x=50, y=350)
e7 = Entry(root, font=("arial", 12, 'bold'), fg="black")
e7.place(x=300, y=350)

rl = Label(root, font=('arial', 12, 'bold'), text="", fg="black")
rl.place(x=80, y=400)

# Function to calculate total marks, percentage, and grade
def calculate():
    try:
        # Fetch marks from entry widgets
        marks = [
            int(e1.get()), int(e2.get()), int(e3.get()), 
            int(e4.get()), int(e5.get()), int(e6.get()), int(e7.get())
        ]
        total_marks = sum(marks)
        percentage = (total_marks / 700) * 100

        # Determine grade
        if percentage >= 95:
            grade = "O"
        elif percentage >= 85:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 65:
            grade = "B+"
        elif percentage >= 45:
            grade = "B"
        elif percentage >= 35:
            grade = "C+"
        elif percentage >= 25:
            grade = "C"
        else:
            grade = "F"

        # Display result
        rl.config(
            text=f"Total: {total_marks}, Percentage: {percentage:.2f}%, Grade: {grade}"
        )
    except ValueError:
        rl.config(text="Please enter valid numeric marks!")

# Buttons
b1 = Button(root, font=('arial', 12, 'bold'), text="Calculate", fg="red", command=calculate)
b1.place(x=100, y=450)

b2 = Button(root, font=('arial', 12, 'bold'), text="Exit", fg="red", command=root.destroy)
b2.place(x=300, y=450)

root.mainloop()