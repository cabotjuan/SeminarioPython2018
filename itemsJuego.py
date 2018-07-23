import pygame
from pygame.locals import *
from setup import *
class ItemsJuegoGenerica():
	
	def __init__(self, img, esc_x, esc_y):
		
		self.escX = esc_x
		self.escY = esc_y
		img = pygame.image.load(img)
		self.image = pygame.transform.scale(img, (self.escX, self.escY)) ### CAMBIE DE 100 A 125
		
		self.rect = self.image.get_rect()
		
		
		
		
	def getX(self):
		return self.rect.centerx
	
	def setX(self, x):
		self.rect.centerx = x
	
	def getY(self):
		return self.rect.y
	
	def setY(self, y):
		self.rect.y = y
		
class ItemsJuego(ItemsJuegoGenerica):
	
	def __init__(self, img, vocal, esc_x, esc_y):
		
		ItemsJuegoGenerica.__init__(self, img, esc_x, esc_y)
		
		#self.escX = esc_x
		#self.escY = esc_y
		#img = pygame.image.load(img)
		#self.image = pygame.transform.scale(img, (self.escX, self.escY)) ### CAMBIE DE 100 A 125
		self.vocal = vocal
		self.marca = True
		#self.rect = self.image.get_rect()
		
		
	#def getX(self):
		#return self.rect.centerx
	
	#def setX(self, x):
		#self.rect.centerx = x
	
	#def getY(self):
		#return self.rect.y
	
	#def setY(self, y):
		#self.rect.y = y

class CasilleroAcomodo():
	def __init__(self, dato, posX, posY):
		self.rect = pygame.draw.rect(pantalla, (255,255,255), (posX, posY, 50, 50), 4)
		self.dato = dato

class ItemAcomodo(CasilleroAcomodo):
	def __init__(self, dato, posX, posY):
		CasilleroAcomodo.__init__(self, dato, posX, posY)
		self.rect_fig = pygame.draw.rect(pantalla, (0,0,0), (posX+2, posY+2, 47, 47))			
		fuente = pygame.font.Font(None, 42)
		self.texto_dato = dato
		self.dato_item = fuente.render(self.texto_dato, True, pygame.Color("white"))
		self.dato_item_rect = self.dato_item.get_rect()
		self.dato_item_rect.centerx = self.rect.centerx
		self.dato_item_rect.centery = self.rect.centery
		
		self.mostrar = True
		
		pantalla.blit(self.dato_item, self.dato_item_rect)
		
		
		
	def set_x(self, x):
		self.dato_item_rect.x = x
	def set_y(self, y):
		self.dato_item_rect.y = y
		
	def get_x(self):
		return self.dato_item_rect.x
	def get_y(self):
		return self.dato_item_rect.y
