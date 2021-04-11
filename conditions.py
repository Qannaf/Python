#coding:utf-8

#voila mon 4émé code en python
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
