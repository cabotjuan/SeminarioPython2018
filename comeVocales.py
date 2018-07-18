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

def main():
	
	p_base = pantalla.copy()
	
	#pantalla.fill((50,50,50))
	
	botonSalir = ItemsJuegoGenerica('Imagenes/salir.png', 75, 75)
	botonSalir.setX(V_ANCHO/24)
	botonSalir.setY(V_LARGO-75)
	pantalla.blit(botonSalir.image, botonSalir.rect)###BOTON SALIR###
	
	botonMusica = ItemsJuegoGenerica('Imagenes/sonido.png', 75, 75)
	botonMusica.setX(V_ANCHO-60)
	botonMusica.setY(V_LARGO-75)
	pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###

	botonMenu = ItemsJuegoGenerica('Imagenes/inicio.png', 75, 75)
	botonMenu.setX(V_ANCHO/8)
	botonMenu.setY(V_LARGO-75)
	pantalla.blit(botonMenu.image, botonMenu.rect)###BOTON MENU###
	
	fin_juego = False
	
	
	L_Vocales = []
	L_Objetos = []
	
	
	L_img = os.listdir('Imagenes/comienzanConVocal')
	
	
	
	cargarVocales(L_Vocales)
	
	p_base_vocales = pantalla.copy()
	
	cargarObjetos(L_Objetos, L_img)
	
	pygame.display.update()
	
	seleccionado = None
	
	for i in range(len(L_Objetos)):
	
		pantalla.blit(L_Objetos[i].image, L_Objetos[i].rect)
	
	p_conObj = pantalla.copy()	
	
	## LOOP PRINCIPAL
	
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
						S_Correcto.play()
						print ('borrado'+str(L_Objetos.index(seleccionado)))
						del L_Objetos[L_Objetos.index(seleccionado)]
						if not L_Objetos:
							cargarObjetos(L_Objetos, L_img)	
						
					else:
						S_Incorrecto.play()
						seleccionado.setX(copia_x)
						seleccionado.setY(copia_y)
						
				pantalla.blit(p_base_vocales,(0,0))		
						
				for i in range(0, len(L_Objetos)):
					
					pantalla.blit(L_Objetos[i].image, L_Objetos[i].rect)
				p_conObj = pantalla.copy()	

				seleccionado = None
				
				
				#elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					######## PONER SONIDO ##########

				
				if botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					terminarPrograma()
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					
					
					pantalla.blit(p_base, (0,0))
					pygame.display.update()
					menuPrincipal()
					
					
			
				
				print('se levanta el mouse')
				
			elif evento.type == MOUSEMOTION and seleccionado:
				
				pantalla.blit(p_conObj, (0,0))
				seleccionado.rect.centerx = evento.pos[0]
				seleccionado.rect.centery = evento.pos[1]
				pantalla.blit(seleccionado.image, seleccionado.rect)
				print('arrastrando..')
				
				
			
		pygame.display.update()
		

if __name__ == '__main__':
	main()

