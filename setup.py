import pygame
from pygame.locals import *
import sys


V_ANCHO = 1024
V_LARGO = 700

pantalla = pygame.display.set_mode((V_ANCHO,V_LARGO))

def terminarPrograma():
	pygame.quit()
	sys.exit()
