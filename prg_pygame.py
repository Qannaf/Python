#coding:utf-8
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

test = True

while test:
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            test = False
    