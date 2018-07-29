import random, time, pygame, sys, comeVocales, acomodoYFormo, enSuLugar,os, json, bisect
from pygame.locals import *
from setup import *
from itemsJuego import *
#from cargaBotonesFijos import *


MAX_PUNTAJE = 150

reproducirSonido= True

PuntajeJuego = {
	"Juego": None,
	"Puntos": 0,
	"Jugado": None
}

def displayPuntaje(pts):
	
	img = pygame.image.load('Imagenes/displayPuntos.png')
	Surf = pygame.transform.scale(img, (200, 50))
	Surf_Vacia = Surf.copy()
	texto_puntos = ' Puntos: '+str(pts)
	fuente = pygame.font.Font(None, 48)
	puntos = fuente.render(texto_puntos, True, pygame.Color("white"))
	puntos_rect = puntos.get_rect()
	puntos_rect.topleft = pantalla.get_rect().topleft
	Surf_Vacia.blit(puntos, puntos_rect)
	pantalla.blit(Surf_Vacia, Surf_Vacia.get_rect())
	pygame.display.flip()
	
def mostrarPuntaje():
	arc_ptje = open('Puntaje.json', "r")
	dic_ptje = json.load(arc_ptje)
	desp_y = V_LARGO / 5.5
	
	for J in dic_ptje:	### ITERO ENTRE LOS 4 JUEGOS ### 
		texto_juego = J['Juego']+':  '+str(J['Puntos'])+' Puntos'
		texto_jugado = 'Jugado: '+ J['Jugado']
		fuente = pygame.font.Font(None, 40)
		juego = fuente.render(texto_juego.upper(), True, pygame.Color("white"))
		juego_rect = juego.get_rect()
		juego_rect.centerx = pantalla.get_rect().centerx
		juego_rect.y = desp_y

		jugado = fuente.render(texto_jugado.upper(), True, pygame.Color("white"))
		jugado_rect = jugado.get_rect()
		jugado_rect.centerx = pantalla.get_rect().centerx
		jugado_rect.y = desp_y + 30

		pantalla.blit(juego, juego_rect)
		pantalla.blit(jugado, jugado_rect)
		desp_y+= V_LARGO / 5.5
	
	marco = pygame.draw.rect(pantalla, (0,0,0), (100, 100, V_ANCHO - 200, V_LARGO - 200), 10)
	arc_ptje.close()

def guardarPuntaje(nuevo_ptje):
	arc_ptje = open('Puntaje.json', "r")
	dic_ptje = json.load(arc_ptje)

	for J in dic_ptje:	### ITERO ENTRE LOS 4 JUEGOS ### 
			if J['Juego'] == nuevo_ptje['Juego']:
				if nuevo_ptje['Puntos'] >= J['Puntos']:
					J['Puntos'] = nuevo_ptje['Puntos'] 
					J['Jugado'] = nuevo_ptje['Jugado'] 
					
	arc_ptje.close()			
	arc_ptje = open('Puntaje.json', "w")
	json.dump(dic_ptje, arc_ptje)
	arc_ptje.close()
		
	calificaciones  = ["Bien", "Muy Bien", "Excelente"]
	breakpoints = [0.6, 0.9]
	return calificaciones[bisect.bisect(breakpoints, MAX_PUNTAJE/nuevo_ptje['Puntos'])]

def cargarMenuJugar():
	
	#pygame.draw.rect(pantalla, pygame.Color("blue"), (V_ANCHO/3, V_LARGO/9 ,350, 100), 0)
	
	#pygame.draw.rect(pantalla, pygame.Color("pink"), (V_ANCHO/2.5, V_LARGO/53 ,250, 75), 0)
	
	
	
	
	l_botones =[]
	desplY = -50
	for boton in sorted(os.listdir('Imagenes/botones')):
		
		boton= ItemsJuegoGenerica('Imagenes/botones/'+boton, 560, 120)
		
		desplY += V_ANCHO / 7
		
		boton.setX(V_ANCHO/2)
		boton.setY(desplY)
		
		l_botones.append(boton)
	
	return l_botones
	

#def manejoBotonesFijos():



#sonido = 'ON'

		#if evento.type == QUIT:
			#terminarPrograma()

		#if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				
			#if botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and sonido == 'ON':
				
				#presionado = ItemsJuegoGenerica('Imagenes/sonidoPresionado.png', 75, 75)
				#presionado.setX(botonMusica.getX())
				#presionado.setY(botonMusica.getY())
				
				#pantalla.blit(presionado.image, presionado.rect)
				
			#elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and sonido == 'OFF':
				
				#presionado = ItemsJuegoGenerica('Imagenes/mutePresionado.png', 75, 75)
				#presionado.setX(botonMute.getX())
				#presionado.setY(botonMute.getY())
				
				#pantalla.blit(presionado.image, presionado.rect)
			
			#elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
				
				#presionado = ItemsJuegoGenerica('Imagenes/salirPresionado.png', 75, 75)
				#presionado.setX(botonSalir.getX())
				#presionado.setY(botonSalir.getY())
				
				#pantalla.blit(presionado.image, presionado.rect)
			
			#elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
				
				#presionado = ItemsJuegoGenerica('Imagenes/inicioPresionado.png', 75, 75)
				#presionado.setX(botonMenu.getX())
				#presionado.setY(botonMenu.getY())
				
				#pantalla.blit(presionado.image, presionado.rect)
	
	
		#elif evento.type == MOUSEBUTTONUP and evento.button == 1:
			
			#if botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and sonido == 'ON':
					
				#pantalla.blit(botonMute.image, botonMute.rect)
				#sonido = 'OFF'
			
			#elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and sonido == 'OFF':
					
				#pantalla.blit(botonMusica.image, botonMusica.rect)
				#sonido = 'ON'
					
				
			#elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
				
				#terminarPrograma()
		
		#pygame.display.update()
	
	#p_baseFija = pantalla.copy()
		
		
	
	

def menuPrincipal(reproducirSonido):	
	
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
	#pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###

	botonMenu = ItemsJuegoGenerica('Imagenes/inicio.png', 75, 75)
	botonMenu.setX(V_ANCHO/8)
	botonMenu.setY(V_LARGO-75)
	pantalla.blit(botonMenu.image, botonMenu.rect)###BOTON MENU###
	
	
	
	botonMute = ItemsJuegoGenerica('Imagenes/mute.png', 75, 75)
	botonMute.setX(botonMusica.getX())
	botonMute.setY(botonMusica.getY())
	p_base= pantalla.copy()
	
	if reproducirSonido:
		pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###
		
	else:
		pantalla.blit(botonMute.image, botonMute.rect)###BOTON MUSICA###
						
	#p_baseFija = pantalla.copy()
	
	estado_menu = 'principal'
	
	#p_base= pantalla.copy()
	
	botonJugar = ItemsJuegoGenerica('Imagenes/jugar.png', 560, 120)
	botonJugar.rect.center = (V_ANCHO/2, V_LARGO/2) #boton de jugar
	pantalla.blit(botonJugar.image, botonJugar.rect)
	
	botonPuntos = ItemsJuegoGenerica('Imagenes/misPuntos.png', 560, 120)
	botonPuntos.rect.center = (V_ANCHO/2, V_LARGO/1.3)#boton de puntos
	pantalla.blit(botonPuntos.image, botonPuntos.rect)
	
	pygame.display.update()
	
	p_menuP = pantalla.copy()
	
	l_botones_juegos = cargarMenuJugar()
	
	 
	while True:
		
		presionado = None
		#Event Queue
		Qeventos = pygame.event.get()
	
		
		for evento in Qeventos:
			
			
			#manejoBotonesFijos()
			
			if evento.type == QUIT:
				terminarPrograma()
				
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				
				
				pygame.mixer.Channel(0).play(S_Click)
				
				if botonJugar.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado_menu == 'principal':
					
					presionado = ItemsJuegoGenerica('Imagenes/jugarPresionado.png', 560, 120)
					presionado.setX(botonJugar.getX())
					presionado.setY(botonJugar.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
					
				elif botonPuntos.rect.collidepoint(evento.pos[0],evento.pos[1])and estado_menu == 'principal':
					
					presionado = ItemsJuegoGenerica('Imagenes/misPuntosPresionado.png', 560, 120)
					presionado.setX(botonPuntos.getX())
					presionado.setY(botonPuntos.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
					
				
				elif l_botones_juegos[0].rect.collidepoint((evento.pos[0],evento.pos[1])) and estado_menu == 'jugar':
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/comeVocalesPresionado.png', 560, 120)
					presionado.setX(l_botones_juegos[0].getX())
					presionado.setY(l_botones_juegos[0].getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
					
				elif l_botones_juegos[1].rect.collidepoint((evento.pos[0],evento.pos[1])) and estado_menu == 'jugar':
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/acomodoYFormoPresionado.png', 560, 120)
					presionado.setX(l_botones_juegos[1].getX())
					presionado.setY(l_botones_juegos[1].getY())
					
					pantalla.blit(presionado.image, presionado.rect)					
					
					
				elif l_botones_juegos[2].rect.collidepoint((evento.pos[0],evento.pos[1]))and estado_menu == 'jugar':
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/elEntrometidoPresionado.png', 560, 120)
					presionado.setX(l_botones_juegos[2].getX())
					presionado.setY(l_botones_juegos[2].getY())
					
					pantalla.blit(presionado.image, presionado.rect)					
					
				
				
				elif l_botones_juegos[3].rect.collidepoint((evento.pos[0],evento.pos[1]))and estado_menu == 'jugar':
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/enSuLugarPresionado.png', 560, 120)
					presionado.setX(l_botones_juegos[3].getX())
					presionado.setY(l_botones_juegos[3].getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
				elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					
					presionado = ItemsJuegoGenerica('Imagenes/sonidoPresionado.png', 75, 75)
					presionado.setX(botonMusica.getX())
					presionado.setY(botonMusica.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
				elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirSonido:
					
					presionado = ItemsJuegoGenerica('Imagenes/mutePresionado.png', 75, 75)
					presionado.setX(botonMute.getX())
					presionado.setY(botonMute.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
				elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					presionado = ItemsJuegoGenerica('Imagenes/salirPresionado.png', 75, 75)
					presionado.setX(botonSalir.getX())
					presionado.setY(botonSalir.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					presionado = ItemsJuegoGenerica('Imagenes/inicioPresionado.png', 75, 75)
					presionado.setX(botonMenu.getX())
					presionado.setY(botonMenu.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
				
				
				#pygame.display.update()
					
					
					
			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
				
				if botonJugar.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado_menu == 'principal':
					
					pantalla.blit(p_base , (0,0))
					#pygame.display.update()
					
					for boton in l_botones_juegos:
						pantalla.blit(boton.image, boton.rect)
						
				
					p_jugar = pantalla.copy()
					estado_menu = 'jugar'
				
					####CARGA DE BOTONES JUGAR####

				elif botonPuntos.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado_menu == 'principal':
					pantalla.blit(p_base , (0,0))
					mostrarPuntaje()
############					

				####ENTRADA A UN JUEGO####					
				elif l_botones_juegos[0].rect.collidepoint((evento.pos[0],evento.pos[1])) and estado_menu == 'jugar' : 
					pantalla.blit(p_base , (0,0))
					pygame.display.update()
					PuntajeJuego['Juego'] = 'Come Vocales'
					comeVocales.main(reproducirSonido, PuntajeJuego)	
					
				elif l_botones_juegos[1].rect.collidepoint((evento.pos[0],evento.pos[1])) and estado_menu == 'jugar' :
					pantalla.blit(p_base , (0,0))
					pygame.display.update()
					PuntajeJuego['Juego'] = 'Acomodo y Formo'
					acomodoYFormo.main(reproducirSonido, PuntajeJuego)	
					
				#elif l_botones_juegos[2].rect.collidepoint((evento.pos[0],evento.pos[1])) and estado_menu == 'jugar' :
					#pantalla.blit(p_base , (0,0))
					#PuntajeJuego['Juego'] = 'El Entrometido '
					#pygame.display.update()
					#elEntrometido.main(reproducirSonido, PuntajeJuego)	
				
				elif l_botones_juegos[3].rect.collidepoint((evento.pos[0],evento.pos[1])) and estado_menu == 'jugar' :
					pantalla.blit(p_base , (0,0))
					PuntajeJuego['Juego'] = 'En su Lugar'
					pygame.display.update()
					enSuLugar.main(reproducirSonido, PuntajeJuego)	

				####ENTRADA A UN JUEGO####
				
				elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					
					pantalla.blit(botonMute.image, botonMute.rect)
					reproducirSonido = False
				
				elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirSonido:
						
					pantalla.blit(botonMusica.image, botonMusica.rect)
					reproducirSonido= True
			
				elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					terminarPrograma()
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					pantalla.blit(p_menuP, (0,0))
					#pygame.display.update()
					
					estado_menu = 'principal'
					
				elif estado_menu == 'principal': 
					#Reestablecer botones cuando se presiona pero se cancela...
					pantalla.blit(p_menuP, (0,0))
				
				elif estado_menu == 'jugar':
					pantalla.blit(p_jugar, (0,0))
				
				#pygame.display.update()
				
				if reproducirSonido:
					pygame.mixer.Channel(0).set_volume(1)
					pantalla.blit(botonMusica.image, botonMusica.rect)
					#pygame.display.update(botonMusica.rect)
				else:
					pygame.mixer.Channel(0).set_volume(0)
					pantalla.blit(botonMute.image, botonMute.rect)
					#pygame.display.update(botonMute.rect)
				
			pygame.display.update()



def main():
	pygame.init()
	global reproducirSonido
	menuPrincipal(reproducirSonido)
	


if __name__ == '__main__':
    main()
