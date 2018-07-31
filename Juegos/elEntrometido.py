import random, os, time, pygame, sys
from pygame.locals import *
from Juegos.setup import *
from Juegos.itemsJuego import *
import principal



JUEGOTERMINADO = USEREVENT + 2

def main(reproducirSonido, PuntajeJuego, reproducirMusica):
	
	"""Muestra botones de display. Escribe cuadro con ayuda. Carga imagen fija e imagenes movibles.
	Suma o resta puntos. Revision de eventos en bucle infinito"""
	
	puntos_total = 0
	PuntajeJuego['Jugado'] = time.asctime( time.localtime(time.time()) )
	
	botonSalir = ItemsJuegoGenerica('Imagenes/salir.png', 75, 75)
	botonSalir.setX(V_ANCHO/24)
	botonSalir.setY(V_LARGO-75)
	
	botonSonido = ItemsJuegoGenerica('Imagenes/sonido.png', 75, 75)
	botonSonido.setX(V_ANCHO-60)
	botonSonido.setY(V_LARGO-75) ###BOTON MUSICA###

	botonMenu = ItemsJuegoGenerica('Imagenes/inicio.png', 75, 75)
	botonMenu.setX(V_ANCHO/8)
	botonMenu.setY(V_LARGO-75)
	
	botonMute = ItemsJuegoGenerica('Imagenes/mute.png', 75, 75)
	botonMute.setX(botonSonido.getX())
	botonMute.setY(botonSonido.getY())
	
	pantalla.blit(botonSalir.image, botonSalir.rect)###BOTON SALIR###
	pantalla.blit(botonMenu.image, botonMenu.rect)###BOTON MENU###
	
	if reproducirSonido:
		pantalla.blit(botonSonido.image, botonSonido.rect)###BOTON MUSICA###
		
	else:
		pantalla.blit(botonMute.image, botonMute.rect)###BOTON MUSICA###
		
	botonMusica = ItemsJuegoGenerica('Imagenes/musica.png', 75, 75)
	botonMusica.setX(V_ANCHO-140)
	botonMusica.setY(V_LARGO-75)
	
	botonMusicaMute = ItemsJuegoGenerica('Imagenes/musicaMute.png', 75, 75)
	botonMusicaMute.setX(V_ANCHO-140)
	botonMusicaMute.setY(V_LARGO-75)
	
	if reproducirMusica:
		pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###
		
	else:
		pantalla.blit(botonMusicaMute.image, botonMusicaMute.rect)###BOTON MUSICA###
	
	
	l_fijas = os.listdir('Imagenes/ElEntrometido/imgFijas/')
	fija = random.choice(l_fijas)
	print(fija)
	img_fija = ItemsJuego('Imagenes/ElEntrometido/imgFijas/'+fija, fija[0], 160, 160)
	img_fija.setX(V_ANCHO/3)
	img_fija.setY(V_LARGO/1.7)
	
	###	CARTEL TACHO ###
	
	fondo_t = pygame.draw.rect(pantalla, (0,0,0), (85, V_LARGO/2, 350, 240), 4)
	fuente = pygame.font.Font("Fuentes/Gaegu-Regular.ttf", 28)
	t = fuente.render('TIRA AL TACHO', True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.x = fondo_t.x + 10
	t_rect.centery = fondo_t.centery -80
	pantalla.blit(t, t_rect)
	t = fuente.render('LO QUE NO', True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.x = fondo_t.x + 10
	t_rect.centery = fondo_t.centery  -40
	pantalla.blit(t, t_rect)
	t = fuente.render('EMPIECE CON', True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.x = fondo_t.x + 10
	t_rect.centery = fondo_t.centery 
	pantalla.blit(t, t_rect)
	t = fuente.render('DE', True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.x = fondo_t.x + 50
	t_rect.centery = fondo_t.centery + 65
	pantalla.blit(t, t_rect)
	fuente = pygame.font.Font("Fuentes/Gaegu-Bold.ttf", 60)
	t = fuente.render(fija[0].upper(), True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.x = fondo_t.x + 10
	t_rect.centery = fondo_t.centery + 65
	pantalla.blit(t, t_rect)
	pantalla.blit(img_fija.image, img_fija.rect)	
	
	p_base = pantalla.copy()
	
	
	img_tacho = ItemsJuegoGenerica('Imagenes/tacho.png', 170, 300)
	img_tacho.setX(V_ANCHO/1.7)
	img_tacho.setY(V_LARGO/2)
	
	SupTacho = img_tacho.image.convert_alpha()
	SupTacho.fill((0, 0, 0, 1))
	
	pantalla.blit(img_tacho.image, img_tacho.rect)
	
	
	
	tacho_abierto = ItemsJuegoGenerica ('Imagenes/tachoAbierto.png', img_tacho.escX, img_tacho.escY)
	tacho_abierto.setX(img_tacho.getX())
	tacho_abierto.setY(img_tacho.getY())
	
	p_sin_img = pantalla.copy()
	
	
	l_imagenes = os.listdir('Imagenes/ElEntrometido/imgsElEntrometido')
	
	l_imgs = []
	
	despl= 100
	for i in l_imagenes:
		
		img = ItemsJuego('Imagenes/ElEntrometido/imgsElEntrometido/' + i, i[0], 125, 125 )
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
				
			elif evento.type == JUEGOTERMINADO:
				PuntajeJuego['Puntos'] = evento.pts
				calificar = principal.guardarPuntaje(PuntajeJuego)
				calificacionImg = pygame.image.load('Imagenes/'+calificar+'.png')
				calificacionImgRect = calificacionImg.get_rect()
				calificacionImgRect.center = (V_ANCHO/2, V_LARGO/2)
				pantalla.blit(calificacionImg, calificacionImgRect)
				pygame.display.update()
				pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sonidos/Terminado.wav'))
				pygame.time.delay(3000)
				pantalla.blit(p_base, (0,0))
				principal.menuPrincipal(reproducirSonido, reproducirMusica)
			
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
		
				
				if botonSonido.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					
					presionado = ItemsJuegoGenerica('Imagenes/sonidoPresionado.png', 75, 75)
					presionado.setX(botonSonido.getX())
					presionado.setY(botonSonido.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
				elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirSonido:
					
					presionado = ItemsJuegoGenerica('Imagenes/mutePresionado.png', 75, 75)
					presionado.setX(botonMute.getX())
					presionado.setY(botonMute.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
				elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirMusica:
					
					presionado = ItemsJuegoGenerica('Imagenes/musicaPresionado.png', 75, 75)
					presionado.setX(botonMusica.getX())
					presionado.setY(botonMusica.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
				elif botonMusicaMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirMusica:
					
					presionado = ItemsJuegoGenerica('Imagenes/musicaMutePresionado.png', 75, 75)
					presionado.setX(botonMusicaMute.getX())
					presionado.setY(botonMusicaMute.getY())
					
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
							
					if reproducirSonido:
						pantalla.blit(botonSonido.image, botonSonido.rect)
						#pygame.display.update(botonSonido.rect)
					else:
						pantalla.blit(botonMute.image, botonMute.rect)
						#pygame.display.update(botonMute.rect)
						
							
					if reproducirMusica:
						#pygame.mixer.music.unpause()
						pantalla.blit(botonMusica.image, botonMusica.rect)
						
					else:
						#pygame.mixer.music.pause()
						pantalla.blit(botonMusicaMute.image, botonMusicaMute.rect)
								
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
						
						
						### Verificar si FIN DE JUEGO
						Finalizar = True
						
						for img in l_imgs:
							if img.marca == True and img.vocal != img_fija.vocal:
								Finalizar = False
						if Finalizar:
							p_base = pantalla.copy()
							pantalla.blit(p_base, (0,0))
							ev_finalizado = pygame.event.Event(JUEGOTERMINADO, pts= puntos_total)
							pygame.event.post(ev_finalizado)
						
						
					
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
						
					
						
			
			
				elif botonSonido.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					pygame.mixer.Channel(0).set_volume(0)
					pantalla.blit(botonMute.image, botonMute.rect)
					reproducirSonido = False
						
						
				elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirSonido:
					pygame.mixer.Channel(0).set_volume(1)
					pantalla.blit(botonSonido.image, botonSonido.rect)
					reproducirSonido = True
					
				elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirMusica:
					pygame.mixer.music.pause()
					pantalla.blit(botonMusicaMute.image, botonMusicaMute.rect)
					reproducirMusica = False

				elif botonMusicaMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirMusica:
					pygame.mixer.music.unpause()
					pantalla.blit(botonMusica.image, botonMusica.rect)
					reproducirMusica = True
				
				elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					terminarPrograma()
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					pantalla.blit(p_base, (0,0))
					pygame.display.update()
					principal.menuPrincipal(reproducirSonido, reproducirMusica)
				
					
				seleccionado = None
				
				if reproducirSonido:
					pantalla.blit(botonSonido.image, botonSonido.rect)
					#pygame.display.update(botonSonido.rect)
				else:
					pantalla.blit(botonMute.image, botonMute.rect)
					#pygame.display.update(botonMute.rect)
					
						
				if reproducirMusica:
					#pygame.mixer.music.unpause()
					pantalla.blit(botonMusica.image, botonMusica.rect)
					
				else:
					#pygame.mixer.music.pause()
					pantalla.blit(botonMusicaMute.image, botonMusicaMute.rect)
					
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
				
				
