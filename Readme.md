## 1. Premier code en python  script.py
""" commentaire en
pluseurs lignes
juste avec les double cotte
"""
````
print("Bonjour tout le monde,\n je m'appele Qannaf!")
print('\tje suis ingenieur de logiciel')
print("\tvoila je peux dire que j'ai appris le python")
````

## 2. 2éme code en python les variables variable.py
````
agePersonne = 27
agePersonne1 = 27.
nomPersonne = "Qannaf"
Personne = True

#Pour voir le ype de chaque variable
print(type(agePersonne))
print(type(agePersonne1))
print(type(nomPersonne))
print(type(Personne))

# affichage 1
print("Votre nome c'est : ",nomPersonne)
print("votre age est : ",agePersonne)

# affichage 2
phrase = "Votre nome c'est {} et votre age est {} "
print(phrase.format(nomPersonne,agePersonne))

# affichage 3
print("Votre nome c'est {} et votre age est {} ".format(nomPersonne,agePersonne))

# fonction input()
nomPersonne = input("S.V.P entrer votre nom : ")
print("Bienveneu {} dans notre club".format(nomPersonne))


#changer le type de variable

prix = int(input("entrez le prix : "))
prixTotal = prix + (prix* 20/100)
print("le prix = {}".format(prixTotal))

vrai = True
faux = False
print("vrai booleen = {}\tvrai entier = {} \t faux booleen = {}\tfaux entier = {}".format(vrai, int(vrai),faux,int(faux)))
````

## 3. voila mon 3émé code en python  operateur.py
````
"""
     Les opérateurs (+,-,/ rt *)
"""
calcul = 5/2
print("Le résultat en réel = {} \t Le résultat en entier = {} \n calul +1 = {}".format(calcul,int(calcul),calcul+1))
````

## 4. 4émé code en python conditions.py
````
"""
     Les conditions
"""
identifiant = "Qannaf"
motDePasse = "qannaf92"

print("interface de connextion")
nom = input("entrez votre nom : ")
mot= input("entrez votre mot de passe : ")

if identifiant == nom and mot == motDePasse:
    print ("Bienvenue {} \nvous etes bien connecte".format(nom))
else:
    print("Je ne suis plus dans le if")

lettre = input("Svp entrez votre lettre : ")
if lettre in "aeiouy":
    print("c'est une voyelle")
else:
    print("c'est une consonne")

    
if lettre not in "aeiouy":
    print("c'est une consonne")
else:
    print("c'est une voyelle")

age = int(input("entrez votre age :"))

if age == 18:
    print("tu vient d'etre majeur")
elif 18<age <= 30:
    print("c'est le temps de se marier")
else :
    print("tu as {} ans".format(age))

````

## 5. 5émé code en python boucles.py

* while
````
i = 0
while i<5 :
    print("compteur = {}".format(i))
    i=i+1 #i+=1

test = True

while test :
    mot = input("> ")
    
    if mot == "again" :
        continue
    elif mot == "quit":
        test = False
    elif mot =="hello":
        print("Bonjour :)!")
    else :
        print("commande introuvable")

print("A bientot ...")
````

## 6. 6émé code en python fonctions.py
````
"""
     Les fonctions
"""

#ma fonction
def dire_bonjour():
    print("Bonjour à tous ! :)")

def dire(nom_p="Qannaf",message="Salut!",age=int("18")):
    print("nom {} : message {} : age {} ans".format(nom_p,message,age))


dire_bonjour()
dire("ALSAHMI","Bonjour")
dire("Ahmed","Salut!")
dire()


def  lire_arme(*final_i):
    for i in final_i:
        print(i)

lire_arme("épée")
lire_arme("épée","arc","cheval","couteau")



def somme(n1, n2):
    return n1 + n2

nbr1 = int(input("nbr1 = "))
nbr2 = int(input("nbr2 = "))
print("{} + {} = {}".format(nbr1,nbr2,somme(nbr1,nbr2)))

````

## 7. 7émé code en python Les modularité   modularite.py joueur.py mes_modules/joueur.py
````
#fonction lambda

coucou = lambda : print("Bonjour")
coucou()


ttc = lambda prixHT:prixHT + (prixHT *20/100)
print(ttc(24))


somme = lambda a=0,b=0: a+b
print(somme(), somme(2,5))
````
````
from math import *

#module
print(sqrt(100),sin(90))

#mes propres modules
from mes_modules.joueur import *
perler()
partir()

from joueur import *
perler()
partir()
````

## 8. 8éme code en python gestion les erreurs gestion_erreurs.py
````
age = input("Quels age as-tu ? ")

try:
    age = int(age)
except:
    print("l'age indiqué est c'est pas un nombre !")
else:
    print("Tu as {} ans".format(age))
finally:
     print("fin de programme !")


#mieux comprandre try
n1 = 150
n2 = input("entrer n2 = ")

try:
    n2 = int(n2) 
except ValueError:
    print("valeur incorrecte")
else:
    print("Bravo, tu as noté un nbr")
    try:
        print("Résultats = {}/{} = {}".format(n1,n2,int(n1/n2)))
    except ZeroDivisionError:
        print("Vous ne pouvez pas divider par zéro")
finally:
    print("Fin du programme...")


#pas important
try:
    age = int(input("Quels age as-tu ? "))
    assert age > 25 #je veux que age soit > 25
except AssertionError:
    print("je veux que age soit > 25")
````



