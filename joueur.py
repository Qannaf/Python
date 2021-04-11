#coding:utf-8

"""
Module pour le joueur

"""

def perler(nom_p="Qannaf",message="Salut!",age=int("18")):
    print("nom {} : message {} : age {} ans".format(nom_p,message,age))

def partir():
    print("aurevoir !")


#tester le module joueur avant d'utiliser

if __name__ == "__main__":
    perler("qannaf","salut à tous")
    partir()
    
