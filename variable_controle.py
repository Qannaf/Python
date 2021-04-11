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
var = StringVar()              #StringVar(), IntVar(), DoubleVar(), BooleanVar()

test = Label(mon_app, text = "bonjour",textvariable = var)
test.pack()

var.set("Coucou")   #remplacer l text sur l'interface
print("Label:",type(var.get()))

#Boucle pribcipale
mon_app.mainloop()



		################################

#Observateur	
def misajour(*args):
	var_label.set(var_entry.get())		
		
		
								
								
#Creation la fenetre ...
mon_app = Tk()
mon_app.title("Mon interface")


#widgets ...
var_entry = StringVar()              
entry = Entry(mon_app,textvariable = var_entry)
var_entry.trace("w",misajour)

var_label = StringVar()              
label = Label(mon_app,textvariable = var_label)
var_label.set("Entrez votre nom ...")


entry.pack()
label.pack()


#Boucle pribcipale
mon_app.mainloop()



############################"""

#Observateur	
def misajour(*args):
	if var.get():
		print("Homme ...")
	else:
		print("Femme ...")		
		
		
								
								
#Creation la fenetre ...
mon_app = Tk()
mon_app.title("Mon interface")


#widgets ...
var = IntVar()
radio1 = Radiobutton(mon_app,text = "Homme",value = 1,variable = var)
radio2 = Radiobutton(mon_app,text = "Femme",value = 0,variable = var)

var.trace("w",misajour)


radio1.pack()
radio2.pack()


#Boucle pribcipale
mon_app.mainloop()


############################"""

#Observateur	
def misajour(*args):
	if var1.get():
		var2.set("Homme ...")
	else:
		var2.set("Femme ...")		
		
		
								
								
#Creation la fenetre ...
mon_app = Tk()
mon_app.title("Mon interface")


#widgets ...
var1 = IntVar()
radio1 = Radiobutton(mon_app,text = "Homme",value = 1,variable = var1)
radio2 = Radiobutton(mon_app,text = "Femme",value = 0,variable = var1)

var2 = StringVar()
label_gender = Label(mon_app, textvariable = var2)

var1.trace("w",misajour)


radio1.pack()
radio2.pack()
label_gender.pack()

#Boucle pribcipale
mon_app.mainloop()










############################"""

#Observateur	
def misajour(*args):
	if var1.get()>10.0:
		btn1.config(bg="red")
	else:
		btn1.config(bg="green")		
		
		
								
								
#Creation la fenetre ...
mon_app = Tk()
mon_app.title("Mon interface")


#widgets ...
var1 = DoubleVar()
btn1 =Entry(mon_app,textvariable = var1)
var1.trace("w",misajour)


btn1.grid()



#Boucle pribcipale
mon_app.mainloop()
