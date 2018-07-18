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
	# MAIN LOOP 
	
	#fuente = pygame.font.Font(None, 32)
	#t_titulo = 'Comenzar a jugar'
	#titulo = fuente.render(t_titulo, True, pygame.Color("pink"))
	
	#titulo_rect = titulo.get_rect()
	
	#titulo_rect.centerx = pantalla.get_rect().centerx
	
	#pantalla.blit(titulo, titulo_rect)
	
	estado_menu = 'principal'
	
	p_base= pantalla.copy()
	
	botonJugar = ItemsJuegoGenerica('Imagenes/Jugar.png', 250, 75)
	botonJugar.rect.center = (V_ANCHO/2, V_LARGO/2)
	
	pantalla.blit(botonJugar.image, botonJugar.rect)
	
	botonPuntos = ItemsJuegoGenerica('Imagenes/misPuntos.png', 250, 75)
	botonPuntos.rect.center = (V_ANCHO/2, V_LARGO/1.5)
	
	pantalla.blit(botonPuntos.image, botonPuntos.rect)
	
	pygame.display.update()
	
	print(pygame.display.Info().current_h)
	
	l_botones_juegos = cargarMenuJugar()
	p_menuP = pantalla.copy()
	 
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
				
					pygame.display.update()
					
				
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
					
				elif estado_menu == 'principal': 
					#Reestablecer botones cuando se presiona pero se cancela...
					pantalla.blit(p_menuP, (0,0))
				elif estado_menu == 'jugar':
					pantalla.blit(p_jugar, (0,0))
				pygame.display.update()
					

def main():
	pygame.init()
	menuPrincipal()
	
def terminarPrograma():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
    main()
