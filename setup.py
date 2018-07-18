import pygame
from pygame.locals import *


V_ANCHO = 1024
V_LARGO = 740

pantalla = pygame.display.set_mode((V_ANCHO,V_LARGO))

pygame.mixer.init()
#Sonidos 
S_Click = pygame.mixer.Sound('Sonidos/Click.wav')
S_Correcto = pygame.mixer.Sound('Sonidos/Correcto.wav')
S_Incorrecto = pygame.mixer.Sound('Sonidos/Incorrecto.wav')
