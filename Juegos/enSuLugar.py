import random, os, time, pygame, sys
from pygame.locals import *
from Juegos.setup import *
from Juegos.itemsJuego import *
import principal


	
CARGARENSULUGAR = USEREVENT+1
JUEGOTERMINADO = USEREVENT+2


def main(reproducirSonido, PuntajeJuego, reproducirMusica):

	"""Carga botones de display. Muestra cuadro con ayuda. Carga imagenes y sus nombres.
	Revision de eventos en bucle.
	"""
	
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
	
	
	### CARTEL AYUDA ###
	
	fondo_t = pygame.draw.rect(pantalla, (0,0,0), (V_ANCHO - 370, 20, 350, 120), 4)
	fuente = pygame.font.Font("Fuentes/Gaegu-Regular.ttf", 28)
	t = fuente.render('ARRASTRA EL NOMBRE', True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.centerx = fondo_t.centerx
	t_rect.centery = fondo_t.centery - 20
	pantalla.blit(t, t_rect)
	t = fuente.render('A SU LUGAR', True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.centerx = fondo_t.centerx
	t_rect.centery = fondo_t.centery +20
	pantalla.blit(t, t_rect)	
	
	
	
	p_base = pantalla.copy()	
	
	
	l_imagenes = os.listdir('Imagenes/enSuLugar/')
	
	puntos_total = 0
	puntos_etapa = 0
	PuntajeJuego['Jugado'] = time.asctime( time.localtime(time.time()) )
	
	seleccionado = None
	
	ev_enSuLugar = pygame.event.Event(CARGARENSULUGAR)
	pygame.event.post(ev_enSuLugar)
		
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
				
			elif evento.type == CARGARENSULUGAR:
				
				l_casilleros = []
				l_nombres = []
				l_imgs_pantalla = []
				l_nombres_str = []
				desp = 0
				desp1 = 0
				for i in range(2):
					
					k = random.randrange(0, len(l_imagenes))
					nombre = 'Imagenes/enSuLugar/'+str(l_imagenes[k])
					imgNueva = ItemsJuegoGenerica(nombre, 125, 125)
					
					imgNueva.setX(V_ANCHO/4 + desp)
					imgNueva.setY(V_LARGO/4)
					
					pantalla.blit(imgNueva.image, imgNueva.rect)
					l_imgs_pantalla.append(imgNueva)
					casilleroNuevo = CasilleroAcomodo (os.path.splitext(l_imagenes[k])[0],imgNueva.rect.x - 30 ,imgNueva.rect.y + 160, 185, 45)
					l_casilleros.append(casilleroNuevo)
					
					l_nombres_str.append(os.path.splitext(l_imagenes[k])[0])
					
					del l_imagenes[k]
					desp += V_ANCHO/2
					
				p_sin_nombres = pantalla.copy()
				
				for i in range(len(l_nombres_str)):
					
					
					nombre_img = ItemAcomodo(l_nombres_str[i], V_ANCHO/2 - 100, V_LARGO/1.5 + desp1 , 185, 45)
					
					l_nombres.append(nombre_img)
					
					desp1 += 120
				
				
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
					
					
				### VERIFICAR SI SE SELECCIONA ALGUNA PALABRA ###
				for i in range(len(l_nombres)):
					
					if l_nombres[i].rect.collidepoint(evento.pos[0],evento.pos[1]):
						
						### SE SELECCIONA PALABRA ###
						seleccionado = l_nombres[i]
					
						i_obj = i
						
						l_nombres[i].mostrar = False
						
						pantalla.blit(p_sin_nombres, (0,0))
						
						
				if seleccionado:
					
					copia_x = seleccionado.dato_item_rect.centerx
					copia_y = seleccionado.dato_item_rect.centery
				
				### DIBUJO TODAS LAS LETRAS RESTANTES ###
				
					Recargar = True
					
					for h in range(len(l_nombres)):
						
						if l_nombres[h].mostrar:
							Recargar = False
							pygame.draw.rect(pantalla, (255,255,255), (l_nombres[h].rect), 4)
							
							pygame.draw.rect(pantalla, (0,0,0), (l_nombres[h].rect_fig.x, l_nombres[h].rect_fig.y, 183, 42))
							
							pantalla.blit(l_nombres[h].dato_item, l_nombres[h].dato_item_rect)
			
			
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
					
						
					p_con_nombres = pantalla.copy()
					
					seleccionado.rect.centerx = evento.pos[0]
					seleccionado.rect.centery = evento.pos[1]

					seleccionado.dato_item_rect.centerx = evento.pos[0]
					seleccionado.dato_item_rect.centery = evento.pos[1]

					pygame.draw.rect(pantalla, (255,255,255), (seleccionado.rect.x,seleccionado.rect.y ,185, 45), 4)
					pygame.draw.rect(pantalla, (0,0,0), (seleccionado.rect.x+2, seleccionado.rect.y+2, 183, 42))
					pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
				
					
				
				
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
			
			
				for img in l_imgs_pantalla:
					if img.rect.collidepoint(evento.pos[0],evento.pos[1]):
						print('ENTRO AL IF COORD')
						print(img.nombre)
						S_nombre = pygame.mixer.Sound('Sonidos/nombres/'+img.nombre+'.wav')
						pygame.mixer.Channel(0).play(S_nombre)

			
				if botonSonido.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
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

								
				if seleccionado:
					
					index = seleccionado.rect.collidelist(l_casilleros) 
					print(index)
					print('l_casilleros.dato'+str(l_casilleros[index].dato))
					print('seleccionado.dato'+seleccionado.dato)
					
					if index != -1: 
						
						if str(l_casilleros[index].dato) == seleccionado.dato:

							puntos_etapa += 5
							puntos_total += 5
						
							pygame.mixer.Channel(0).play(S_Correcto)
							print('colisiono')
							#seleccionado.set_x(l_casilleros[index].get_x())
							#seleccionado.set_y(l_casilleros[index].get_y())
							
							seleccionado.dato_item_rect.centerx = l_casilleros[index].rect.centerx
							seleccionado.dato_item_rect.centery = l_casilleros[index].rect.centery
							
							pantalla.blit(p_sin_nombres, (0,0))
							
							pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
							
							p_sin_nombres = pantalla.copy()
							
							pantalla.blit(p_con_nombres, (0,0))
							
							pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
							
							seleccionado = None
															
							if(Recargar):
								pantalla.blit(p_base, (0,0))
								if l_imagenes:
									if puntos_etapa == 20:
										puntos_total += 10
										puntos_etapa = 0
									ev_enSuLugar = pygame.event.Event(CARGARENSULUGAR)
									pygame.event.post(ev_enSuLugar)
								else:
									ev_terminado = pygame.event.Event(JUEGOTERMINADO, pts= puntos_total)
									pygame.event.post(ev_terminado)
							
							
						elif l_casilleros[index].dato != seleccionado.dato:
							pygame.mixer.Channel(0).play(S_Incorrecto)
							l_nombres[i_obj].mostrar = True
							pantalla.blit(p_con_nombres, (0,0))
							### VOLVER A SU LUGAR ###
							seleccionado.rect.centerx = copia_x
							seleccionado.rect.centery = copia_y
							seleccionado.dato_item_rect.centerx = copia_x
							seleccionado.dato_item_rect.centery = copia_y											
							pygame.draw.rect(pantalla, (255,255,255), (seleccionado.rect), 4)
							pygame.draw.rect(pantalla, (0,0,0), (seleccionado.rect.x+2, seleccionado.rect.y+2, 182, 42))
							pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
							if puntos_total > 0:
								puntos_etapa -= 2
								puntos_total -= 2 

					else:		
						l_nombres[i_obj].mostrar = True
						pantalla.blit(p_con_nombres, (0,0))
						### VOLVER A SU LUGAR ###
						seleccionado.rect.centerx = copia_x
						seleccionado.rect.centery = copia_y
						seleccionado.dato_item_rect.centerx = copia_x
						seleccionado.dato_item_rect.centery = copia_y											
						pygame.draw.rect(pantalla, (255,255,255), (seleccionado.rect), 4)
						pygame.draw.rect(pantalla, (0,0,0), (seleccionado.rect.x+2, seleccionado.rect.y+2, 182, 42))
						pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
					


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
				
				pantalla.blit(p_con_nombres, (0,0))
				
				seleccionado.rect.centerx = evento.pos[0]
				seleccionado.rect.centery = evento.pos[1]
				
				seleccionado.dato_item_rect.centerx = evento.pos[0]
				seleccionado.dato_item_rect.centery = evento.pos[1]
				
				pygame.draw.rect(pantalla, (255,255,255), (seleccionado.rect.x,seleccionado.rect.y ,185, 45), 4)
				pygame.draw.rect(pantalla, (0,0,0), (seleccionado.rect.x+2, seleccionado.rect.y+2, 182, 42))
				pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
				
		principal.displayPuntaje(puntos_total)
		pygame.display.update()

