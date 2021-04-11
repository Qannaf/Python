#coding:utf-8
import pickle

''' =================  l'écriture   =============== '''
with open("doc/fichier.txt","w") as fic:
	fic.write("Hi!\t evry one\n")
	fic.write(" My name is Qannaf, I have ")
	fic.write(str(27))
	fic.write(" years old\n And Yous? ...")
	


''' =================  lecteur le fichier   =============== '''
with open("doc/fichier.txt","r") as fic:
	content = fic.read()
	print(content)
	# pas besois de fermer le fichier avec with
	
	
if fic.closed:
	print("\n\t!!! rasurez-vous votre fichier est bien fermé !!!")



''' ========== ===== '''


class Player:
	def __init__(self, name, level):
		self.name = name
		self.level = level 
		
	def Mymethode(self):
		print( "{} ({})".format(self.name,self.level) )
		
p1 = Player("Qannaf", 10)
p1.Mymethode()

with open("doc/player.data","wb") as fic:
	tmp = pickle.Pickler(fic)
	tmp.dump(p1) 
	

	
with open("doc/player.data","rb") as fic:
	tmp = pickle.Unpickler(fic)
	player_one = tmp.load()
	
player_one.Mymethode()
