from itemsJuego import *
from setup import *
import random, os, time, pygame, sys





def manejoDeEventos():
	

	while True:
		
		Qeventos = pygame.event.get()
		for evento in Qeventos:
			
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				##########################
				
				
				
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
				##########################
				
				
				

def cargarBotones():
	
	botonOpcionL = ItemsJuegoGenerica('Imagenes/opLetras.png', 560, 120)
	botonOpcionL.setX(V_ANCHO/2)
	botonOpcionL.setY(V_LARGO/2)
	pantalla.blit(botonOpcionL.image, botonOpcionL.rect)###BOTON OPCION DE LETRAS###
	
	botonOpcionS = ItemsJuegoGenerica('Imagenes/opSilabas.png', 560, 120)
	botonOpcionS.setX(V_ANCHO/2)
	botonOpcionS.setY(V_LARGO/2)
	pantalla.blit(botonOpcionS.image, botonOpcionS.rect)###BOTON OPCION DE SILABAS###
	


def main():
	cargarBotones()
	manejoDeEventos()
	
	
if __name__ == '__main__':
	main()
