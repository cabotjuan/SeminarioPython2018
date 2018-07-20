import random, os, time, pygame, sys
from pygame.locals import *
from setup import *
from itemsJuego import *
from principal import *



CANT_IMAGENES_PANTALLA = 4

###	CARGAR IMG DE LAS VOCALES.



def cargarVocales(L_Vocales):
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
	
	
	despl_x = 10
	
	for j in range(CANT_IMAGENES_PANTALLA):
		
		i = random.randrange(0, len(L_img)-1)
		img = L_img[i]
		nuevoItem = ItemsJuego('Imagenes/comienzanConVocal/'+img, img[0], 125,125)
		despl_x += V_ANCHO / 5
		
		nuevoItem.setX(despl_x)
		nuevoItem.setY(V_LARGO/4) ####CAMBIE DE 3 A 4		

		L_Objetos.append(nuevoItem)
		#pantalla.blit(nuevoItem.image, nuevoItem.rect)
		
		del L_img[i]

def main(reproducirSonido):
	
	print(reproducirSonido)
	
	p_base = pantalla.copy()
	
	#pantalla.fill((50,50,50))
	
	botonSalir = ItemsJuegoGenerica('Imagenes/salir.png', 75, 75)
	botonSalir.setX(V_ANCHO/24)
	botonSalir.setY(V_LARGO-75)
	pantalla.blit(botonSalir.image, botonSalir.rect)###BOTON SALIR###
	
	botonMusica = ItemsJuegoGenerica('Imagenes/sonido.png', 75, 75)
	botonMusica.setX(V_ANCHO-60)
	botonMusica.setY(V_LARGO-75)
	#pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###

	botonMenu = ItemsJuegoGenerica('Imagenes/inicio.png', 75, 75)
	botonMenu.setX(V_ANCHO/8)
	botonMenu.setY(V_LARGO-75)
	pantalla.blit(botonMenu.image, botonMenu.rect)###BOTON MENU###
	
	botonMute = ItemsJuegoGenerica('Imagenes/mute.png', 75, 75)
	botonMute.setX(botonMusica.getX())
	botonMute.setY(botonMusica.getY())
	
	L_Vocales = []
	cargarVocales(L_Vocales)
	
	
	
	if reproducirSonido:
		pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###
		
	else:
		pantalla.blit(botonMute.image, botonMute.rect)###BOTON MUSICA###
	
	p_base_vocales = pantalla.copy()
	fin_juego = False
	
	
	
	L_Objetos = []
	
	
	L_img = os.listdir('Imagenes/comienzanConVocal')
	
	
	
	
	
	cargarObjetos(L_Objetos, L_img)
	
	pygame.display.update()
	
	seleccionado = None
	
	for i in range(len(L_Objetos)):
	
		pantalla.blit(L_Objetos[i].image, L_Objetos[i].rect)
	
	p_conObj = pantalla.copy()	
	
	## LOOP PRINCIPAL

	if reproducirSonido:
		pygame.mixer.stop()
		pantalla.blit(botonMusica.image, botonMusica.rect)
		#pygame.display.update(botonMusica.rect)
	else:
		#pygame.mixer.unpause()
		pantalla.blit(botonMute.image, botonMute.rect)
		#pygame.display.update(botonMute.rect)
	
	while True:
		
		Qeventos = pygame.event.get()
		for evento in Qeventos:
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				
				
				for i in range(0, len(L_Objetos)):
					
					if L_Objetos[i].rect.collidepoint((evento.pos[0],evento.pos[1])):
						seleccionado = L_Objetos[i]
						ind_obj = i
					
				if seleccionado:
					copia_x = seleccionado.getX()
					copia_y = seleccionado.getY()
				#print('se selecciono obj')
				
				elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					
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
			
				if seleccionado:
				
					index = seleccionado.rect.collidelist(L_Vocales) 
					
				
					
					if index != -1 and L_Vocales[index].vocal == seleccionado.vocal:
						#===>Contar puntos aca<===
						pygame.mixer.Channel(0).play(S_Correcto)
						print ('borrado'+str(L_Objetos.index(seleccionado)))
						del L_Objetos[L_Objetos.index(seleccionado)]
						if not L_Objetos:
							cargarObjetos(L_Objetos, L_img)	
						
					else:
						pygame.mixer.Channel(0).play(S_Incorrecto)
						seleccionado.setX(copia_x)
						seleccionado.setY(copia_y)
						
					
						
					pantalla.blit(p_base_vocales,(0,0))		
						
					if reproducirSonido:
						pantalla.blit(botonMusica.image, botonMusica.rect)
						#pygame.display.update(botonMusica.rect)
					else:
						pantalla.blit(botonMute.image, botonMute.rect)
						#pygame.display.update(botonMute.rect)
					
				
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
					menuPrincipal(reproducirSonido)
					
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
		

if __name__ == '__main__':
	main(sys.argv[0])

