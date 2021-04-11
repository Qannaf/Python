#coding:utf-8

''' ===============  ***les fenetres*** =============  '''

#import tkinter
from tkinter import messagebox   #pour envoyer des avertissemment en cas des erreurs
from tkinter import *



''' =======      pgrm           ============= '''

#Checkbutton
mon_app = Tk()
mon_app.title("Mon premier programme interface")

test = Checkbutton(mon_app, text = "oui",offvalue = 2,onvalue = 5) #valeur par déffaut offvalue = 2,onvalue = 5 

test.pack()
mon_app.mainloop()


#radiobutton
mon_app = Tk()
mon_app.title("Mon premier programme interface")

testc = Checkbutton(mon_app, text = "oui",offvalue = 2,onvalue = 5)

test1 = Radiobutton(mon_app, text = "Homme",value = 1)
test2 = Radiobutton(mon_app, text = "Femme",value = 0)

testc.pack()
test1.pack()
test2.pack()
mon_app.mainloop()



#Scale
mon_app = Tk()
mon_app.title("Mon premier programme interface")

test = Scale(mon_app, from_ = 10,to =100,tickinterval = 25)
test1 = Spinbox(mon_app, from_ = 10,to =10)

test.pack()
test1.pack()
mon_app.mainloop()



#lb
mon_app = Tk()
mon_app.title("Mon premier programme interface")

test = Listbox(mon_app)
test.insert(1,"A")
test.insert(2,"B/C")
test.insert(3,"D")

test.pack()
mon_app.mainloop()




'''   showerreur, showinfo, showwarning, askquestion, askokcancel, askyesno,askretrycancel '''

#messagebox
def myfonction():
	messagebox.askretrycancel("ERREUR","Un probleme est survenu !")#showerreu,showwrning showinf pour declancher une avertisement
	
mon_app = Tk()
mon_app.title("Mon premier programme interface")

test = Button(mon_app, text = "Déclancher une erreur",command = myfonction )

test.pack()
mon_app.mainloop()




