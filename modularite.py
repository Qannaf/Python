#coding:utf-8
from math import *

#voila mon 6émé code en python
"""
     Les modularité
     
"""

#fonction lambda
coucou = lambda : print("Bonjour")

coucou()


ttc = lambda prixHT:prixHT + (prixHT *20/100)

print(ttc(24))


somme = lambda a=0,b=0: a+b

print(somme(), somme(2,5))


#module
print(sqrt(100),sin(90))

#mes propres modules
from mes_modules.joueur import *
perler()
partir()

from joueur import *
perler()
partir()

