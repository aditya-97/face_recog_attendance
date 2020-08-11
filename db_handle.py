import sqlite3
from tkinter import *
from tkinter import messagebox
import csv
import os
import time

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.cur = self.conn.cursor()
        #self.cur.execute(
        #   "CREATE TABLE Lecture1 ( 'Name' TEXT NOT NULL, 'Roll_No' INTEGER, '1' TEXT, '2' TEXT, '3' TEXT, '4' TEXT, '5' TEXT, '6' TEXT, '7' TEXT, '8' TEXT, '9' TEXT, '10' TEXT, '11' TEXT, '12' TEXT, '13' TEXT, '14' TEXT, '15' TEXT, '16' TEXT, '17' TEXT, '18' TEXT, '19' TEXT, '20' TEXT, '21' TEXT, '22' TEXT, '23' TEXT, '24' TEXT, '25' TEXT, '26' TEXT, '27' TEXT, '28' TEXT, '29' TEXT, '30' TEXT, '31' TEXT "))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT Id,Name,Roll_No FROM lecture1")
        rows = self.cur.fetchall()
        return rows

    #def insert(self, title, author, isbn):
    #    self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?)", (title, author, isbn))
    #    self.conn.commit()
    #    self.view()

    #def update(self, id, title, author, isbn):
    #    self.cur.execute("UPDATE book SET title=?, author=?, isbn=? WHERE id=?", (title, author, isbn, id))
    #    self.view()

    def delete(self, id):
        self.cur.execute("DELETE FROM lecture1 WHERE id=?", (id,))
        self.conn.commit()
        self.view()

    def search(self, name="", roll=""):
        self.cur.execute("SELECT Name,Roll_No FROM lecture1 WHERE Name=? OR Roll_No=?", (name, roll))
        rows = self.cur.fetchall()
        return rows


db = DB()

def delet():
  
    def get_selected_row(event):
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
    #e3.delete(0, END)
    #e3.insert(END, selected_tuple[3])


    def view_command():
        list1.delete(0, END)
        for row in db.view():
            list1.insert(END, row)


    def search_command():
        list1.delete(0, END)
        print(e1.get())
        for row in db.search(e1.get(), e2.get()):
            list1.insert(END, row)


#def add_command():
    #db.insert(title_text.get(), author_text.get(), isbn_text.get())
    #list1.delete(0, END)
    #list1.insert(END, (title_text.get(), author_text.get(), isbn_text.get()))


    def delete_command():
        print(selected_tuple[2])
        num = db.delete(selected_tuple[0])
        for i in range(1,42):
            os.remove('./dataset/User.'+str(selected_tuple[2])+'.'+str(i)+'.jpg')


#def update_command():
   # db.update(selected_tuple[0], title_text.get(), author_text.get(), isbn_text.get())


    window = Tk()

    window.title("Students")


    def on_closing():
        dd = db
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
            del dd


    window.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing

    l1 = Label(window, text="Name")
    l1.grid(row=0, column=0)

    l2 = Label(window, text="Roll No")
    l2.grid(row=0, column=2)

#l3 = Label(window, text="ISBN")
#l3.grid(row=1, column=0)

    title_text = StringVar()
    e1 = Entry(window, textvariable=title_text)
    e1.grid(row=0, column=1)

    author_text = StringVar()
    e2 = Entry(window, textvariable=author_text)
    e2.grid(row=0, column=3)

#isbn_text = StringVar()
#e3 = Entry(window, textvariable=isbn_text)
#e3.grid(row=1, column=1)

    list1 = Listbox(window, height=6, width=35)
    list1.grid(row=2, column=0, rowspan=6, columnspan=2)

    sb1 = Scrollbar(window)
    sb1.grid(row=2, column=2, rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>', get_selected_row)

    b1 = Button(window, text="View all", width=12, command=view_command)
    b1.grid(row=2, column=3)

    b2 = Button(window, text="Search entry", width=12, command=search_command)
    b2.grid(row=3, column=3)

#b3 = Button(window, text="Add entry", width=12, command=add_command)
#b3.grid(row=4, column=3)

#b4 = Button(window, text="Update selected", width=12, command=update_command)
#b4.grid(row=5, column=3)

    b5 = Button(window, text="Delete selected", width=12, command=delete_command)
    b5.grid(row=6, column=3)

    b6 = Button(window, text="Close", width=12, command=window.destroy)
    b6.grid(row=7, column=3)

    window.mainloop()

def get_data():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    data = c.execute('SELECT * FROM lecture1')

    with open('Attendance.csv','wb') as f:
        w = csv.writer(f)
        w.writerow(['Id','Name','Roll No','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'])
        w.writerows(data)
        conn.close()
    messagebox.showinfo("Success", "CSV file stored!")