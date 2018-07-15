import pygame
from pygame.locals import *

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
		#self.rect = self.image.get_rect()
		
		
	#def getX(self):
		#return self.rect.centerx
	
	#def setX(self, x):
		#self.rect.centerx = x
	
	#def getY(self):
		#return self.rect.y
	
	#def setY(self, y):
		#self.rect.y = y
		
