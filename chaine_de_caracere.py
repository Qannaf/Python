#coding:utf-8

#voila mon 14émé code en python  pass si il y a pas un constructeur

#Classe str:string(chaine de cractere)

#help(str)
ma_chaine ="Bonjour tout le monde!"
ma_chaine1 = ma_chaine.lower()
ma_chaine2 = ma_chaine.capitalize()
ma_chaine3 = ma_chaine.title()
ma_chaine4 = ma_chaine.upper()

print("{}\n{}\n{}\n{}\n{}".format(ma_chaine,ma_chaine1,ma_chaine2,ma_chaine3,ma_chaine4))



#rempleçage par copie
ch1 = "Bonjour"
ch2 = ch1
print(ch1,ch2)
ch2 = ch1.upper()
print(ch1,ch2)


ch = "MonSuperProgramme"
print(ch)
ch = ch.center(50,'-')
print(ch)

print(ch.find("Super"))
print(ch.index("Super"))
print(ch.strip())

ch1 = ch.replace("M","T",1)
print(ch1)

print(ch2.split("`|"))


ch = "Bonjour"
if ch.islower():
    print("Maj")
else:
    print("min")
    
