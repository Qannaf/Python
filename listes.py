#coding:utf-8

#voila mon 15émé code en python  pass si il y a pas un constructeur

#Création une liste


liste = list()
print(liste)

liste = [1,2,3,4,"Vélo"]
print(liste)

liste = [1]*10
print(liste)
print(liste[:])

liste = range(20)
print(liste)

#boucle
i=0
while i<len(liste):
    print(liste[i])
    i+=1
    
for element in liste:
    print(element)


liste =["Arc","épée","bouclier","potion","fleche","tunique"]
for element in liste:
    print(element)

#accéder un élément    liste[x] = affiche l'élément d'indice 1
                      # liste[-x] = affiche x éme l'élément en partant de la fin
                    # list [A:B] = affiche de A à B
    print(liste[3])
    print(liste[-3])
    print(liste[:])
    print(liste[:3])
    print(liste[3:])
    print(liste[1])
    print(liste[-1])
    print(liste[-4])
    print(liste[2:5])
liste [2] = "Qannaf"
print(liste)

"""
liste[:] = ["bouclier d'acier"]*len(liste)
print(liste[:])

liste[2:4] = ["bouclier d'acier"]*2
print(liste[:])
"""

if "Arc" in liste:
    print("Arce trové")
else:
    print("rien")

liste.append("Alsahmi")
print(liste[:])
liste.append("Ahmed")
print(liste[:])

liste.insert(0,"Saleh")
print(liste[:])


liste.remove("Saleh")
print(liste[:])
del liste[0]
print(liste[:])

print("l'indice de alsahmi",liste.index("Alsahmi"))

objrt_sprm = liste.index("Alsahmi")
del liste[objrt_sprm]
print(liste[:])

liste.remove("Ahmed")
print(liste[:])

liste = [3,-4,55,3,76,-5,56,4,-8,345]
print(liste[:])
liste.sort()
print(liste[:])
liste.reverse()
print(liste[:])

print("nbr de potions",liste.count(3))

liste.clear
print(liste[:])

