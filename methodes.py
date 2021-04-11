#coding:utf-8

#voila mon 10émé code en python

class Humain:
    """"Classe qui définit un humain"""
    lieu = "France"                    #attribue de la classe
    def __init__(self,m_nom ,m_age):   #constrecture
        self.nom = m_nom
        self.age = m_age
        
    def parler(self,message):         #self = methode instance (objet)
        print("{} a dit {}".format(self.nom,message))
        
    def changer_lieu(cls,nouveau_lieu):  #cls = methode de classe
        Humain.lieu = nouveau_lieu
        
    changer_lieu = classmethod (changer_lieu)

    def definition():                    #methode statistique
        print("L'humain est qlqchose de vivant")
        
    definition = staticmethod(definition)
#prgm principale
h1 = Humain("Qannaf",27)

h1.parler("Bonjour à tous")

print("lieu actuelle : {}".format(Humain.lieu))
Humain.changer_lieu("Yémen")
print("lieu actuelle : {}".format(Humain.lieu))
 
Humain.definition()
