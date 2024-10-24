import mysql.connector
from mysql.connector import MySQLConnection, Error
from tkinter import *
conn = mysql.connector.connect(host="localhost",database="student",user="root",password="1234")

def insert_data():
    top=Tk()
    def reset_button():
        E1.delete(0, END)
        E2.delete(0, END)
        E3.delete(0, END)

    def submit_button():
        query = f"insert into book(title,author,price) values ('{E1.get()}', '{E2.get()}', '{E3.get()}')"
        cursor=conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Record entered successfully")
            
    b1 = Button(top,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
    b2 = Button(top, text = "Submit",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

    b1.grid(row=3, column=0, pady=2)
    b2.grid(row=4, column=0, pady=2)

    L1 = Label(top, text="Book title")
    L1.grid(row=0, column=0, sticky=W, pady=2)

    L2 = Label(top, text="Book author")
    L2.grid(row=1, column=0, sticky=W, pady=2)

    L3 = Label(top, text="Book price")
    L3.grid(row=2, column=0, sticky=W, pady=2)

    E1 = Entry(top)
    E1.grid(row=0, column=1, pady=2)

    E2 = Entry(top)
    E2.grid(row=1, column=1, pady=2)

    E3 = Entry(top)
    E3.grid(row=2, column=1, pady=2)

    top.mainloop()

def update_data():
    def updatetitle():
        win=Tk()
        def reset_button():
            E1.delete(0, END)
            E2.delete(0, END)

        def submit_button():
            query = f"UPDATE book SET title = '{E1.get()}' WHERE author = '{E2.get()}'"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record updated successfully")

        b1 = Button(win,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(win, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=3, column=0, pady=2)
        b2.grid(row=4, column=0, pady=2)

        L1 = Label(win, text="New Book name")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        L2 = Label(win, text="Book author")
        L2.grid(row=1, column=0, sticky=W, pady=2)

        E1 = Entry(win)
        E1.grid(row=0, column=1, pady=2)

        E2 = Entry(win)
        E2.grid(row=1, column=1, pady=2)

        win.mainloop()

    def updateauthor():
        we=Tk()
        def reset_button():
            E1.delete(0, END)
            E2.delete(0, END)

        def submit_button():
            query = f"UPDATE book SET author = '{E2.get()}' WHERE title = '{E1.get()}'"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record updated successfully")

        b1 = Button(we,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(we, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=3, column=0, pady=2)
        b2.grid(row=4, column=0, pady=2)

        L1 = Label(we, text="Old Book name")
        L1.grid(row=0, column=0, sticky=W, pady=2)

        L2 = Label(we, text="New Book author")
        L2.grid(row=1, column=0, sticky=W, pady=2)

        E1 = Entry(we)
        E1.grid(row=0, column=1, pady=2)

        E2 = Entry(we)
        E2.grid(row=1, column=1, pady=2)

        we.mainloop()

    def updateprice():
        wen=Tk()
        def reset_button():
            E2.delete(0, END)
            E3.delete(0, END)

        def submit_button():
            query = f"UPDATE book SET price = '{E3.get()}' WHERE author = '{E2.get()}'"
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Record updated successfully")

        b1 = Button(wen,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
        b2 = Button(wen, text = "Update",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

        b1.grid(row=3, column=0, pady=2)
        b2.grid(row=4, column=0, pady=2)

        L2 = Label(wen, text="Old Book author")
        L2.grid(row=1, column=0, sticky=W, pady=2)

        L3 = Label(wen, text="New Book price")
        L3.grid(row=2, column=0, sticky=W, pady=2)

        E2 = Entry(wen)
        E2.grid(row=1, column=1, pady=2)

        E3 = Entry(wen)
        E3.grid(row=2, column=1, pady=2)

        wen.mainloop()
    root = Tk()

    update_title_button = Button(root, text="Update Title", command=updatetitle)
    update_author_button = Button(root, text="Update Author", command=updateauthor)
    update_price_button = Button(root, text="Update Price", command=updateprice)

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
        query = f"DELETE FROM book WHERE title = '{E1.get()}'"
        cursor=conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Record deleted successfully")

    b1 = Button(de,text = "Reset",command = reset_button,activeforeground = "red",activebackground = "blue",pady=10)
    b2 = Button(de, text = "Delete",command = submit_button,activeforeground = "red",activebackground = "blue",pady=10)

    b1.grid(row=3, column=0, pady=2)
    b2.grid(row=4, column=0, pady=2)

    L1 = Label(de, text="Enter Book name you want to delete")
    L1.grid(row=0, column=0, sticky=W, pady=2)

    E1 = Entry(de)
    E1.grid(row=0, column=1, pady=2)

    de.mainloop()

def exit_program():
    full.quit()

full = Tk()

insert_button = Button(full, text="Insert Data", command=insert_data)
update_button = Button(full, text="Update Data", command=update_data)
delete_button = Button(full, text="Delete Data", command=delete_data)
exit_button = Button(full, text="Exit Program", command=exit_program)

insert_button.grid(row=0, column=0)
update_button.grid(row=0, column=1)
delete_button.grid(row=0, column=2)
exit_button.grid(row=0, column=3)

full.title("Book Management System")
full.geometry("300x100")

full.mainloop()