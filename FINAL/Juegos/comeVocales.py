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

import random, os, time, pygame, sys, json
from pygame.locals import *
from Juegos.setup import *
from Juegos.itemsJuego import *
from principal import *



CANT_IMAGENES_PANTALLA = 4

JUEGOTERMINADO = USEREVENT + 2

###	CARGAR IMG DE LAS VOCALES.

def cargarVocales(L_Vocales):
	""" Se cargan las imagenes de las vocales en una Lista de objetos ItemsJuego(). """
	despl_x = 10
	for imgVocal in os.listdir('Imagenes/vocales'):
		
		nuevoItem = ItemsJuego('Imagenes/vocales/'+imgVocal, imgVocal[0], 125, 125)
		despl_x += V_ANCHO / 6
		
		nuevoItem.setX(despl_x)
		nuevoItem.setY(V_LARGO - 200)

		L_Vocales.append(nuevoItem)
		pantalla.blit(nuevoItem.image, nuevoItem.rect)
		
		
## CARGAR LA IMG DE LOS OBJETOS A ARRASTRAR.
def cargarObjetos(L_Objetos, L_img):
	
	""" Se cargan las imagenes de los objetos a arrastrar. se guardan en una Lista de objetos ItemsJuego(). """
	
	despl_x = 10
	
	for j in range(CANT_IMAGENES_PANTALLA):
		
		i = random.randrange(0, len(L_img))
		img = L_img[i]
		nuevoItem = ItemsJuego('Imagenes/comienzanConVocal/'+img, img[0], 125,125)
		despl_x += V_ANCHO / 5
		
		nuevoItem.setX(despl_x)
		nuevoItem.setY(V_LARGO/4) ####CAMBIE DE 3 A 4		

		L_Objetos.append(nuevoItem)
		#pantalla.blit(nuevoItem.image, nuevoItem.rect)
		
		del L_img[i]

def main(reproducirSonido, PuntajeJuego, reproducirMusica):

	""" Come Vocales. Se Inicializan puntajes, se carga: carteles, botones de display, imagenes de Vocales y objetos a arrastrar. """

	### PUNTAJE DEL JUEGO ACTUAL ###
	
	puntos_total = 0
	puntos_etapa = 0
	
	### FECHA Y HORA DE JUEGO ###
	
	PuntajeJuego['Jugado'] = time.asctime( time.localtime(time.time()) )
	

	fondo_t = pygame.draw.rect(pantalla, (0,0,0), (V_ANCHO - 350, 20, 350, 120), 4)
	fuente = pygame.font.Font("Fuentes/Gaegu-Regular.ttf", 28)
	t = fuente.render('ARRASTRA LAS IMAGENES', True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.centerx = fondo_t.centerx
	t_rect.centery = fondo_t.y + 30
	pantalla.blit(t, t_rect)
	t = fuente.render('A SUS VOCALES INCIALES', True, pygame.Color("white"))
	t_rect = t.get_rect()
	t_rect.centerx = fondo_t.centerx
	t_rect.centery = fondo_t.y + 70
	pantalla.blit(t, t_rect)
	p_base = pantalla.copy()
	seleccionado = None
	
	### CARGA DE BOTONES DISPLAY ###
	
	botonSalir = ItemsJuegoGenerica('Imagenes/salir.png', 75, 75)
	botonSalir.setX(V_ANCHO/24)
	botonSalir.setY(V_LARGO-75)
	pantalla.blit(botonSalir.image, botonSalir.rect)###BOTON SALIR###
	
	botonSonido = ItemsJuegoGenerica('Imagenes/sonido.png', 75, 75)
	botonSonido.setX(V_ANCHO-60)
	botonSonido.setY(V_LARGO-75) ###BOTON MUSICA###


	botonMenu = ItemsJuegoGenerica('Imagenes/inicio.png', 75, 75)
	botonMenu.setX(V_ANCHO/8)
	botonMenu.setY(V_LARGO-75)
	pantalla.blit(botonMenu.image, botonMenu.rect)###BOTON MENU###
	
	botonMute = ItemsJuegoGenerica('Imagenes/mute.png', 75, 75)
	botonMute.setX(botonSonido.getX())
	botonMute.setY(botonSonido.getY())
	
	if reproducirSonido:
		pantalla.blit(botonSonido.image, botonSonido.rect) ### BOTON MUSICA ###		
	else:
		pantalla.blit(botonMute.image, botonMute.rect) ### BOTON MUTE ###
		
		
	botonMusica = ItemsJuegoGenerica('Imagenes/musica.png', 75, 75)
	botonMusica.setX(V_ANCHO-140)
	botonMusica.setY(V_LARGO-75)
	
	botonMusicaMute = ItemsJuegoGenerica('Imagenes/musicaMute.png', 75, 75)
	botonMusicaMute.setX(V_ANCHO-140)
	botonMusicaMute.setY(V_LARGO-75)
	
	if reproducirMusica:
		pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###
		#pygame.mixer.music.play()
		
	else:
		pantalla.blit(botonMusicaMute.image, botonMusicaMute.rect)###BOTON MUSICA###
		#pygame.mixer.music.pause()

	### CARGA DE VOCALES EN PANTALLA ###
	
	L_Vocales = []
	cargarVocales(L_Vocales)
	p_base_vocales = pantalla.copy()
	
	### CARGA DE OBJETOS A ARRASTRAR ###
	
	L_Objetos = []
	L_img = os.listdir('Imagenes/comienzanConVocal')
	cargarObjetos(L_Objetos, L_img)
	for i in range(len(L_Objetos)):
		pantalla.blit(L_Objetos[i].image, L_Objetos[i].rect)
	p_conObj = pantalla.copy()	

	
	### LOOP PRINCIPAL ###
	#displayPuntaje(puntos_total)
	
	while True:
		displayPuntaje(puntos_total)
	
		Qeventos = pygame.event.get()
		for evento in Qeventos:
			
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
				
			elif evento.type == JUEGOTERMINADO:
				### PANTALLA DE FINALIZADO ###
				PuntajeJuego['Puntos'] = evento.pts
				calificar = guardarPuntaje(PuntajeJuego)
				print(calificar)
				print(evento.pts)
				calificacionImg = pygame.image.load('Imagenes/'+calificar+'.png')
				calificacionImgRect = calificacionImg.get_rect()
				calificacionImgRect.center = (V_ANCHO/2, V_LARGO/2)
				pantalla.blit(calificacionImg, calificacionImgRect)
				pygame.display.update()
				pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sonidos/Terminado.wav'))
				pygame.time.delay(3000)
				pantalla.blit(p_base, (0,0))
				menuPrincipal(reproducirSonido, reproducirMusica)
				
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				
				
				for i in range(0, len(L_Objetos)):
					
					if L_Objetos[i].rect.collidepoint((evento.pos[0],evento.pos[1])):
						seleccionado = L_Objetos[i]
						print(seleccionado.nombre)
						ind_obj = i
					
				if seleccionado:
					copia_x = seleccionado.getX()
					copia_y = seleccionado.getY()
				
				elif botonSonido.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					
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
					
			
			
					
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
			
				if seleccionado:
					

						
					index = seleccionado.rect.collidelist(L_Vocales) 
					
					print('ANTES AL IF COORD')
					print('vocal: '+seleccionado.vocal)
					print('index: '+str(index))
					
					if index != -1:
						if L_Vocales[index].vocal == seleccionado.vocal:
							
							puntos_etapa += 5
							puntos_total += 5
							pygame.mixer.Channel(0).play(S_Correcto)
							
							del L_Objetos[L_Objetos.index(seleccionado)]
							if not L_Objetos:
								
								if puntos_etapa == 20:
									puntos_total += 10
								if not L_img:
									### JUEGO FINALIZA ###
									ev_finalizado = pygame.event.Event(JUEGOTERMINADO, pts= puntos_total)
									pygame.event.post(ev_finalizado)
								else:
									### CARGAR IMG SIG ETAPA ###
									puntos_etapa = 0
									cargarObjetos(L_Objetos, L_img)	
								
						elif  L_Vocales[index].vocal != seleccionado.vocal:
							if puntos_total > 0 :
								puntos_etapa -= 2
								puntos_total -= 2 
							pygame.mixer.Channel(0).play(S_Incorrecto)
					else:
						### LEER NOMBRE DE IMAGEN ###
						if seleccionado.getX() == copia_x and seleccionado.getY() == copia_y:
							print('ENTRO AL IF COORD')
							print(seleccionado.nombre)
							S_nombre = pygame.mixer.Sound('Sonidos/nombres/'+seleccionado.nombre+'.wav')
							pygame.mixer.Channel(0).play(S_nombre)
					
					seleccionado.setX(copia_x)
					seleccionado.setY(copia_y)
						
					
						
					pantalla.blit(p_base_vocales,(0,0))		
						
					
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
					menuPrincipal(reproducirSonido, reproducirMusica)
					
				print('se levanta el mouse')
				
				for i in range(0, len(L_Objetos)):
					
					pantalla.blit(L_Objetos[i].image, L_Objetos[i].rect)
				p_conObj = pantalla.copy()	

				seleccionado = None
				
				
			
				
			elif evento.type == MOUSEMOTION and seleccionado:
				
				pantalla.blit(p_conObj, (0,0))
				seleccionado.rect.centerx = evento.pos[0]
				seleccionado.rect.centery = evento.pos[1]
				pantalla.blit(seleccionado.image, seleccionado.rect)
				print('arrastrando..')
				
				
			
		pygame.display.update()
