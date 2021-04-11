#coding:utf-8

''' ===============  ***les fenetres*** =============  '''

import tkinter
#from tkinter import *


''' =======      pgrm           ============= '''

#Label    il affiche le msg dans un seul ligne sauf si on lui a demandé de reterne à la ligne
mon_app = tkinter.Tk()
mon_app.title("Mon premier programme interface")
msg = tkinter.Label(mon_app, text= "Bienvenue à tous !")

print(msg["text"])  #afficherle msg au terminal en tant que dictionnaire
print(msg.cget("text")) #afficherle msg au terminal par methode

msg["text"] = "Hello evry one !"  #changer le msg en tant que dictionnaire
msg.config(text="Hollaaaaaaaaaaaaaaaaaaaaaaaaaa !")  #changer le msg par methode

msg.pack()
mon_app.mainloop()


#Message   elle passe à la ligne seul
mon_app = tkinter.Tk()
mon_app.title("Mon premier programme interface")
msg = tkinter.Message(mon_app, text= "Bonjour et Bienvenue à tous  !")
msg.pack()
mon_app.mainloop()

#Entry   
mon_app = tkinter.Tk()
mon_app.title("Mon premier programme interface")
msg = tkinter.Entry(mon_app, show = "*")   #show pour le mot de passe
msg.pack()
mon_app.mainloop()

mon_app = tkinter.Tk()
mon_app.title("Mon premier programme interface")
msg = tkinter.Entry(mon_app, exportselection=0)   #exportselection empecher la selection du text
msg.pack()
mon_app.mainloop()


#Button  
def hello():
	print("Hello sur le terminal!")
	
mon_app = tkinter.Tk()
mon_app.title("Mon premier programme interface")
msg = tkinter.Button(mon_app, text = "Ok", width=25, height=5,command = hello)   #show pour le mot de passe
msg.pack()
mon_app.mainloop()

