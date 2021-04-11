#coding:utf-8
import pickle
#voila mon 19émé code en python  pass si il y a pas un constructeur
#							


fic = open("doc/fichier.txt","r")
print(fic.read())
fic.close()

#===========
fic = open("doc/fichier.txt","r")

line = fic.readline()               #ligne par ligne
print(line)

line = fic.readline()
print(line)

fic.close()

#===========
fic = open("doc/fichier.txt","r")

line = fic.readlines()               #ligne ptous les lignes
print(line)


fic.close()
#=====================

'''  fait gaffe la fonction read() return string '''
fic = open("doc/fichier.txt","r")
print(fic.read())
print(type(fic.read()))
fic.close()



#=====================

with open("doc/fichier.txt","r") as fic:
	content = fic.read()
	print(content)
	# pas besois de fermer le fichier avec with
	
if fic.closed:
	print("Fermé")


''' =================  l'écriture   =============== '''
with open("doc/fichier.txt","w") as fic:
	fic.write("Hi!\n")
	fic.write(" My name is Qannaf, I have ")
	fic.write(str(27))
	fic.write(" years old\n And Yous? ...")
	
#===========

class Player:
	def __init__(self, name, level):
		self.name = name
		self.level = level 
		
	def Mymethode(self):
		print("{} ({})".format(self.name,self.level))
		
p1 = Player("Qannaf", 10)

''''
with open("doc/player.data","wb") as fic:
	record = pickle.Pickler(fic)
	record.dump(p1)
	'''
with open("doc/player.data","rb") as fic:
	get_record = pickle.Unpickler(fic)
	player_one = get_record.load()
	
player_one.Mymethode()

