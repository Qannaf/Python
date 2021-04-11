#coding:utf-8

#voila mon 9émé code en python
"""
     Les POO
"""

#methode 1
class Humain:
    """
    Classe des étre humains
    """
    def __init__(self):
        #pass
        print("création Humain...") #self pour afficher a'addresse
        self.prenom = "jojo"
        self.age = 100

        
print("Lancement de programme...")
h1 = Humain()
print("prénom de h1 {}".format(h1.prenom))


#methode 2 par les parametres
    #compteur le nombrede objet crée
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
