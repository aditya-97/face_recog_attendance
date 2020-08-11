
from Tkinter import *
import tkMessageBox
import log_user


def user():
  new = Tk()
  new.geometry('500x200')
  new.config(bg='green')
  new.resizable(False, False)
  frm1 = Frame(new, bg='green')
  frm1.pack(fill=BOTH, expand=1)
  frm2 = Frame(new, bg='green')
  frm2.pack(fill=BOTH, expand=1)
  name = Label(frm1, font=('times', 20, 'bold'), bg='green', text='Name')
  name.pack(side='left', padx=20)
  name_en = Entry(frm1, font=('times', 20, 'bold'), fg='black', bg='grey')
  name_en.pack(side='right', padx=20)
  roll = Label(frm2, font=('times', 20, 'bold'), bg='green', text='Roll No')
  roll.pack(side='left', padx=20)
  roll_en = Entry(frm2, font=('times', 20, 'bold'), fg='black', bg='grey')
  roll_en.pack(side='right', padx=20)
  def sub1():
    nm = name_en.get()
    rl = roll_en.get()
    if (nm != '' and rl != ''):
      log_user.log(nm,rl)
      new.destroy()
    else:
        tkMessageBox.showerror("Error", "Please enter Name and Roll No.")
  sub = Button(new, bg='black', fg='yellow', bd=5, font=('times', 20, 'bold'), text="Submit", command=sub1)
  sub.pack(anchor='center')
  new.mainloop()
