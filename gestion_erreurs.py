#coding:utf-8
"""
voila mon 8éme code en python les variables
"""

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
except ZeroDivisionError:
    print("Vous ne pouvez pas divider par zéro")
else:
    print("Bravo, tu as noté un nbr valide")
    print("Résultats = {}/{} = {}".format(n1,n2,int(n1/n2)))
finally:
    print("Fin du programme...")


#pas important
try:
    
    age = int(input("Quels age as-tu ? "))
    assert age > 25 #je veux que age soit > 25
except AssertionError:
    print("je veux que age soit > 25")


