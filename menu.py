#coding:utf-8
from tkinter import *

''' ===============           fonction                =============  '''
def myfonction():
	print("Hello! ...")
	
def myaffich():
	a = Toplevel(mon_app)
	a.title("A propos de mon_app")
	lb = Label(a, text = "Qannaf c'est lui qui a crée cette application")
	lb.pack()
''' ===============      ***les fenetres***           =============  '''

#Creation et parametre de la fenetre ...
mon_app = Tk()
mon_app.geometry("640x480")
mon_app.title("Mon interface")


#widgets ...
menu_principale =  Menu(mon_app)

menu_1 = Menu(menu_principale,tearoff = 0)
menu_1.add_command(label="Option1",command = myfonction)
menu_1.add_command(label="Option2")
menu_1.add_command(label="Quitter",command = mon_app.quit)

menu_2 = Menu(menu_principale,tearoff = 0)
menu_2.add_command(label="Commande1")
menu_2.add_command(label="Commande2")
menu_2.add_command(label="A propos",command = myaffich)

menu_principale.add_cascade(label="Premier", menu=menu_1)
menu_principale.add_cascade(label="Second", menu=menu_2)

#Boucle pribcipale
mon_app.config(menu=menu_principale)
mon_app.mainloop()



