import random, os, time, pygame, sys
from pygame.locals import *
from setup import *
from itemsJuego import *



CANT_IMAGENES_PANTALLA = 4

###	CARGAR SPRITES DE LAS VOCALES.

def cargarSpriteVocales(G_Vocales):
	despl_x = 10
	for imgVocal in os.listdir('Imagenes/vocales'):
		nuevoItem = ItemsJuego('Imagenes/vocales/'+imgVocal, imgVocal[0])
		despl_x += V_ANCHO / 6
		nuevoItem.setX(despl_x)
		nuevoItem.setY(V_LARGO - 200)
		G_Vocales.add(nuevoItem)
	
## CARGAR SPRITES DE LOS OBJETOS A ARRASTRAR.
def cargarSpriteObjetos(G_Objetos, L_img):
	despl_x = 10
	for j in range(CANT_IMAGENES_PANTALLA):
		i = random.randrange(0, len(L_img)-1)
		img = L_img[i]
		nuevoItem = ItemsJuego('Imagenes/comienzanConVocal/'+img, img[0])
		despl_x += V_ANCHO / 6
		nuevoItem.setX(despl_x)
		nuevoItem.setY(V_LARGO/3)		
		G_Objetos.add(nuevoItem)
		
		del L_img[i]

def main():
	fin_juego = False
	L_img = os.listdir('Imagenes/comienzanConVocal')
	
	G_Vocales = pygame.sprite.Group()
	G_Objetos = pygame.sprite.Group()
	
	cargarSpriteVocales(G_Vocales)
	cargarSpriteObjetos(G_Objetos, L_img)
	
	G_Vocales.draw(pantalla)
	G_Objetos.draw(pantalla)
	pygame.display.update()
	
	L_Objetos = G_Objetos.sprites()
	
	## LOOP PRINCIPAL
	while True:
		Qeventos = pygame.event.get()
		for evento in Qeventos:
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			elif evento.type == MOUSEBUTTONDOWN and event.button == 1:
				if L_Objetos[0].collidepoint((event.pos[0],event.pos[1])):
					seleccionado = L_Objetos[0]
					
			elif evento.type == MOUSEBUTTONUP and event.button == 1:
				seleccionado = None
				
			elif evento.type == MOUSEMOTION and seleccionado:
				seleccionado



if __name__ == '__main__':
	main()
