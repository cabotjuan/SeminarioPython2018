import random, os, time, pygame, sys
from pygame.locals import *
from setup import *
from itemsJuego import *
import principal



def main(reproducirSonido, PuntajeJuego):
	
	botonSalir = ItemsJuegoGenerica('Imagenes/salir.png', 75, 75)
	botonSalir.setX(V_ANCHO/24)
	botonSalir.setY(V_LARGO-75)
	
	botonMusica = ItemsJuegoGenerica('Imagenes/sonido.png', 75, 75)
	botonMusica.setX(V_ANCHO-60)
	botonMusica.setY(V_LARGO-75) ###BOTON MUSICA###

	botonMenu = ItemsJuegoGenerica('Imagenes/inicio.png', 75, 75)
	botonMenu.setX(V_ANCHO/8)
	botonMenu.setY(V_LARGO-75)
	
	botonMute = ItemsJuegoGenerica('Imagenes/mute.png', 75, 75)
	botonMute.setX(botonMusica.getX())
	botonMute.setY(botonMusica.getY())
	
	pantalla.blit(botonSalir.image, botonSalir.rect)###BOTON SALIR###
	pantalla.blit(botonMenu.image, botonMenu.rect)###BOTON MENU###
	
	if reproducirSonido:
		pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###
		
	else:
		pantalla.blit(botonMute.image, botonMute.rect)###BOTON MUSICA###
		
	p_base = pantalla.copy()
	
	
	l_imagenes = os.listdir('Imagenes/imgsElEntrometido/')
	
	l_imgs = []
	
	despl= 100
	for i in l_imagenes:
		
		img = ItemsJuego('Imagenes/imgsElEntrometido/' + i, i[0], 125, 125 )
		img.setX(despl)
		img.setY(V_LARGO/4)
		
		pantalla.blit(img.image, img.rect)
		
		l_imgs.append(img)
		
		despl += 200
	
	while True:

		Qeventos = pygame.event.get()
		for evento in Qeventos:
			
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
				
				
			
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
		
				
				if botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					
					presionado = ItemsJuegoGenerica('Imagenes/sonidoPresionado.png', 75, 75)
					presionado.setX(botonMusica.getX())
					presionado.setY(botonMusica.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
				elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirSonido:
					
					presionado = ItemsJuegoGenerica('Imagenes/mutePresionado.png', 75, 75)
					presionado.setX(botonMute.getX())
					presionado.setY(botonMute.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
				elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					presionado = ItemsJuegoGenerica('Imagenes/salirPresionado.png', 75, 75)
					presionado.setX(botonSalir.getX())
					presionado.setY(botonSalir.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					presionado = ItemsJuegoGenerica('Imagenes/inicioPresionado.png', 75, 75)
					presionado.setX(botonMenu.getX())
					presionado.setY(botonMenu.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
					
				
					
				
					
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
			
				if botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					pygame.mixer.Channel(0).set_volume(0)
					pantalla.blit(botonMute.image, botonMute.rect)
					reproducirSonido = False
						
						
				elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirSonido:
					pygame.mixer.Channel(0).set_volume(1)
					pantalla.blit(botonMusica.image, botonMusica.rect)
					reproducirSonido = True

				
				elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					terminarPrograma()
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					pantalla.blit(p_base, (0,0))
					pygame.display.update()
					principal.menuPrincipal(reproducirSonido)
					
					
					
			
				
		pygame.display.update()		
				
				
