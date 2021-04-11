#coding:utf-8

#voila mon 12émé code en python

class Humain:
    """"Classe qui définit un humain"""
    def __init__(self,nom ,age):   #constrecture
        self.nom = nom
        self._age = age
        
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

    
#prgm principale
h1 = Humain("Qannaf",27)

print(h1.nom,"\t",h1.age)
h1.nom = "ALSAHMI"
h1.age = 1
print(h1.nom,"\t",h1.age)
print("{} {}".format(h1.nom,h1.age))



