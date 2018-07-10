import pygame
from pygame.locals import *

class ItemsJuego(pygame.sprite.Sprite):
	def __init__(self, img, vocal):
		super().__init__()
		img = pygame.image.load(img)
		self.image = pygame.transform.scale(img, (100, 100))
		self.vocal = vocal
		self.rect = self.image.get_rect()
		
	def getX(self):
		return self.rect.centerx
	
	def setX(self, x):
		self.rect.centerx = x
	
	def getY(self):
		return self.rect.y
	
	def setY(self, y):
		self.rect.y = y
