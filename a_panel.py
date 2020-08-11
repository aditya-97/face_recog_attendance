from Tkinter import *
from create  import  user
from train import trn
from db_handle import delet,get_data
import ui
import tkMessageBox
def panel():
    home = Tk()
    home.geometry('700x500')
    home.resizable(False, False)
    frm1 = Frame(home, bg='blue')
    frm1.pack(fill=BOTH,expand = 1) 
    frm2 = Frame(home, bg='blue')
    frm2.pack(fill=BOTH, expand=1)
    add = Button(frm1, font=('times', 20, 'bold'), text='Add User', bg='black', fg='yellow', bd=5,command=user)
    add.pack(padx=50, pady=20, side='left')
    dlt = Button(frm1, font=('times', 20, 'bold'), text='Delete User', bg='black', fg='yellow', bd=5, command=delet)
    dlt.pack(padx=50, pady=20, side='right')
    tran = Button(frm2, font=('times', 20, 'bold'), text='Train Model', bg='black', fg='yellow', bd=5,command=trn)
    tran.pack(padx=50, pady=20, side='left')
    dat = Button(frm2, font=('times', 20, 'bold'), text='Get Data', bg='black', fg='yellow', bd=5,command=get_data)
    dat.pack(padx=50, pady=20, side='right')
    def on_closing():
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            home.destroy()
            ui.main()
    home.protocol("WM_DELETE_WINDOW", on_closing)
    home.mainloop()
if __name__ == "__main__":
    panel()