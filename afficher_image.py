#coding:utf-8
import pygame


pygame.init()

#Création mon_app
resolution = (640,480)  
couleur_blanc = (255, 255, 255)
couleur_black = (0, 0, 0)

mon_app = pygame.display.set_mode(resolution) #creation de surface
pygame.display.set_caption("Mon application")   #changer son nom
#mon_app.fill(couleur_blanc)   #mettre couleur pour le fond

#charger l'image
mon_image = pygame.image.load("Qannaf.png") #returne une surface
mon_image.convert_alpha()
#mon_image.convert()


#information 



#quitter mon_app
test = True
while test:
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            test = False
    #Corp de programme
    mon_app.fill(couleur_black)
    mon_app.blit(mon_image, [10, 10])

    pygame.display.flip()

