#coding:utf-8

import tkinter
from tkinter import messagebox


#messagebox
def myfonction():
    messagebox.askyesno("ERREUR","Un probleme est survenu !")
	
mon_app = tkinter.Tk()
test = tkinter.Button(mon_app, text = "Déclancher une erreur",command = myfonction )

test.pack()
mon_app.mainloop()




