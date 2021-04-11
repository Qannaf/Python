#coding:utf-8

''' ===============  ***les fenetres*** =============  '''

#import tkinter
#from tkinter import messagebox   #pour envoyer des avertissemment en cas des erreurs
from tkinter import *



''' =======      pgrm           ============= '''

#Creation et parametre de fenetre ...
mon_app = Tk()
mon_app.title("Mon premier programme interface")


#widgets ...
              #StringVar(), IntVar(), DoubleVar(), BooleanVar()
def sup():
	test.forget()

test = Button(mon_app, text = "Delete me",command=sup)
test.pack()



#Boucle pribcipale
mon_app.mainloop()



	