#coding:utf-8
import pygame

"""
pygame.FULLSCREEN
pygame.RESIZABLE
pygame.NOFRAME
pygame.display.Info()
pygame.get_sdl_version()
pygame.display.set_caption

pygame.OPENGL
pygame.HWSURFACE
pygame.DOUBLEBUF
"""

pygame.init()

#Création mon_app
res = (640,480)
mon_app = pygame.display.set_mode(res,pygame.RESIZABLE) #(res,pygame.RESIZABLE|pygame.FULLSCREEN)
pygame.display.set_caption("Mon application")     #Changer le nom de mon_app

#information 
print(pygame.display.Info()) 
print(pygame.get_sdl_version())


#quitter mon_app
test = True
while test:
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            test = False
    #res = (640,480)
    #mon_app = pygame.display.set_mode(res,pygame.RESIZABLE)

