import pygame
from pygame.locals import *

class itemAcomodo():
	def __init__(self, img, esc_x, esc_y):		
		self.escX = esc_x
		self.escY = esc_y
		img = pygame.image.load(img)
		self.imagen = pygame.transform.scale(img, (self.escX, self.escY))
		self.rectImagen = self.image.get_rect()

				
