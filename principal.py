import random, time, pygame, sys, comeVocales
from pygame.locals import *
import setup




def menuPrincipal():	
	# MAIN LOOP 
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
					comeVocales.main()

def main():
	pygame.init()
	menuPrincipal()
	s
def terminarPrograma():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
    main()
