import random, os, time, pygame, sys
from pygame.locals import *
from setup import *
from itemsJuego import *
import principal



def main(reproducirSonido, PuntajeJuego):
	
	
	puntos_total = 0
	
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
		
		
	
	img_fija = ItemsJuego('Imagenes/oso.png', 'o', 160, 160)
	img_fija.setX(V_ANCHO/6)
	img_fija.setY(V_LARGO/1.7)
	
	pantalla.blit(img_fija.image, img_fija.rect)	
	p_base = pantalla.copy()
	
	
	img_tacho = ItemsJuegoGenerica('Imagenes/tacho.png', 170, 300)
	img_tacho.setX(V_ANCHO/2)
	img_tacho.setY(V_LARGO/2)
	
	SupTacho = img_tacho.image.convert_alpha()
	SupTacho.fill((0, 0, 0, 1))
	
	pantalla.blit(img_tacho.image, img_tacho.rect)
	
	
	
	tacho_abierto = ItemsJuegoGenerica ('Imagenes/tachoAbierto.png', img_tacho.escX, img_tacho.escY)
	tacho_abierto.setX(img_tacho.getX())
	tacho_abierto.setY(img_tacho.getY())
	
	p_sin_img = pantalla.copy()
	
	
	l_imagenes = os.listdir('Imagenes/imgsElEntrometido/')
	
	l_imgs = []
	
	despl= 100
	for i in l_imagenes:
		
		img = ItemsJuego('Imagenes/imgsElEntrometido/' + i, i[0], 125, 125 )
		img.setX(despl)
		img.setY(V_LARGO/5)
		
		pantalla.blit(img.image, img.rect)
		
		l_imgs.append(img)
		
		despl += 200
	
	
	
	seleccionado = None
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
					
				
				for i in range(len(l_imgs)):
					
					if l_imgs[i].rect.collidepoint(evento.pos[0],evento.pos[1]):
						
						### SE SELECCIONA PALABRA ###
						seleccionado = l_imgs[i]
					
						i_obj = i
						
						l_imgs[i].marca = False
						
						#pantalla.blit(p_sin_nombres, (0,0))
				
				
				if seleccionado:
					
					copia_x = seleccionado.rect.centerx
					copia_y = seleccionado.rect.centery	
					
					pantalla.blit(p_sin_img, (0,0))
					
					for h in range(len(l_imgs)):
						
						if l_imgs[h].marca:
							
							pantalla.blit(l_imgs[h].image, l_imgs[h].rect)
							
					p_con_imgs = pantalla.copy()
					
					seleccionado.rect.centerx = evento.pos[0]
					seleccionado.rect.centery = evento.pos[1]
					pantalla.blit(seleccionado.image, seleccionado.rect)
					
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
			
			
				if seleccionado:
					
					if  img_tacho.rect.collidepoint(evento.pos[0],evento.pos[1]) and img_fija.vocal != seleccionado.vocal:
						
						puntos_total += 5
						pygame.mixer.Channel(0).play(S_Correcto)
						
						pantalla.blit(p_con_imgs, (0,0))
					
					else:
						if img_fija.vocal == seleccionado.vocal:
							
							pygame.mixer.Channel(0).play(S_Incorrecto)
							if puntos_total > 0:
								
								puntos_total -= 2
							
						
						l_imgs[i_obj].marca = True
						pantalla.blit(p_con_imgs, (0,0))
						### VOLVER A SU LUGAR ###
						seleccionado.rect.centerx = copia_x
						seleccionado.rect.centery = copia_y
						pantalla.blit(seleccionado.image, seleccionado.rect)
						
			
			
				elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
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
					
					
				
					
				seleccionado = None
					
			elif evento.type == MOUSEMOTION and seleccionado:
				
				pantalla.blit(p_con_imgs, (0,0))
		
				seleccionado.rect.centerx = evento.pos[0]
				seleccionado.rect.centery = evento.pos[1]
				
				pantalla.blit(seleccionado.image, seleccionado.rect)
				
				#pantalla.blit(SupTacho, (V_ANCHO/2, V_LARGO/2))
				
				if img_tacho.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					
					pantalla.blit(tacho_abierto.image, tacho_abierto.rect)
					
				else:
					pantalla.blit(img_tacho.image, img_tacho.rect)
				
		
		principal.displayPuntaje(puntos_total)		
		pygame.display.update()		
				
				
