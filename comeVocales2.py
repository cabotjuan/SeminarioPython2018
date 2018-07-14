import random, os, time, pygame, sys
from pygame.locals import *
from setup import *
from itemsJuego2 import *



CANT_IMAGENES_PANTALLA = 4

###	CARGAR IMG DE LAS VOCALES.

def cargarVocales(L_Vocales):
	despl_x = 10
	for imgVocal in os.listdir('Imagenes/vocales'):
		nuevoItem = ItemsJuego('Imagenes/vocales/'+imgVocal, imgVocal[0])
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
		nuevoItem = ItemsJuego('Imagenes/comienzanConVocal/'+img, img[0])
		despl_x += V_ANCHO / 6
		nuevoItem.setX(despl_x)
		nuevoItem.setY(V_LARGO/3)		
		L_Objetos.append(nuevoItem)
		pantalla.blit(nuevoItem.image, nuevoItem.rect)
		del L_img[i]

def main():
	fin_juego = False
	L_img = os.listdir('Imagenes/comienzanConVocal')
	
	L_Vocales = []
	L_Objetos = []
	
	cargarVocales(L_Vocales)
	cargarObjetos(L_Objetos, L_img)
	pygame.display.update()
	seleccionado = None
	## LOOP PRINCIPAL
	while True:
		Qeventos = pygame.event.get()
		for evento in Qeventos:
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				if L_Objetos[0].rect.collidepoint((evento.pos[0],evento.pos[1])):
					seleccionado = L_Objetos[0]
				if L_Objetos[1].rect.collidepoint((evento.pos[0],evento.pos[1])):
					seleccionado = L_Objetos[1]
				if L_Objetos[2].rect.collidepoint((evento.pos[0],evento.pos[1])):
					seleccionado = L_Objetos[2]
				if L_Objetos[3].rect.collidepoint((evento.pos[0],evento.pos[1])):
					seleccionado = L_Objetos[3]
				print('se selecciono obj')
					
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
				seleccionado = None
				
				print('se levanta el mouse')
				
			elif evento.type == MOUSEMOTION and seleccionado:
				seleccionado.rect.centerx = evento.pos[0]
				seleccionado.rect.centery = evento.pos[1]
				pantalla.blit(seleccionado.image, seleccionado.rect)
				print('x'+str(seleccionado.getX())+'y'+str(seleccionado.getY()))
				print('arrastrando..')
		pygame.display.update()
		

if __name__ == '__main__':
	main()

