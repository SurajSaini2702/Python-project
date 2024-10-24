import mysql.connector
conn=mysql.connector.connect(host='localhost',database='student',user='root',password='1234')
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import *

rootf = tk.Tk()

def logs():
    log = tk.Toplevel(rootf)
    log.transient(rootf)
    log.title('View all students')

    columns = ('Admission Number','Name','Age','Class','Father Name','Mother Name')
    tree = ttk.Treeview(log, height=20, columns=columns, show='headings')
    tree.grid(row=0, column=0, sticky='news')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)

    def reset_button():
            E1.delete(0, END)
    
    def submit_button():
        query = f"SELECT * FROM stu_records where adm_no = '{E1.get()}'"
        c = conn.cursor()
        c.execute(query)

        for rec in c:
            tree.insert('', 'end', value=rec)

    b1 = Button(rootf,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
    b2 = Button(rootf, text = "Find",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

    b1.grid(row=3, column=0, pady=2)
    b2.grid(row=4, column=0, pady=2)

    L1 = Label(rootf, text="Enter admission number of student you want to find")
    L1.grid(row=0, column=0, sticky=W, pady=2)

    E1 = Entry(rootf)
    E1.grid(row=0, column=1, pady=2)

    sb = tk.Scrollbar(log, orient=tk.VERTICAL, command=tree.yview)
    sb.grid(row=0, column=1, sticky='ns')
    tree.config(yscrollcommand=sb.set)

    btn = tk.Button(log, text='Exit', command=log.destroy, width=20, bd=2, fg='#eb4d4b')
    btn.grid(row=1, column=0, columnspan=2)

    rootf.mainloop()

logs()