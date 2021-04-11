#coding:utf-8

#voila mon 6émé code en python
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
