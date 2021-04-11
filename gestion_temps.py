#coding:utf-8
import time

''' ===============           pgm                =============  '''
print("Le premier texte")
time.sleep(0.5)               #pour suspendre les instructions
print("Le second texte")


#1er Janvier 1970 à 00h00
print(time.time())


debut= time.time()
time.sleep(2)
fin= time.time()

print("temps d'excution = {}s".format(fin-debut))


print(time.localtime())

"""
Localtime()
mktime()
"""
tps = time.localtime()
print(tps)

tps = time.mktime(tps)
print(tps)


"""
%d : jour(01 à 31)
%m : mois(01 à 12)
%Y : année(ex : 2018) - %y (00 à 99)
%H : Heures(00 à 23)
%I : minutes(00 à 59)
%S : secondes(00 à 59)
%p : AM/PM
%A : jour semaine / %a(jour abrégé)
%B : mois  / %b (mois abrégé)
"""

print(time.strftime("%H:%I:%S %A %B %d/%m/%Y %Z"))


