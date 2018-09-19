#########################################
#	Universidad Nacional de la Plata	#
#	Seminario de lenguajes Python		#
#	Año 2018							#
#										#
#	Autores								#
#		Cabot, Juan Andrés 				#
#		Ruiz, Daiana Florencia 			#
#										#
#	Recursos 							#
#		openclipart.org					#  
#		freesound.org					#
#										#
#										#
#	Licencia Libre  					#
#		 								#
#										#
#########################################

import pygame
from pygame.locals import *
import sys


V_ANCHO = 1024
V_LARGO = 700
	
pantalla = pygame.display.set_mode((V_ANCHO,V_LARGO))


def terminarPrograma():
	pygame.quit()
	sys.exit()

pygame.mixer.init()
#Sonidos 

### CHANNEL 0 ###
S_Click = pygame.mixer.Sound('Sonidos/Click.wav')
S_Correcto = pygame.mixer.Sound('Sonidos/Correcto.wav')
S_Incorrecto = pygame.mixer.Sound('Sonidos/Incorrecto.wav')

M_Constante = pygame.mixer.music.load('Sonidos/MusicaPrincipal.ogg')



