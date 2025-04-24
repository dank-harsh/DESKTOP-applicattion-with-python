import tkinter as tk
import pymysql

def connect_db():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="1234"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    cursor.close()
    db.close()

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="student_db"
    )
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            number VARCHAR(20),
            branch VARCHAR(100)
        )
    """)
    db.commit()
    cursor.close()
    return db

# Add Student Function
def addstud():
    top1 = tk.Toplevel(top)
    top1.geometry("400x400")
    top1.configure(bg="#e6e6e6")

    tk.Label(top1, text="Name", font=("Comic Sans MS", 12, "bold"), bg="#e6e6e6").pack()
    e1 = tk.Entry(top1, font=("Century Gothic", 12))
    e1.pack()

    tk.Label(top1, text="Email", font=("Comic Sans MS", 12, "bold"), bg="#e6e6e6").pack()
    e2 = tk.Entry(top1, font=("Century Gothic", 12))
    e2.pack()

    tk.Label(top1, text="Number", font=("Comic Sans MS", 12, "bold"), bg="#e6e6e6").pack()
    e3 = tk.Entry(top1, font=("Century Gothic", 12))
    e3.pack()

    tk.Label(top1, text="Branch", font=("Comic Sans MS", 12, "bold"), bg="#e6e6e6").pack()
    e4 = tk.Entry(top1, font=("Century Gothic", 12))
    e4.pack()

    def submit_details():
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO students (name, email, number, branch) VALUES (%s, %s, %s, %s)", 
                       (e1.get(), e2.get(), e3.get(), e4.get()))
        db.commit()
        db.close()
        print("Student Added Successfully")

    tk.Button(top1, text="Submit", command=submit_details, font=("Century Gothic", 12, "bold"), bg="#ff4d4d", fg="white").pack(pady=10)

    top1.mainloop()

# View Students Function
def viewstud():
    top2 = tk.Toplevel(top)
    top2.geometry("400x400")
    top2.configure(bg="#e6e6e6")  

    tk.Label(top2, text="Get Student Details", font=("Comic Sans MS", 15, "bold"), bg="#e6e6e6").pack()

    lst = tk.Listbox(top2, height=40, width=40, font=("Century Gothic", 12))
    
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM students")
    students = cursor.fetchall()
    db.close()
    
    for i, student in enumerate(students, start=1):
        lst.insert(i, student[0])
    
    lst.pack()
    top2.mainloop()

# Search Function
def search():
    top3 = tk.Toplevel(top)
    top3.geometry("400x400")
    top3.configure(bg="#e6e6e6")

    tk.Label(top3, text="Search Student", font=("Comic Sans MS", 15, "bold"), bg="#e6e6e6").pack()
    
    search_entry = tk.Entry(top3, font=("Century Gothic", 12))
    search_entry.pack()
    
    result_label = tk.Label(top3, text="", font=("Century Gothic", 12), bg="#e6e6e6")
    result_label.pack()
    
    def perform_search():
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM students WHERE name = %s", (search_entry.get(),))
        student = cursor.fetchone()
        db.close()
        if student:
            result_label.config(text=f"Name: {student[1]}\nEmail: {student[2]}\nNumber: {student[3]}\nBranch: {student[4]}")
        else:
            result_label.config(text="Student not found")
    
    tk.Button(top3, text="Search", command=perform_search, font=("Century Gothic", 12, "bold"), bg="#ff4d4d", fg="white").pack(pady=10)
    
    top3.mainloop()

# Logout Function
def logout():
    top.destroy()

# Main Window
top = tk.Tk()
top.geometry('400x600')
top.configure(bg="#f0f0f0")

L1 = tk.Label(top, text="Student Management System", fg="black", bg="#f0f0f0", font=("Century Gothic", 15, "bold"))
L1.pack(pady=20)

button_style = {
    "width": 20,
    "height": 2,
    "bg": "#ff4d4d",
    "fg": "white",
    "font": ("Century Gothic", 12, "bold"),
    "relief": tk.RAISED,
    "bd": 3
}

tk.Button(top, text="Add Student", command=addstud, **button_style).pack(pady=10)
tk.Button(top, text="View Student", command=viewstud, **button_style).pack(pady=10)
tk.Button(top, text="Search Student", command=search, **button_style).pack(pady=10)
tk.Button(top, text="Log Out", command=logout, **button_style).pack(pady=10)

top.mainloop()
