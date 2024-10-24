import mysql.connector
from mysql.connector import MySQLConnection, Error
import tkinter as tk
from tkinter import *
from tkinter import ttk
conn = mysql.connector.connect(host="localhost",database="student",user="root",password="1234")

def stu_records():
    def insert_data():
        top=Tk()
        def reset_button():
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)
            E5.delete(0, END)
            E6.delete(0, END)

        def submit_button():
            query = f"insert into stu_records(adm_no,name,age,class,dad_name,mom_name) values ('{E1.get()}', '{E2.get()}', '{E3.get()}', '{E4.get()}', '{E5.get()}', '{E6.get()}')"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record entered successfully")
                
        b1 = Button(top,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(top, text = "Submit",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=6, column=0, pady=2)
        b2.grid(row=7, column=0, pady=2)

        L1 = Label(top, text="Admission Number")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        L2 = Label(top, text="Student Name")
        L2.grid(row=1, column=0, sticky=W, pady=2)

        L3 = Label(top, text="Student Age")
        L3.grid(row=2, column=0, sticky=W, pady=2)

        L4 = Label(top, text="Class")
        L4.grid(row=3, column=0, sticky=W, pady=2)

        L5 = Label(top, text="Father's Name")
        L5.grid(row=4, column=0, sticky=W, pady=2)

        L6 = Label(top, text="Mother's Name")
        L6.grid(row=5, column=0, sticky=W, pady=2)

        E1 = Entry(top)
        E1.grid(row=0, column=1, pady=2)

        E2 = Entry(top)
        E2.grid(row=1, column=1, pady=2)

        E3 = Entry(top)
        E3.grid(row=2, column=1, pady=2)

        E4 = Entry(top)
        E4.grid(row=3, column=1, pady=2)

        E5 = Entry(top)
        E5.grid(row=4, column=1, pady=2)

        E6 = Entry(top)
        E6.grid(row=5, column=1, pady=2)

        top.mainloop()

    def update_data():
        def updatename():
            win=Tk()
            
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_records SET name = '{E1.get()}' WHERE adm_no = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(win,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(win, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(win, text="Enter Student name")
            L1.grid(row=0, column=0, sticky=W, pady=2)

            L2 = Label(win, text="Enter the existing admission number")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            E1 = Entry(win)
            E1.grid(row=0, column=1, pady=2)

            E2 = Entry(win)
            E2.grid(row=1, column=1, pady=2)

            win.mainloop()

        def updateage():
            we=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_records SET age = '{E2.get()}' WHERE adm_no = '{E1.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(we,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(we, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(we, text="Enter existing admission number of student")
            L1.grid(row=0, column=0, sticky=W, pady=2)

            L2 = Label(we, text="New age of student")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            E1 = Entry(we)
            E1.grid(row=0, column=1, pady=2)

            E2 = Entry(we)
            E2.grid(row=1, column=1, pady=2)

            we.mainloop()

        def updateclass():
            wen=Tk()
            def reset_button():
                E2.delete(0, END)
                E3.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_records SET class = '{E3.get()}' WHERE adm_no = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wen,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wen, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L2 = Label(wen, text="Enter existing admission number of student")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            L3 = Label(wen, text="Enter updated class of student")
            L3.grid(row=2, column=0, sticky=W, pady=2)

            E2 = Entry(wen)
            E2.grid(row=1, column=1, pady=2)

            E3 = Entry(wen)
            E3.grid(row=2, column=1, pady=2)

            wen.mainloop()

        def updatefname():
            wenf=Tk()
            def reset_button():
                E2.delete(0, END)
                E3.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_records SET dad_name = '{E3.get()}' WHERE adm_no = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wenf,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wenf, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L2 = Label(wenf, text="Enter existing admission number of student")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            L3 = Label(wenf, text="Enter updated father name of student")
            L3.grid(row=2, column=0, sticky=W, pady=2)

            E2 = Entry(wenf)
            E2.grid(row=1, column=1, pady=2)

            E3 = Entry(wenf)
            E3.grid(row=2, column=1, pady=2)

            wenf.mainloop()


        def updatemname():
            wenm=Tk()
            def reset_button():
                E2.delete(0, END)
                E3.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_records SET mom_name = '{E3.get()}' WHERE adm_no = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wenm,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wenm, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L2 = Label(wenm, text="Enter existing admission number of student")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            L3 = Label(wenm, text="Enter updated mother name of student")
            L3.grid(row=2, column=0, sticky=W, pady=2)

            E2 = Entry(wenm)
            E2.grid(row=1, column=1, pady=2)

            E3 = Entry(wenm)
            E3.grid(row=2, column=1, pady=2)

            wenm.mainloop()

        root = Tk()

        update_name_button = Button(root, text="Update Name", command=updatename)
        update_age_button = Button(root, text="Update Age", command=updateage)
        update_class_button = Button(root, text="Update Class", command=updateclass)
        update_fname_button = Button(root, text="Update Father's name", command=updatefname)
        update_mname_button = Button(root, text="Update Mother's Name", command=updatemname)

        update_name_button.grid(row=3, column=0)
        update_age_button.grid(row=3, column=1)
        update_class_button.grid(row=3, column=2)
        update_fname_button.grid(row=3, column=3)
        update_mname_button.grid(row=3, column=4)

        root.title("Update Student Data")
        root.geometry("400x200")

        root.mainloop()

    def delete_data():
        de = Tk()
        def reset_button():
            E1.delete(0, END)

        def submit_button():
            query = f"DELETE FROM stu_records WHERE adm_no = '{E1.get()}'"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record deleted successfully")

        b1 = Button(de,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(de, text = "Delete",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=3, column=0, pady=2)
        b2.grid(row=4, column=0, pady=2)

        L1 = Label(de, text="Enter admission number of student you want to delete")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        E1 = Entry(de)
        E1.grid(row=0, column=1, pady=2)

        de.mainloop()

    def find_data():
        rootf = tk.Tk()
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

        rootf.mainloop()

    def exit_program():
        full.quit()

    full = Tk()

    insert_button = Button(full, text="Insert Data", command=insert_data)
    update_button = Button(full, text="Update Data", command=update_data)
    delete_button = Button(full, text="Delete Data", command=delete_data)
    find_button = Button(full, text="Find Data", command=find_data)
    exit_button = Button(full, text="Exit Program", command=exit_program)

    insert_button.grid(row=0, column=0)
    update_button.grid(row=0, column=1)
    delete_button.grid(row=0, column=2)
    find_button.grid(row=0, column=3)
    exit_button.grid(row=0, column=4)

    full.title("Student Record Management System")
    full.geometry("300x100")

    full.mainloop()

def stu_fees():
    def insert_data():
        top=Tk()
        def reset_button():
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)

        def submit_button():
            query = f"insert into stu_fees(receipt_no,month,amount,adm_no) values ('{E1.get()}', '{E2.get()}', '{E3.get()}', '{E4.get()}')"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record entered successfully")
                
        b1 = Button(top,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(top, text = "Submit",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=6, column=0, pady=2)
        b2.grid(row=7, column=0, pady=2)

        L1 = Label(top, text="Receipt number")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        L2 = Label(top, text="Month of deposit")
        L2.grid(row=1, column=0, sticky=W, pady=2)

        L3 = Label(top, text="Amount of deposit")
        L3.grid(row=2, column=0, sticky=W, pady=2)

        L4 = Label(top, text="Student admission number")
        L4.grid(row=3, column=0, sticky=W, pady=2)

        E1 = Entry(top)
        E1.grid(row=0, column=1, pady=2)

        E2 = Entry(top)
        E2.grid(row=1, column=1, pady=2)

        E3 = Entry(top)
        E3.grid(row=2, column=1, pady=2)

        E4 = Entry(top)
        E4.grid(row=3, column=1, pady=2)

        top.mainloop()

    def update_data():
        def updatemonth():
            win=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_fees SET month = '{E1.get()}' WHERE receipt_no = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(win,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(win, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(win, text="Updated Month")
            L1.grid(row=0, column=0, sticky=W, pady=2)

            L2 = Label(win, text="Enter existing receipt number")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            E1 = Entry(win)
            E1.grid(row=0, column=1, pady=2)

            E2 = Entry(win)
            E2.grid(row=1, column=1, pady=2)

            win.mainloop()

        def updateamount():
            we=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_fees SET amount = '{E2.get()}' WHERE receipt_no = '{E1.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(we,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(we, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(we, text="Enter updated amount")
            L1.grid(row=0, column=0, sticky=W, pady=2)

            L2 = Label(we, text="Enter exisitng receipt_no")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            E1 = Entry(we)
            E1.grid(row=0, column=1, pady=2)

            E2 = Entry(we)
            E2.grid(row=1, column=1, pady=2)

            we.mainloop()

        def updateadmno():
            wen=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_fees SET adm_no = '{E1.get()}' WHERE receipt_no = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wen,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wen, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(wen, text="Enter updated admission number (should exist in records)")
            L1.grid(row=1, column=0, sticky=W, pady=2)

            L2 = Label(wen, text="Enter exisitng receipt number")
            L2.grid(row=2, column=0, sticky=W, pady=2)

            E1 = Entry(wen)
            E1.grid(row=1, column=1, pady=2)

            E2 = Entry(wen)
            E2.grid(row=2, column=1, pady=2)

            wen.mainloop()
        root = Tk()

        update_title_button = Button(root, text="Update Month", command=updatemonth)
        update_author_button = Button(root, text="Update Amount", command=updateamount)
        update_price_button = Button(root, text="Update Admission Number", command=updateadmno)

        update_title_button.grid(row=3, column=0)
        update_author_button.grid(row=3, column=1)
        update_price_button.grid(row=3, column=2)

        root.title("Book Inventory Management")
        root.geometry("400x200")

        root.mainloop()

    def delete_data():
        de = Tk()
        def reset_button():
            E1.delete(0, END)

        def submit_button():
            query = f"DELETE FROM stu_fees WHERE receipt_no = '{E1.get()}'"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record deleted successfully")

        b1 = Button(de,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(de, text = "Delete",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=3, column=0, pady=2)
        b2.grid(row=4, column=0, pady=2)

        L1 = Label(de, text="Enter receipt number you want to delete")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        E1 = Entry(de)
        E1.grid(row=0, column=1, pady=2)

        de.mainloop()
        
    def find_data():
        rootg = tk.Tk()
        log = tk.Toplevel(rootg)
        log.transient(rootg)
        log.title('View all students')

        columns = ('Receipt Number','Month','Amount','Admission Number')
        tree = ttk.Treeview(log, height=20, columns=columns, show='headings')
        tree.grid(row=0, column=0, sticky='news')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        def reset_button():
                E1.delete(0, END)

        def submit_button():
            query = f"SELECT * FROM stu_fees where adm_no = '{E1.get()}'"
            c = conn.cursor()
            c.execute(query)

            for rec in c:
                tree.insert('', 'end', value=rec)

        b1 = Button(rootg,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(rootg, text = "Find",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=3, column=0, pady=2)
        b2.grid(row=4, column=0, pady=2)

        L1 = Label(rootg, text="Enter admission number of student you want to find")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        E1 = Entry(rootg)
        E1.grid(row=0, column=1, pady=2)

        sb = tk.Scrollbar(log, orient=tk.VERTICAL, command=tree.yview)
        sb.grid(row=0, column=1, sticky='ns')
        tree.config(yscrollcommand=sb.set)

        rootg.mainloop()

    def exit_program():
        full.quit()

    full = Tk()

    insert_button = Button(full, text="Insert Data", command=insert_data)
    update_button = Button(full, text="Update Data", command=update_data)
    delete_button = Button(full, text="Delete Data", command=delete_data)
    find_button = Button(full, text="Find Data", command=find_data)
    exit_button = Button(full, text="Exit Program", command=exit_program)

    insert_button.grid(row=0, column=0)
    update_button.grid(row=0, column=1)
    delete_button.grid(row=0, column=2)
    find_button.grid(row=0, column=3)
    exit_button.grid(row=0, column=4)

    full.title("Student Fees Management System")
    full.geometry("300x100")

    full.mainloop()


def stu_marks():
    def insert_data():
        top=Tk()
        def reset_button():
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)
            E5.delete(0, END)
            E6.delete(0, END)
            E7.delete(0, END)
            E8.delete(0, END)

        def submit_button():
            total = m1.get() + m2.get() + m3.get() + m4.get() + m5.get()
            perc=total/5
            if perc>=90:
                grade = 'A'
            elif perc>=80:
                grade = 'B'
            elif perc>=70:
                grade = 'C'
            elif perc>=60:
                grade = 'D'
            elif perc>=50:
                grade = 'E'
            else:
                grade = 'F'
            query = f"insert into stu_marks1(pid,semester,roll_no,english,maths,science,hindi,ict,total,percentage,grade,adm_no) values ('{E1.get()}', '{E2.get()}', '{E3.get()}', '{E4.get()}', '{E5.get()}', '{E6.get()}', '{E7.get()}', '{total}', '{perc}', '{grade}', '{E8.get()}')"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record entered successfully")
                
        b1 = Button(top,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(top, text = "Submit",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=9, column=0, pady=2)
        b2.grid(row=10, column=0, pady=2)

        L1 = Label(top, text="ID of student marks")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        L2 = Label(top, text="Semester of student")
        L2.grid(row=1, column=0, sticky=W, pady=2)

        L3 = Label(top, text="Roll number of student")
        L3.grid(row=2, column=0, sticky=W, pady=2)

        L4 = Label(top, text="Marks in English")
        L4.grid(row=3, column=0, sticky=W, pady=2)

        L5 = Label(top, text="Marks in Mathematics")
        L5.grid(row=4, column=0, sticky=W, pady=2)

        L6 = Label(top, text="Marks in Science")
        L6.grid(row=5, column=0, sticky=W, pady=2)

        L7 = Label(top, text="Marks in Hindi")
        L7.grid(row=6, column=0, sticky=W, pady=2)

        L8 = Label(top, text="Marks in Computer Science")
        L8.grid(row=7, column=0, sticky=W, pady=2)

        L9 = Label(top, text="Admission Number of student")
        L9.grid(row=8, column=0, sticky=W, pady=2)

        m1=IntVar()
        m2=IntVar()
        m3=IntVar()
        m4=IntVar()
        m5=IntVar()

        E1 = Entry(top)
        E1.grid(row=0, column=1, pady=2)

        E2 = Entry(top)
        E2.grid(row=1, column=1, pady=2)

        E3 = Entry(top, textvariable=m1)
        E3.grid(row=2, column=1, pady=2)

        E4 = Entry(top, textvariable=m2)
        E4.grid(row=3, column=1, pady=2)

        E5 = Entry(top, textvariable=m3)
        E5.grid(row=4, column=1, pady=2)

        E6 = Entry(top, textvariable=m4)
        E6.grid(row=5, column=1, pady=2)

        E7 = Entry(top, textvariable=m5)
        E7.grid(row=6, column=1, pady=2)

        E8 = Entry(top)
        E8.grid(row=7, column=1, pady=2)

        E9 = Entry(top)
        E9.grid(row=8, column=1, pady=2)

        top.mainloop()

    def update_data():
        def updatesem():
            wik=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_marks1 SET semester = '{E1.get()}' WHERE pid = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wik,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wik, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(wik, text="Updated Semester")
            L1.grid(row=0, column=0, sticky=W, pady=2)

            L2 = Label(wik, text="Existing PID")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            E1 = Entry(wik)
            E1.grid(row=0, column=1, pady=2)

            E2 = Entry(wik)
            E2.grid(row=1, column=1, pady=2)

            wik.mainloop()

        def updaterollno():
            win=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_marks1 SET roll_no = '{E1.get()}' WHERE pid = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(win,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(win, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(win, text="Updated Roll number")
            L1.grid(row=0, column=0, sticky=W, pady=2)

            L2 = Label(win, text="Existing PID")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            E1 = Entry(win)
            E1.grid(row=0, column=1, pady=2)

            E2 = Entry(win)
            E2.grid(row=1, column=1, pady=2)

            win.mainloop()

        def updateeng():
            we=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_marks1 SET english = '{E1.get()}' WHERE pid = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(we,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(we, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(we, text="Updated marks of english")
            L1.grid(row=0, column=0, sticky=W, pady=2)

            L2 = Label(we, text="Existing PID")
            L2.grid(row=1, column=0, sticky=W, pady=2)

            E1 = Entry(we)
            E1.grid(row=0, column=1, pady=2)

            E2 = Entry(we)
            E2.grid(row=1, column=1, pady=2)

            we.mainloop()

        def updatemaths():
            wen=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_marks1 SET maths = '{E1.get()}' WHERE PID = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wen,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wen, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(wen, text="Updated marks in Mathematics")
            L1.grid(row=1, column=0, sticky=W, pady=2)

            L2 = Label(wen, text="Existing PID")
            L2.grid(row=2, column=0, sticky=W, pady=2)

            E1 = Entry(wen)
            E1.grid(row=1, column=1, pady=2)

            E2 = Entry(wen)
            E2.grid(row=2, column=1, pady=2)

            wen.mainloop()

        def updatesci():
            weh=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_marks1 SET science = '{E1.get()}' WHERE PID = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(weh,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(weh, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(weh, text="Updated marks in Science")
            L1.grid(row=1, column=0, sticky=W, pady=2)

            L2 = Label(weh, text="Existing PID")
            L2.grid(row=2, column=0, sticky=W, pady=2)

            E1 = Entry(weh)
            E1.grid(row=1, column=1, pady=2)

            E2 = Entry(weh)
            E2.grid(row=2, column=1, pady=2)

            weh.mainloop()

        def updatehindi():
            wenw=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_marks1 SET hindi = '{E1.get()}' WHERE PID = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wenw,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wenw, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(wenw, text="Updated marks in Hindi")
            L1.grid(row=1, column=0, sticky=W, pady=2)

            L2 = Label(wenw, text="Existing PID")
            L2.grid(row=2, column=0, sticky=W, pady=2)

            E1 = Entry(wenw)
            E1.grid(row=1, column=1, pady=2)

            E2 = Entry(wenw)
            E2.grid(row=2, column=1, pady=2)

            wenw.mainloop()
        
        def updatecs():
            wenwc=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_marks1 SET ict = '{E1.get()}' WHERE PID = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wenwc,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wenwc, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(wenwc, text="Updated marks in Computers")
            L1.grid(row=1, column=0, sticky=W, pady=2)

            L2 = Label(wenwc, text="Existing PID")
            L2.grid(row=2, column=0, sticky=W, pady=2)

            E1 = Entry(wenwc)
            E1.grid(row=1, column=1, pady=2)

            E2 = Entry(wenwc)
            E2.grid(row=2, column=1, pady=2)

            wenwc.mainloop()

        def updateadmno():
            wenwa=Tk()
            def reset_button():
                E1.delete(0, END)
                E2.delete(0, END)

            def submit_button():
                query = f"UPDATE stu_marks1 SET adm_no = '{E1.get()}' WHERE PID = '{E2.get()}'"
                cursor=conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Record updated successfully")

            b1 = Button(wenwa,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
            b2 = Button(wenwa, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

            b1.grid(row=3, column=0, pady=2)
            b2.grid(row=4, column=0, pady=2)

            L1 = Label(wenwa, text="Updated Admission number")
            L1.grid(row=1, column=0, sticky=W, pady=2)

            L2 = Label(wenwa, text="Existing PID")
            L2.grid(row=2, column=0, sticky=W, pady=2)

            E1 = Entry(wenwa)
            E1.grid(row=1, column=1, pady=2)

            E2 = Entry(wenwa)
            E2.grid(row=2, column=1, pady=2)

            wenwa.mainloop()
        
        root = Tk()

        update_sem_button = Button(root, text="Update Semester", command=updatesem)
        update_rollno_button = Button(root, text="Update Roll number", command=updaterollno)
        update_eng_button = Button(root, text="Update marks of English", command=updateeng)
        update_maths_button = Button(root, text="Update marks of Maths", command=updatemaths)
        update_sci_button = Button(root, text="Update marks of Science", command=updatesci)
        update_hindi_button = Button(root, text="Update marks of Hindi", command=updatehindi)
        update_cs_button = Button(root, text="Update marks of Computers", command=updatecs)
        update_admno_button = Button(root, text="Update Admission number", command=updateadmno)

        update_sem_button.grid(row=3, column=0)
        update_rollno_button.grid(row=3, column=1)
        update_eng_button.grid(row=3, column=2)
        update_maths_button.grid(row=3, column=3)
        update_sci_button.grid(row=3, column=4)
        update_hindi_button.grid(row=3, column=5)
        update_cs_button.grid(row=3, column=6)
        update_admno_button.grid(row=3, column=7)

        root.title("Marks updation system")
        root.geometry("400x200")

        root.mainloop()

    def delete_data():
        de = Tk()
        def reset_button():
            E1.delete(0, END)

        def submit_button():
            query = f"DELETE FROM stu_marks1 WHERE pid = '{E1.get()}'"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record deleted successfully")

        b1 = Button(de,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(de, text = "Delete",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=3, column=0, pady=2)
        b2.grid(row=4, column=0, pady=2)

        L1 = Label(de, text="Enter pid of record you want to delete")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        E1 = Entry(de)
        E1.grid(row=0, column=1, pady=2)

        de.mainloop()

    def find_data():
        rooth = tk.Tk()
        log = tk.Toplevel(rooth)
        log.transient(rooth)
        log.title('View all students')

        columns = ('Pid','Semester','Roll Number','English','Mathematics','Science','Hindi','Computers','Total','Percentage','Grade','Admission Number')
        tree = ttk.Treeview(log, height=20, columns=columns, show='headings')
        tree.grid(row=0, column=0, sticky='news')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        def reset_button():
                E1.delete(0, END)

        def submit_button():
            query = f"SELECT * FROM stu_marks1 where adm_no = '{E1.get()}'"
            c = conn.cursor()
            c.execute(query)

            for rec in c:
                tree.insert('', 'end', value=rec)

        b1 = Button(rooth,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(rooth, text = "Find",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=3, column=0, pady=2)
        b2.grid(row=4, column=0, pady=2)

        L1 = Label(rooth, text="Enter admission number of student you want to find")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        E1 = Entry(rooth)
        E1.grid(row=0, column=1, pady=2)

        sb = tk.Scrollbar(log, orient=tk.VERTICAL, command=tree.yview)
        sb.grid(row=0, column=1, sticky='ns')
        tree.config(yscrollcommand=sb.set)

        rooth.mainloop()

    def exit_program():
        full.quit()

    full = Tk()

    insert_button = Button(full, text="Insert Data", command=insert_data)
    update_button = Button(full, text="Update Data", command=update_data)
    delete_button = Button(full, text="Delete Data", command=delete_data)
    find_button = Button(full, text="Find Data", command=find_data)
    exit_button = Button(full, text="Exit Program", command=exit_program)

    insert_button.grid(row=0, column=0)
    update_button.grid(row=0, column=1)
    delete_button.grid(row=0, column=2)
    find_button.grid(row=0, column=3)
    exit_button.grid(row=0, column=4)

    full.title("Student Marks Management")
    full.geometry("300x100")

    full.mainloop()

why = Tk()

update_rollno_button = Button(why, text="Deal with Records", command=stu_records)
update_eng_button = Button(why, text="Deal with Fees", command=stu_fees)
update_maths_button = Button(why, text="Deal with Marks", command=stu_marks)

update_rollno_button.grid(row=3, column=0)
update_eng_button.grid(row=3, column=1)
update_maths_button.grid(row=3, column=2)
why.title("All in one dealing system")
why.geometry("400x200")

why.mainloop()