import random, os, time, pygame, sys
from pygame.locals import *
from setup import *



class ItemsJuego(pygame.sprite.Sprite):
	def __init__(self, img, vocal):
		super().__init__()
		img = pygame.image.load(img)
		self.image = pygame.transform.scale(img, (100, 100))
		self.vocal = vocal
		self.rect = self.image.get_rect()
		
	def getX(self):
		return self.rect.x
	
	def setX(self, x):
		self.rect.x = x
	
	def getY(self):
		return self.rect.y
	
	def setY(self, y):
		self.rect.y = y

CANT_IMAGENES_PANTALLA = 4

###	CARGAR SPRITES DE LAS VOCALES.

def cargarSpriteVocales(G_Vocales):
	despl_x = 10
	for imgVocal in os.listdir('Imagenes/vocales'):
		nuevoItem = ItemsJuego('Imagenes/vocales/'+imgVocal, imgVocal[0])
		despl_x += V_ANCHO / 6
		nuevoItem.setX(x)
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
		nuevoItem.setX(x)
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
	
	## LOOP PRINCIPAL
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		


if __name__ == '__main__':
	main()
