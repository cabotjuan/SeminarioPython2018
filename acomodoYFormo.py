import random, os, time, pygame, sys
from pygame.locals import *
from setup import *
from itemsJuego import *
import principal
from separasilabas import *

	
	
#def opcionSilabas(reproducirSonido)	:
	
	#######################

CARGARACOMODO = USEREVENT+1
JUEGOTERMINADO = USEREVENT+2

def main(reproducirSonido, PuntajeJuego):
	### PUNTAJE DEL JUEGO ACTUAL ###
	
	puntos_total = 0
	puntos_etapa = 0
	
	### FECHA Y HORA DE JUEGO ###
	
	PuntajeJuego['Jugado'] = time.asctime( time.localtime(time.time()) )
	
	
	botonSalir = ItemsJuegoGenerica('Imagenes/salir.png', 75, 75)
	botonSalir.setX(V_ANCHO/24)
	botonSalir.setY(V_LARGO-75)
	#pantalla.blit(botonSalir.image, botonSalir.rect)###BOTON SALIR###

	botonMusica = ItemsJuegoGenerica('Imagenes/sonido.png', 75, 75)
	botonMusica.setX(V_ANCHO-60)
	botonMusica.setY(V_LARGO-75)
	#pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###

	botonMenu = ItemsJuegoGenerica('Imagenes/inicio.png', 75, 75)
	botonMenu.setX(V_ANCHO/8)
	botonMenu.setY(V_LARGO-75)
	#pantalla.blit(botonMenu.image, botonMenu.rect)###BOTON MENU###

	botonMute = ItemsJuegoGenerica('Imagenes/mute.png', 75, 75)
	botonMute.setX(botonMusica.getX())
	botonMute.setY(botonMusica.getY())
	
	pantalla.blit(botonSalir.image, botonSalir.rect) ###BOTON SALIR###
	pantalla.blit(botonMenu.image, botonMenu.rect) ###BOTON MENU###

	if reproducirSonido:
		pantalla.blit(botonMusica.image, botonMusica.rect)###BOTON MUSICA###
		
	else:
		pantalla.blit(botonMute.image, botonMute.rect)###BOTON MUSICA###
	
	p_base= pantalla.copy()
	p_con_letras = pantalla.copy()
	botonOpcionL = ItemsJuegoGenerica('Imagenes/conLetras.png', 560, 120)
	botonOpcionL.setX(V_ANCHO/2)
	botonOpcionL.setY(V_LARGO/2)
	pantalla.blit(botonOpcionL.image, botonOpcionL.rect)###BOTON OPCION DE LETRAS###
	
	botonOpcionS = ItemsJuegoGenerica('Imagenes/conSilabas.png', 560, 120)
	botonOpcionS.setX(V_ANCHO/2)
	botonOpcionS.setY(V_LARGO/4)
	pantalla.blit(botonOpcionS.image, botonOpcionS.rect)###BOTON OPCION DE SILABAS###

	pygame.display.update()
	
	seleccionado = None
	l_items = os.listdir('Imagenes/imgsAcomodoYFormo/letras')
	l_casilleros = []
	l_dibujos=[]
	
	estado = 'elegir opcion'
	opc =''

	while True:

		Qeventos = pygame.event.get()
		for evento in Qeventos:
			
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			elif evento.type == JUEGOTERMINADO:
				PuntajeJuego['Puntos'] = evento.pts
				calificar = principal.guardarPuntaje(PuntajeJuego)
				print(calificar)
				print('Termino Acomodo y Formo')
				pantalla.blit(p_base, (0,0))
				principal.menuPrincipal(reproducirSonido)
				
			elif evento.type == CARGARACOMODO:

				l_casilleros = []
				l_dibujos=[]
				
				i= random.randrange(len(l_items))
				item = ItemsJuegoGenerica('Imagenes/imgsAcomodoYFormo/letras/'+l_items[i], 175, 175)
				item.setX(V_ANCHO/3)
				item.setY(V_LARGO/5)
				
				pantalla.blit(item.image, item.rect)
				
				if(evento.opcion == 'letras'): ### ACOMODAR LETRAS EN SU LUGAR CORRESPONDIENTE ###
					desp = 0
					
					l_letras= list(os.path.splitext(l_items[i])[0])
					### CARGA CASILLEROS VACIOS ###
					
					for g in range(len(l_letras)):
						l_letras[g] = l_letras[g].upper()
						casillero = CasilleroAcomodo(l_letras[g], V_ANCHO/8+desp, V_LARGO/2, 50, 50)
						l_casilleros.append(casillero)
						desp += 75
						
					p_casilleros_vacios = pantalla.copy()
					
					desp = 0
					
					### CARGA DIBUJOS A ARRASTRAR ###
					
					for l in range(len(l_letras)) :
						
						k = random.randrange(0, len(l_letras))
						
						item = ItemAcomodo(l_letras[k], V_ANCHO/8+desp, V_LARGO/1.5, 50, 50)	
						
						l_dibujos.append(item)
												
						desp += 75	
						del l_letras[k]

						
				elif(evento.opcion == 'silabas'): ### ACOMODAR SILABAS EN SU LUGAR CORRESPONDIENTE ###
					
					
					nombre_img = os.path.splitext(l_items[i])[0]
					silabear = silabizer()
					print(nombre_img)
					l_silabas = silabear(nombre_img)
					print(l_silabas)
					desp = 0
					for g in range(len(l_silabas)):
						l_silabas[g] = l_silabas[g]
						casillero = CasilleroAcomodo(l_silabas[g], V_ANCHO/8+desp, V_LARGO/2, 50, 50)
						l_casilleros.append(casillero)
						desp += 75
						
					p_casilleros_vacios = pantalla.copy()
					desp = 0

					for s in range (len(l_silabas)):

						k = random.randrange(0, len(l_silabas))
						#help(l_silabas[k])
						item = ItemAcomodo(str(l_silabas[k]), V_ANCHO/8+desp, V_LARGO/1.5, 50, 50)	

						l_dibujos.append(item)
												
						desp += 75	
						del l_silabas[k]
					print(l_dibujos)
				
				del l_items[i] ### CARGA DE IMAGENES DE ITEMS ###	
				
				p_con_letras = pantalla.copy()
					
			elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
				
				
				if botonOpcionL.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado == 'elegir opcion':
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/conLetrasPresionado.png', 560, 120)
					presionado.setX(botonOpcionL.getX())
					presionado.setY(botonOpcionL.getY())
					
					pantalla.blit(presionado.image, presionado.rect)
					
				
				elif botonOpcionS.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado == 'elegir opcion':
					
					presionado = ItemsJuegoGenerica('Imagenes/botones_presionados/conSilabasPresionado.png', 560, 120)
					presionado.setX(botonOpcionS.getX())
					presionado.setY(botonOpcionS.getY())
					
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
				
				### ITERO POR CADA LETRA A SELECCIONAR. ###
				
				for i in range(len(l_dibujos)):
					
					### SELECCIONO UNO ###
					if l_dibujos[i].rect.collidepoint((evento.pos[0],evento.pos[1])):
						
						print('llego')
					
						seleccionado = l_dibujos[i]
						
						ind_obj = i
						
						l_dibujos[i].mostrar = False
						
						pantalla.blit(p_casilleros_vacios, (0,0))
						
				if seleccionado:
					
					copia_x = seleccionado.dato_item_rect.centerx
					copia_y = seleccionado.dato_item_rect.centery
					
					### DIBUJO TODAS LAS LETRAS RESTANTES ###
					
					Recargar = True
					
					for h in range(len(l_dibujos)):
						
						if l_dibujos[h].mostrar:
							Recargar = False
							pygame.draw.rect(pantalla, (255,255,255), (l_dibujos[h].rect), 4)
							
							pygame.draw.rect(pantalla, (0,0,0), (l_dibujos[h].rect_fig.x, l_dibujos[h].rect_fig.y, 47, 47))
							
							pantalla.blit(l_dibujos[h].dato_item, l_dibujos[h].dato_item_rect)
							
					p_con_letras = pantalla.copy()
					
					seleccionado.rect.centerx = evento.pos[0]
					seleccionado.rect.centery = evento.pos[1]

					seleccionado.dato_item_rect.centerx = evento.pos[0]
					seleccionado.dato_item_rect.centery = evento.pos[1]

					pygame.draw.rect(pantalla, (255,255,255), (seleccionado.rect.x,seleccionado.rect.y ,50, 50), 4)
					pygame.draw.rect(pantalla, (0,0,0), (seleccionado.rect.x+2, seleccionado.rect.y+2, 47, 47))
					pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)

			elif evento.type == MOUSEBUTTONUP and evento.button == 1:
				
				if seleccionado:
					
					index = seleccionado.rect.collidelist(l_casilleros) 
					print(index)
					print('l_casilleros.dato'+str(l_casilleros[index].dato))
					print('seleccionado.dato'+seleccionado.dato)
					
					if index != -1 and str(l_casilleros[index].dato) == seleccionado.dato:

						puntos_etapa += 5
						puntos_total += 5
					
						pygame.mixer.Channel(0).play(S_Correcto)
						print('colisiono')
						#seleccionado.set_x(l_casilleros[index].get_x())
						#seleccionado.set_y(l_casilleros[index].get_y())
						
						seleccionado.dato_item_rect.centerx = l_casilleros[index].rect.centerx
						seleccionado.dato_item_rect.centery = l_casilleros[index].rect.centery
						
						pantalla.blit(p_casilleros_vacios, (0,0))
						
						pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
						
						p_casilleros_vacios = pantalla.copy()
						
						pantalla.blit(p_con_letras, (0,0))
						
						pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
						
						
						seleccionado = None
														
						if(Recargar):
							pantalla.blit(p_base, (0,0))
							if l_items:
								if puntos_etapa == 20:
									puntos_total += 10
									puntos_etapa = 0
								ev_acomodo = pygame.event.Event(CARGARACOMODO, opcion=opc)
								pygame.event.post(ev_acomodo)
							else:
								ev_terminado = pygame.event.Event(JUEGOTERMINADO, pts= puntos_total)
								pygame.event.post(ev_terminado)
						
						
					elif index != -1 and l_casilleros[index].dato != seleccionado.dato:
						pygame.mixer.Channel(0).play(S_Incorrecto)
						l_dibujos[ind_obj].mostrar = True
						pantalla.blit(p_con_letras, (0,0))
						### VOLVER A SU LUGAR ###
						seleccionado.rect.centerx = copia_x
						seleccionado.rect.centery = copia_y
						seleccionado.dato_item_rect.centerx = copia_x
						seleccionado.dato_item_rect.centery = copia_y											
						pygame.draw.rect(pantalla, (255,255,255), (seleccionado.rect), 4)
						pygame.draw.rect(pantalla, (0,0,0), (seleccionado.rect.x+2, seleccionado.rect.y+2, 47, 47))
						pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
						if puntos_total > 0:
							puntos_etapa -= 2
							puntos_total -= 2 
					else:
						
						l_dibujos[ind_obj].mostrar = True
						pantalla.blit(p_con_letras, (0,0))
						### VOLVER A SU LUGAR ###
						seleccionado.rect.centerx = copia_x
						seleccionado.rect.centery = copia_y
						seleccionado.dato_item_rect.centerx = copia_x
						seleccionado.dato_item_rect.centery = copia_y											
						pygame.draw.rect(pantalla, (255,255,255), (seleccionado.rect), 4)
						pygame.draw.rect(pantalla, (0,0,0), (seleccionado.rect.x+2, seleccionado.rect.y+2, 47, 47))
						pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
						
				elif botonOpcionL.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado == 'elegir opcion':
					
					pantalla.blit(p_base, (0,0))
					pygame.display.update()
					
					estado = 'elegida'
					opc ='letras'
					ev_acomodo = pygame.event.Event(CARGARACOMODO, opcion=opc)
					pygame.event.post(ev_acomodo)	
					
					#### IR A MODULO DE JUGAR CON LETRAS ####
					
				elif botonOpcionS.rect.collidepoint(evento.pos[0],evento.pos[1]) and estado == 'elegir opcion':
					
					pantalla.blit(p_base, (0,0))
					pygame.display.update()
					estado = 'elegida'
					opc ='silabas'
					ev_acomodo = pygame.event.Event(CARGARACOMODO, opcion=opc)
					pygame.event.post(ev_acomodo)	
					
					#### IR A MODULO DE JUGAR CON SILABAS ####
					
				elif botonMusica.rect.collidepoint(evento.pos[0],evento.pos[1]) and reproducirSonido:
					pygame.mixer.Channel(0).set_volume(0)
					pantalla.blit(botonMute.image, botonMute.rect)
					reproducirSonido = False
					
				elif botonMute.rect.collidepoint(evento.pos[0],evento.pos[1])and not reproducirSonido:
					pygame.mixer.Channel(0).set_volume(1)
					pantalla.blit(botonMusica.image, botonMusica.rect)
					reproducirSonido = True

				
				elif botonSalir.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					terminarPrograma()
				
				elif botonMenu.rect.collidepoint(evento.pos[0],evento.pos[1]):
					
					pantalla.blit(p_base, (0,0))
					pygame.display.update()
					
					principal.menuPrincipal(reproducirSonido)
					
				seleccionado = None
				
			elif evento.type == MOUSEMOTION and seleccionado:
				
				
				pantalla.blit(p_con_letras, (0,0))
		
				seleccionado.rect.centerx = evento.pos[0]
				seleccionado.rect.centery = evento.pos[1]
				
				seleccionado.dato_item_rect.centerx = evento.pos[0]
				seleccionado.dato_item_rect.centery = evento.pos[1]
				
				pygame.draw.rect(pantalla, (255,255,255), (seleccionado.rect.x,seleccionado.rect.y ,50, 50), 4)
				pygame.draw.rect(pantalla, (0,0,0), (seleccionado.rect.x+2, seleccionado.rect.y+2, 47, 47))
				pantalla.blit(seleccionado.dato_item, seleccionado.dato_item_rect)
				
		principal.displayPuntaje(puntos_total)
		pygame.display.update()
	
	
#if __name__ == '__main__':
	#pygame.init()
	#main(sys.argv[0])
