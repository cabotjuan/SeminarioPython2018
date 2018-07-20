import pygame
from itemsJuego import *
from setup import *




itemFondo = ItemsJuegoGenerica('Imagenes/Fondo.jpg', V_ANCHO, V_LARGO)
itemFondo.setX(V_ANCHO/2)
itemFondo.setY(0)

pantalla.blit (itemFondo.image, itemFondo.rect)
pygame.display.update()


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

botonMute = ItemsJuegoGenerica('Imagenes/mute.png', 75, 75)
botonMute.setX(botonMusica.getX())
botonMute.setY(botonMusica.getY())
