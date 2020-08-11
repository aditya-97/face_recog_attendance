from Tkinter import *
import time
import tkMessageBox
import a_panel
time1 = ''
from recog import get_user
import sqlite3

def main():
    root = Tk()
    root.geometry('1000x400')
    #root.resizable(False, False)
    frm1 = Frame(root, bg='green')
    frm1.pack(fill=BOTH)
    clock = Label(frm1, font=('times', 20, 'bold'), bg='green')
    clock.pack(fill=BOTH, pady=20)
    cal = Label(frm1, font=('times', 20, 'bold'), bg='green')
    cal.pack(fill=BOTH, pady=20)
    frm2 = Frame(root, bg='blue')
    frm2.pack(fill=BOTH, expand=1)
    def capture():
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        date = time.strftime('%d')
        uname = get_user()
        text = "UPDATE Lecture1 SET '%s'='P' WHERE Name='%s'"%(date,uname)
        if (uname=='No Match'):
            tkMessageBox.showerror("Error", "Not recognized,Please try again")
        else:
            result = tkMessageBox.askyesno("Alert"," "+uname+"Would you like to place attendence?")
            if result==True:
                c.execute(text)
                conn.commit()
                user.config(text=uname+', your attendence placed')
                conn.close()

    cap = Button(frm2, font=('times', 20, 'bold'), text='Capture', bg='black', fg='yellow', bd=5,command = capture)
    cap.pack(padx=50, pady=20, side='left')
   
    def login():
        new = Toplevel(root)
        new.geometry('500x200')
        new.config(bg='green')
        new.resizable(False, False)
        frm1 = Frame(new, bg='green')
        frm1.pack(fill=BOTH, expand=1)
        frm2 = Frame(new, bg='green')
        frm2.pack(fill=BOTH, expand=1)
        name = Label(frm1, font=('times', 20, 'bold'), bg='green', text='Username')
        name.pack(side='left', padx=20)
        name_en = Entry(frm1, font=('times', 20, 'bold'), fg='black', bg='grey')
        name_en.pack(side='right', padx=20)
        pwd = Label(frm2, font=('times', 20, 'bold'), bg='green', text='Password')
        pwd.pack(side='left', padx=20)
        pwd_en = Entry(frm2, font=('times', 20, 'bold'), fg='black', show='*', bg='grey')
        pwd_en.pack(side='right', padx=20)

        # def admin():

        def sub():
            nm = name_en.get()
            ps = pwd_en.get()
            if (nm != '' and ps != ''):
                if (nm == 'Admin' and ps == 'admin'):
                    root.destroy()
                    a_panel.panel()
                else:
                    tkMessageBox.showwarning("Login Failed", "Error Username or Password")
            else:
                tkMessageBox.showerror("Error", "Please enter Username or Password")

        sub = Button(new, bg='black', fg='yellow', bd=5, font=('times', 20, 'bold'), text="Submit", command=sub)
        sub.pack(anchor='center')
        new.mainloop()

    adm = Button(frm2, font=('times', 20, 'bold'), text='Admin', bg='black', fg='yellow', bd=5, command=login)
    adm.pack(padx=50, pady=20, side='right')
    user = Label(frm2, text="Welcome", font=('times', 20, 'bold'), bg='green')
    user.pack(pady=20,padx=20,side='bottom')
    def tick():
        global time1

        time2 = time.strftime('Time: %H:%M:%S')
        date = time.strftime('Date: %d-%m-%Y')
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
            cal.config(text=date)
        clock.after(200, tick)

    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
