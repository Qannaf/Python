#coding:utf-8
import pygame


pygame.init()

#Création mon_app
resolution = (640,480)  
couleur_de_fond = (89, 152, 255)
couleur_de_dessin = (0, 0, 0)

mon_app = pygame.display.set_mode(resolution) #creation de surface
pygame.display.set_caption("Mon application")   #changer son nom
mon_app.fill((couleur_de_fond))   #mettre couleur pour le fond



#dessiner ==============================
'''line'''
#pygame.draw.line(mon_app, couleur_de_dessin,[10, 10], [100, 100]) 

'''Rectangle(left,top, largeur, hauteur) '''
#mon_Rectangle = pygame.Rect(10,10,150,65)
#pygame.draw.rect(mon_app, couleur_de_dessin,mon_Rectangle, 5) 

'''Circle([largeur, hauteur], rayon, éppisseur) '''
#pygame.draw.circle(mon_app, couleur_de_dessin, [150,150], 50, 5) 

'''polygone'''
cordonnees = [(100, 10), (10, 10), (30, 40), (40, 60)]
pygame.draw.polygon(mon_app, couleur_de_dessin,cordonnees)

pygame.display.flip()

#information 



#quitter mon_app
test = True
while test:
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            test = False
    #res = (640,480)
    #mon_app = pygame.display.set_mode(res,pygame.RESIZABLE)

