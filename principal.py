import random, time, pygame, sys, comeVocales, os
from pygame.locals import *
from setup import *
from itemsJuego import *



def cargarMenuJugar():
	
	#pygame.draw.rect(pantalla, pygame.Color("blue"), (V_ANCHO/3, V_LARGO/9 ,350, 100), 0)
	
	#pygame.draw.rect(pantalla, pygame.Color("pink"), (V_ANCHO/2.5, V_LARGO/53 ,250, 75), 0)
	
	
	
	
	l_botones =[]
	desplY = 200
	for boton in sorted(os.listdir('Imagenes/botones')):
		
		boton= ItemsJuegoGenerica('Imagenes/botones/'+boton, 250, 75)
		
		desplY += V_ANCHO / 9
		
		boton.setX(V_ANCHO/2)
		boton.setY(desplY)
		
		l_botones.append(boton)
	
	return l_botones
	
def menuPrincipal():	

	
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
	
	estado_menu = 'principal'
	
	p_base= pantalla.copy()
	
	botonJugar = ItemsJuegoGenerica('Imagenes/Jugar.png', 250, 75)
	botonJugar.rect.center = (V_ANCHO/2, V_LARGO/2) #boton de jugar
	pantalla.blit(botonJugar.image, botonJugar.rect)
	
	botonPuntos = ItemsJuegoGenerica('Imagenes/misPuntos.png', 250, 75)
	botonPuntos.rect.center = (V_ANCHO/2, V_LARGO/1.5)#boton de puntos
	pantalla.blit(botonPuntos.image, botonPuntos.rect)
	
	pygame.display.update()
	
	p_menuP = pantalla.copy()
	
	l_botones_juegos = cargarMenuJugar()
	
	
	 
	while True:
		
		presionado = None
		#Event Queue
		Qeventos = pygame.event.get()
	
		
		for evento in Qeventos:
			if evento.type == QUIT:
				terminarPrograma()
				
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				S_Click.play()
				if botonJugar.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado_menu == 'principal':
					
					presionado = ItemsJuegoGenerica('Imagenes/JugarPresionado.png', 250, 75)
					presionado.setX(botonJugar.getX())
					presionado.setY(botonJugar.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
					
				elif botonPuntos.rect.collidepoint(evento.pos[0],evento.pos[1])and estado_menu == 'principal':
					
					presionado = ItemsJuegoGenerica('Imagenes/misPuntosPresionado.png', 250, 75)
					presionado.setX(botonPuntos.getX())
					presionado.setY(botonPuntos.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
					
				
				elif l_botones_juegos[0].rect.collidepoint((evento.pos[0],evento.pos[1])):
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/comeVocalesPresionado.png', 250, 75)
					presionado.setX(l_botones_juegos[0].getX())
					presionado.setY(l_botones_juegos[0].getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
					
				elif l_botones_juegos[1].rect.collidepoint((evento.pos[0],evento.pos[1])):
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/acomodoYFormoPresionado.png', 250, 75)
					presionado.setX(l_botones_juegos[1].getX())
					presionado.setY(l_botones_juegos[1].getY())
					
					pantalla.blit(presionado.image, presionado.rect)					
					
					
				elif l_botones_juegos[2].rect.collidepoint((evento.pos[0],evento.pos[1])):
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/elEntrometidoPresionado.png', 250, 75)
					presionado.setX(l_botones_juegos[2].getX())
					presionado.setY(l_botones_juegos[2].getY())
					
					pantalla.blit(presionado.image, presionado.rect)					
					
				
				
				elif l_botones_juegos[3].rect.collidepoint((evento.pos[0],evento.pos[1])):
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/enSuLugarPresionado.png', 250, 75)
					presionado.setX(l_botones_juegos[3].getX())
					presionado.setY(l_botones_juegos[3].getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
				elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					presionado = ItemsJuegoGenerica('Imagenes/sonidoPresionado.png', 75, 75)
					presionado.setX(botonMusica.getX())
					presionado.setY(botonMusica.getY())
					
					pantalla.blit(presionado.image, presionado.rect)

				#elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					#presionado = ItemsJuegoGenerica('Imagenes/salirPresionado.png', 75, 75)
					#presionado.setX(botonSalir.getX())
					#presionado.setY(botonSalir.getY())
					
					#pantalla.blit(presionado.image, presionado.rect)
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					presionado = ItemsJuegoGenerica('Imagenes/inicioPresionado.png', 75, 75)
					presionado.setX(botonMenu.getX())
					presionado.setY(botonMenu.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
				
				pygame.display.update()
					
					
					
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
				if botonJugar.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado_menu == 'principal':
					
					
					pantalla.blit(p_base , (0,0))
					pygame.display.update()
					
					for boton in l_botones_juegos:
						pantalla.blit(boton.image, boton.rect)
						
				
					p_jugar = pantalla.copy()
					estado_menu = 'jugar'
				
				elif l_botones_juegos[0].rect.collidepoint((evento.pos[0],evento.pos[1])) and estado_menu == 'jugar' :
					pantalla.blit(p_base , (0,0))
					pygame.display.update()
					comeVocales.main()	

				#elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					######## PONER SONIDO ##########

				elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					terminarPrograma()
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					pantalla.blit(p_menuP, (0,0))
					pygame.display.update()
					
					estado_menu = 'principal'
					
				elif estado_menu == 'principal': 
					#Reestablecer botones cuando se presiona pero se cancela...
					pantalla.blit(p_menuP, (0,0))
					
				elif estado_menu == 'jugar':
					pantalla.blit(p_jugar, (0,0))
				
					
				pygame.display.update()
				
				



def main():
	pygame.init()
	menuPrincipal()
	


if __name__ == '__main__':
    main()
