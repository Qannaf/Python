#coding:utf-8

#voila mon 16émé code en python
"""
     Les tuples
"""

liste = [1,2,3,4,5,6]              #créer des (0,1)
for i in enumerate(liste) :    
    print(i)


#Tuple un fois créer on ne peux pas le modifier
mon_tuple = (45,)  #pour avoir un tuple on mais , la virgule
print(type(mon_tuple))

n_tuple = 45,
print(type(mon_tuple))
n_tuple = ()
print(type(mon_tuple))
n_tuple = (4,5)
print(type(mon_tuple))
try:
    print((mon_tuple[0]))   
except :
    print("dépasement de tuple...")

nb1 = 14
nb2 = 24
print(nb1,nb2)
nb1,nb2= 14,24
print(nb1,nb2)
(nb1,nb2)= (14,24)
print(nb1,nb2)

nb1 = 0   #façon de modifier un élément tuple
print(nb1,nb2)

def get_joueur():
    q = 123
    a = 23
    return (q,a)
#prgm principle
x = 0
y = 0
print("le joueur {},{}".format(x,y))
x,y = get_joueur()
print("le joueur {},{}".format(x,y))
x,y =0,10
print("le joueur {},{}".format(x,y))
