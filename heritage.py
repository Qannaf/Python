#coding:utf-8

#voila mon 13émé code en python  pass si il y a pas un constructeur

#class mere
class Vehicule :
    def __init__(self,nom,peneau):
        self.nom = nom
        self.peneau = peneau

    def se_deplacer (self):
        print("la vehicule {} est deplacer...".format(self.nom))
    

#class fille
class Voiture(Vehicule):
    def __init__(self,nom,m_peneau,vitesse):
        Vehicule.__init__(self,nom,m_peneau)
        self.vitesse = vitesse


class Avion(Vehicule):
    def __init__(self,nom,m_peneau,voyage):
        Vehicule.__init__(self,nom,m_peneau)
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
    print("v2 est une Véh")

if isinstance(v3,Avion):
    print("v2 est une Véh")

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
