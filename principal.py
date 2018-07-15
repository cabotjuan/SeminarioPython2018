import random, time, pygame, sys, comeVocales
from pygame.locals import *
from setup import *



def cargarMenu():
	
	pygame.draw.rect(pantalla, pygame.Color("blue"), (V_ANCHO/3, V_LARGO/9 ,350, 100), 0)
	
	pygame.draw.rect(pantalla, pygame.Color("pink"), (V_ANCHO/2.5, V_LARGO/3 ,250, 75), 0)
	
	
	
	
def menuPrincipal():	
	# MAIN LOOP 
	
	#fuente = pygame.font.Font(None, 32)
	#t_titulo = 'Comenzar a jugar'
	#titulo = fuente.render(t_titulo, True, pygame.Color("pink"))
	
	#titulo_rect = titulo.get_rect()
	
	#titulo_rect.centerx = pantalla.get_rect().centerx
	
	#pantalla.blit(titulo, titulo_rect)
	
	cargarMenu()
	pygame.display.update()
	
	
	
	while True:
		#Event Queue
		Qeventos = pygame.event.get()
		
		for evento in Qeventos:
			if evento.type == QUIT:
				terminarPrograma()
				
			elif evento.type == KEYDOWN:
				if evento.key == K_ESCAPE:
					terminarPrograma()
				
				if evento.key == K_1:
					comeVocales2.main()

def main():
	pygame.init()
	menuPrincipal()
	
def terminarPrograma():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
    main()
