## 1. Premier code en python
""" commentaire en
pluseurs lignes
juste avec les double cotte
"""
````
print("Bonjour tout le monde,\n je m'appele Qannaf!")
print('\tje suis ingenieur de logiciel')
print("\tvoila je peux dire que j'ai appris le python")
````

## 2. 2éme code en python les variables
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

## 3. #voila mon 3émé code en python
````
"""
     Les opérateurs (+,-,/ rt *)
"""
calcul = 5/2
print("Le résultat en réel = {} \t Le résultat en entier = {} \n calul +1 = {}".format(calcul,int(calcul),calcul+1))
````