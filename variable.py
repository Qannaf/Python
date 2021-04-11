#coding:utf-8
"""
voila mon 2éme code en python les variables
"""


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
