from tkinter import*

######################################### fenetre de l'application
cal = Tk()
operateur = ""
cal.title('Qannaf - Calculature')

#######################################  Fonctions  #################################

def clic_btn(nmuero):
    global operateur
    operateur = operateur+ str(nmuero)
    text_entre.set(operateur)


def clic_btn_effacer():
    global operateur
    operateur =""
    text_entre.set("")

def clic_btn_eguel():
    global operateur
    somme = str(eval(operateur))
    text_entre.set(somme)
    operateur=""



text_entre = StringVar()
texte_apparaitre = Entry(cal, font=('arial', 17, "bold"), textvariable=text_entre,bd=20, insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)

btn7 = Button(cal, padx=16,bd=6, fg="black", font=('arial', 17, "bold"), text="7",bg="powder blue",justify='right',command=lambda:clic_btn(7)).grid(row=1,column=0)
btn8 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="8",bg="powder blue",justify='right',command=lambda:clic_btn(8)).grid(row=1,column=1)
btn9 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="9",bg="powder blue",justify='right',command=lambda:clic_btn(9)).grid(row=1,column=2)
btn_add = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="+",bg="powder blue",justify='right',command=lambda:clic_btn("+")).grid(row=1,column=3)
btn4 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="4",bg="powder blue",justify='right',command=lambda:clic_btn(4)).grid(row=2,column=0)
btn5 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="5",bg="powder blue",justify='right',command=lambda:clic_btn(5)).grid(row=2,column=1)
btn6 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="6",bg="powder blue",justify='right',command=lambda:clic_btn(6)).grid(row=2,column=2)
btn_sous = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="-",bg="powder blue",justify='right',command=lambda:clic_btn("-")).grid(row=2,column=3)
btn1 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="1",bg="powder blue",justify='right',command=lambda:clic_btn(1)).grid(row=3,column=0)
btn2 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="2",bg="powder blue",justify='right',command=lambda:clic_btn(2)).grid(row=3,column=1)
btn3 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="3",bg="powder blue",justify='right',command=lambda:clic_btn(3)).grid(row=3,column=2)
btn_mult = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="*",bg="powder blue",justify='right',command=lambda:clic_btn("*")).grid(row=3,column=3)
btn0 = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="0",bg="powder blue",justify='right',command=lambda:clic_btn(0)).grid(row=5,column=0)
btnc = Button(cal, padx=16,bd=6,  fg="black", font=('arial', 17, "bold"), text="C",bg="powder blue",justify='right',command=clic_btn_effacer).grid(row=5,column=1)
btn_eguel = Button(cal,bd=6,  padx=16, fg="black", font=('arial', 17, "bold"), text="=",bg="powder blue",justify='right',command=clic_btn_eguel).grid(row=5,column=2)
btn_div = Button(cal,bd=6,  padx=16, fg="black", font=('arial', 17, "bold"), text="/",bg="powder blue",justify='right',command=lambda:clic_btn("/")).grid(row=5,column=3)

############################################## main menu ###################################################

cal.mainloop()












