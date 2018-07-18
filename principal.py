import random, time, pygame, sys, comeVocales, os
from pygame.locals import *
from setup import *
from itemsJuego import *



def cargarMenu():
	
	#pygame.draw.rect(pantalla, pygame.Color("blue"), (V_ANCHO/3, V_LARGO/9 ,350, 100), 0)
	
	#pygame.draw.rect(pantalla, pygame.Color("pink"), (V_ANCHO/2.5, V_LARGO/53 ,250, 75), 0)
	
	
	
	
	l_botones =[]
	desplY = 200
	for boton in sorted(os.listdir('Imagenes/botones')):
		
		boton= ItemsJuegoGenerica('Imagenes/botones/'+boton, 250, 75)
		
		desplY += V_ANCHO / 9
		
		boton.setX(V_ANCHO/2)
		boton.setY(desplY)
		
		l_botones.append(boton)
		
		pantalla.blit(boton.image, boton.rect)
	
	
	pygame.display.update()
	
	return l_botones
	
def menuPrincipal():	
	# MAIN LOOP 
	
	#fuente = pygame.font.Font(None, 32)
	#t_titulo = 'Comenzar a jugar'
	#titulo = fuente.render(t_titulo, True, pygame.Color("pink"))
	
	#titulo_rect = titulo.get_rect()
	
	#titulo_rect.centerx = pantalla.get_rect().centerx
	
	#pantalla.blit(titulo, titulo_rect)
	
	botonSalir = ItemsJuegoGenerica('Imagenes/salir.png', 75, 75)
	botonSalir.setX(V_ANCHO/24)
	botonSalir.setY(V_LARGO-75)
	pantalla.blit(botonSalir.image, botonSalir.rect)
	
	botonMusica = ItemsJuegoGenerica('Imagenes/musica.png', 75, 75)
	botonMusica.setX(V_ANCHO-60)
	botonMusica.setY(V_LARGO-75)
	pantalla.blit(botonMusica.image, botonMusica.rect)

	botonMenu = ItemsJuegoGenerica('Imagenes/menu.png', 75, 75)
	botonMenu.setX(V_ANCHO/8)
	botonMenu.setY(V_LARGO-75)
	pantalla.blit(botonMenu.image, botonMenu.rect)
	
	p_base= pantalla.copy()
	
	botonJugar = ItemsJuegoGenerica('Imagenes/Jugar.png', 250, 75)
	botonJugar.rect.center = (V_ANCHO/2, V_LARGO/2) #boton de jugar
	
	pantalla.blit(botonJugar.image, botonJugar.rect)
	
	botonPuntos = ItemsJuegoGenerica('Imagenes/misPuntos.png', 250, 75)
	botonPuntos.rect.center = (V_ANCHO/2, V_LARGO/1.5)#boton de puntos
	
	pantalla.blit(botonPuntos.image, botonPuntos.rect)
	
	pygame.display.update()
	
	
	
	
	while True:
		
		presionado = None
		#Event Queue
		Qeventos = pygame.event.get()
	
		
		for evento in Qeventos:
			if evento.type == QUIT:
				terminarPrograma()
				
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				
				if botonJugar.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					presionado = ItemsJuegoGenerica('Imagenes/JugarPresionado.png', 250, 75)
					presionado.setX(botonJugar.getX())
					presionado.setY(botonJugar.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
					pygame.display.update()
					
				
				elif l[0].rect.collidepoint((evento.pos[0],evento.pos[1])):
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/comeVocalesPresionado.png', 250, 75)
					presionado.setX(l[0].getX())
					presionado.setY(l[0].getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
					pygame.display.update()
					
				elif l[1].rect.collidepoint((evento.pos[0],evento.pos[1])):
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/acomodoYFormoPresionado.png', 250, 75)
					presionado.setX(l[1].getX())
					presionado.setY(l[1].getY())
					
					pantalla.blit(presionado.image, presionado.rect)					
					
					
				elif l[2].rect.collidepoint((evento.pos[0],evento.pos[1])):
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/elEntrometidoPresionado.png', 250, 75)
					presionado.setX(l[2].getX())
					presionado.setY(l[2].getY())
					
					pantalla.blit(presionado.image, presionado.rect)					
					
				
				
				elif l[3].rect.collidepoint((evento.pos[0],evento.pos[1])):
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/enSuLugarPresionado.png', 250, 75)
					presionado.setX(l[3].getX())
					presionado.setY(l[3].getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
				
				pygame.display.update()
					
					
					
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
				if botonJugar.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					
					pantalla.blit(p_base , (0,0))
					pygame.display.update()
					l=cargarMenu()
				
				elif l[0].rect.collidepoint((evento.pos[0],evento.pos[1])):
					comeVocales.main()	
				
				
					
				
					

def main():
	pygame.init()
	menuPrincipal()
	
def terminarPrograma():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
    main()
