#coding:utf-8

''' ===============  ***les fenetres*** =============  '''

#import tkinter
#from tkinter import messagebox   #pour envoyer des avertissemment en cas des erreurs
from tkinter import *



''' =======      pgrm           ============= '''

#Creation et parametre de fenetre ...
mon_app = Tk()
mon_app.title("Mon interface")


#widgets ...
#frame = Frame(mon_app, width = 300,height = 200, borderwidth=1)
frame = LabelFrame(mon_app,text = "Titre", width = 300,height = 200, borderwidth=1)


button = Button(mon_app,text = "press her") 


frame.pack()
button.pack()

#Boucle pribcipale
mon_app.mainloop()



'''================='''

#Creation et parametre de fenetre ...
mon_app = Tk()
mon_app.title("Mon interface")


#widgets ...
frame = LabelFrame(mon_app,text = "Title", width = 30,height = 20, borderwidth=1)
label = Label(mon_app, text="Un labal")
entry = Entry(mon_app)
button = Button(mon_app,text = "press her") 


frame.pack(side="top",expand = 1)
label.pack(side="bottom",fill="none",ipadx=100,ipady = 5)
entry.pack(side="right",fill="both",padx=100,pady = 5)
button.pack(side="left", fill="y")

#Boucle pribcipale
mon_app.mainloop()




'''================='''

#Creation et parametre de fenetre ...
mon_app = Tk()
mon_app.title("Mon interface")


#widgets ...
frame = LabelFrame(mon_app,text = "Title", width = 30,height = 20, borderwidth=1)
label = Label(mon_app, text="Un labal")
entry = Entry(mon_app)
button = Button(mon_app,text = "press her") 

frame.grid(row=0, column=0,padx=15,pady=50)
label.grid(row=0, column=1,columnspan=2)
entry.grid(row=0, column=3,rowspan = 1)
button.grid(row=2, column=4,sticky="ne")  #n:nord, s:sud, e:est, o:ouest 

#Boucle pribcipale
mon_app.mainloop()



'''================='''

#Creation et parametre de fenetre ...
mon_app = Tk()
mon_app.title("Mon interface")


#widgets ...

button = Button(mon_app,text = "press her") 
button.place(x=100,y=20)  

#Boucle pribcipale
mon_app.mainloop()
