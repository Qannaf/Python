#coding:utf-8

#voila mon 17émé code en python
"""
     Les dicationnaire
"""
#Création de dictionnaire
dic = {"prénom":"Qannaf"}              #la dictionnaire c'est les crouché
print(dic["prénom"])
dic = {1:123,"chat":"c'est un animale domastique"}             
print(dic["chat"])
dic["chat"] = "c'est un animale le meilleur preferer de l'homme"
print(dic["chat"])
dic["chien"] = "c'est un animale trés fidele"
print(dic["chien"])



dic = {"Salut":"Hi","Bonjour":"Good morning"}
print(dic)
v_suprime = dic.pop("Salut")
print (v_suprime)

del dic["Bonjour"]
print(dic)

dic = {"Salut":"Hi","Bonjour":"Good morning","Aller":"Go","D'accord":"Okey"}
if "chien" in dic :
    print("oui")
else:
    print("non")
if "Salut" in dic :
    print("oui")
else:
    print("non")

for i in dic:
    print(i)

for i in dic.keys():
    print(i)

for i in dic.values():
    print(i)


for k,v in dic.items():
    print("le mot : {}--->  sa traduction  : {}".format(k,v))

dic ["Qannaf"] = "votre prénom"
print(dic)


dic2 = dic   # la copie c'est par réferance
dic2 ["ALSAHMI"] = "Votre nom"
print(dic)


def mafonction(nom,age):
    pass

mafonction(age = 27,nom = "Qannaf")


def mafonction(**p):
    print(p)
mafonction(x  = 123,y = "Qannaf")

def mafonction(*p):
    print(p)
mafonction(123,"Qannaf")

def mafonction(**p):
    print(p)
mafonction(y = "Qannaf")

