#coding:utf-8

''' ===============  ***les fenetres*** =============  '''

import tkinter
#from tkinter import *

fenetre = tkinter.Tk()
fenetre.title("Mon premier programme interface")
#fenetre.minsize(640,480)
#fenetre.maxsize(740,580)
#fenetre.geometry("800600")
#fenetre.resizable(width = False, height = False)
#fenetre.positionfrom("user")
#fenetre.sizefrom("user")
#geometry("X×Y+0+0")
fenetre.geometry("800×600+50+10")

'''
screen_x = int(fenetre.winfo_screenmmwidth())
screen_y =int(fenetre.winfo_screenheight())

window_x = 600
window_y = 480

"""
position_X =  (largeur_ecran//2)-(largeur_fenetre//2)
position_Y = (hauteur_ecran//2)-(hauteur_fenetre//2)
"""
position_X =  (screen_x //2)-(windows_x//2)
position_Y = (screen_y //2)-(windows_y//2)
geo = "{}×{}+{}+{}".format(window_x, window_y,position_X, position_Y )
fenetre.geometry(geo)
'''
fenetre.mainloop()

