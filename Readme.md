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

## 2. les variables variable.py
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

## 3. Les opérateurs (+,-,/ rt *)  operateur.py
````
calcul = 5/2
print("Le résultat en réel = {} \t Le résultat en entier = {} \n calul +1 = {}".format(calcul,int(calcul),calcul+1))
````

## 4. Les conditions conditions.py
````
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

## 5. Les boucles boucles.py

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

## 6. Les fonctions fonctions.py
````
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

## 7. Fonction lambda & Les modularité   modularite.py joueur.py mes_modules/joueur.py
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

## 8. Gestion les erreurs gestion_erreurs.py
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

## 9. Les POO	poo.py

````
#methode 1
class Humain:
    """
    Classe des étre humains
    """
    def __init__(self,m_prenom = "jojo", m_age = 100):
        #pass
        self.prenom = m_prenom
        self.age = m_age
        print("création Humain...",self.prenom,self.age ) #self pour afficher a'addresse

        
print("Lancement de programme...")
h1 = Humain()
print("prénom de h1 {}".format(h1.prenom), "age de h1", h1.age)


#methode 2 par les parametres
    #compteur le nombre de objet crée
class Humain:
    compteur = 0
    def __init__(self,m_prenom="alsahmi",m_age = 10): #constrecture
        self.prenom = m_prenom
        self.age = m_age
        Humain.compteur +=1

        

h1 = Humain("Qannaf",27)
h2 = Humain()
print("prénom de h1 {} et son age = {} ans".format(h1.prenom,h1.age))
print("prénom de h2 {} et son age = {} ans".format(h2.prenom,h2.age))

h1.prenom = "ahmed"
print("prénom de h1 {} et son age = {} ans".format(h1.prenom,h1.age))

print("Humains existants : {}".format(Humain.compteur ))
````


## 10. Les methodes de la class methodes.py
````
class Humain:
    """"Classe qui définit un humain"""
    lieu = "France"                    #attribue de la classe
    def __init__(self,m_nom ="Qannaf" ,m_age = 29):   #constrecture
        self.nom = m_nom
        self.age = m_age
        
    def parler(self,message):         #self = methode instance (objet)
        print("{} a dit {}".format(self.nom,message))


    def changer_lieu(cls,nouveau_lieu):  #cls = methode de classe
        Humain.lieu = nouveau_lieu   
    changer_lieu = classmethod (changer_lieu)

    def definition():                    #methode statistique
        print("L'humain est qlqchose de vivant")   
    definition = staticmethod (definition)

#prgm principale
h1 = Humain("Ahmed")
h1.parler("Bonjour à tous")

print("lieu actuelle : {}".format(Humain.lieu))
Humain.changer_lieu("Yémen")
print("lieu actuelle : {}".format(Humain.lieu))
 
Humain.definition()
````


## 11. encapsulation	encapsulation.py
````
class Humain:
    """"Classe qui définit un humain"""
    def __init__(self,m_nom ="No name" ,m_age = 0):   #constrecture
        self._nom = m_nom                            #private
        self._age = m_age                            #private
        
    def _getnom(self):
        return self._nom

    def _setnom(self,nouvel_nom):
        self._nom = nouvel_nom

    def _getage(self):
        #print("Récupération interdite")
        if self._age<= 1:
            return "{} {}".format(self._age,"an")
        return "{} {}".format(self._age,"ans")
    
    def _setage(self,nouvel_age):
        if nouvel_age<0:
            self._age=0
        else:
            self._age = nouvel_age
    
    #propreité <getter>,<setter>,<deleter>,<helper>
    age = property(_getage,_setage)
    nom = property(_getnom,_setnom)



    
#prgm principale
h1 = Humain("Qannaf",27)

print(h1.nom,"\t",h1.age)
h1.nom = "ALSAHMI"
h1.age = -3
print(h1.nom,"\t",h1.age)
print("{} {}".format(h1.nom,h1.age))
````

## 12. Héritage		heritage.py

#pass si il y a pas un constructeur

#class mere
class Vehicule :
    def __init__(self,nom,peneau):
        self.nom = nom
        self.peneau = peneau

    def se_deplacer (self):
        print("la vehicule {} est deplacer...".format(self.nom))
    

#class fille
class Voiture(Vehicule):
    def __init__(self,nom,peneau,vitesse):
        Vehicule.__init__(self,nom,peneau)
        self.vitesse = vitesse

#class fille
class Avion(Vehicule):
    def __init__(self,nom,peneau,voyage):
        Vehicule.__init__(self,nom,peneau)
        self.voyage = voyage



#prgm principale

v1 = Vehicule("Taxi",31)
v1.se_deplacer()
print(v1.peneau,"Voila")

v2 = Voiture("Toyota",16,220)
v2.se_deplacer()
print(v2.vitesse,"Voila")

v3 = Avion("Airbus",3,"Yémen")
v3.se_deplacer()
print("Sana'a",v3.voyage)

#vérification la class de l'objet
if isinstance(v3,Vehicule):
    print("v3 est une Véh")

if isinstance(v3,Avion):
    print("v3 est une Véh")

#verification l'héritage
if issubclass(Avion,Vehicule):
    print("Avion hérite Vehicule ")
    
#héritage multiple

class Etudiant :
    pass
class Enseignant:
    pass

class Doctorant(Etudiant,Enseignant):
    pass
````


