#coding:utf-8

#voila mon 5émé code en python
"""
     Les boucles
"""

#while
i = 0
while i<5 :
    print("compteur = {}".format(i))
    i=i+1 #i+=1

test = True

while test :
    mot = input("> ")
    
    if mot == "again" :
        continue
    elif mot == "quit":
        test = False
    elif mot =="hello":
        print("Bonjour :)!")
    else :
        print("commande introuvable")

print("A bientot ...")


#for


