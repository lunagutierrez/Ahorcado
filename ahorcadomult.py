# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:04:53 2020
@author: lunag
"""

import time
import turtle
import dibujo
import winsound
import ahorcadoind
import pygame
pygame.init()

#Crear la pantalla
win=pygame.display.set_mode((1200,800))

#Nombre de la pantalla
pygame.display.set_caption("Ahorcado")
#icon = pygame.image.load('logo.png')
#pygame.display.set_icon(icon)
fontTitle= pygame.font.Font ('freesansbold.ttf', 60) #fuente y tamaño del texto GRANDE
fontBody= pygame.font.Font('freesansbold.ttf', 32) #fuente y tamaño del texto MEDIO
    #fontLittle= pygame.font.Font('freesansbold.ttf', 20) #fuente y tamaño del texto PEQUEÑO


class palabras: #clase de palabras que permite escribir la palabra a adivinar tomando en cuenta el nivel de dificultad escogido
    def palabra(lev):
            while True:  
                word = input("Escribe una palabra en minusula de la longitud del nivel de dificultad escogido ")
                try:
                    if not word.isalpha():
                        win.blit(fontBody.render("Los caracteres de tu palabra solo pueden ser letras.", 0,(255, 255, 255)),(50,480))
                        pygame.display.update()
                    elif lev != len(word):
                        win.blit(fontBody.render("Tu palabra debe ser de la longitud del nivel de dificultad escogido", 0,(255, 255, 255)), (50,480))
                    else:
                        return word
                        break
                except:
                    win.blit(fontBody.render('Lo digitado no es valido', 0,(255, 255, 255)), (50,480))   


#Bienvenida
def setup_mult():
    user1 = input("¿Nombre de usuario jugador 1? ")
    user2 = input("¿Nombre de usuario jugador 2? ")
    
    #bienvenida
    win.blit(fontTitle.render("Hola, " + user1 + " y " + user2 + " Juguemos ahorcado!", 0,(0, 128, 128)), (50,80))
    pygame.display.update()

    win.blit(fontTitle.render("Primero va a adivinar " + user1 + " la palabra que escoja " + user2, 0,(0, 128, 128)), (50,80))
#esperar un segundo
    time.sleep(1)
    
           
    
    t=turtle.Turtle()
    #Creamos la ventana del juego en turtle
    dibujo.Tortuga.Ventana(t)
    
    #ciclo while para determinar el nivel de dificultad y por ende la longitud de las palabras a adivinar
    while True: 
        lev = int(input("Escojan un nivel de dificultad entre 3 y 10: "))
        try:
            if 3 <= lev <= 10:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                break
            else:
                print('{0} no esta entre 3 y 10'.format(lev))
        
        except:
            print('{0} no es un entero entre 3 y 10'.format(lev))
                
        
    print ("\n" + user1 + " deja de mirar la pantalla mientras " + user2 + " digita la palabra que vas a adivinar")   
       
    #usamos la clase palabras con el nivel escogido en el ciclo while de lev previo 
    #el jugador 2 digita la palabra a adivinar
    word = palabras.palabra(lev)
    time.sleep(0.5)
    print('\n' * 60)
    winsound.PlaySound("audioahorcado.wav", winsound.SND_ASYNC) #El jugador que adivina es advertido que puede mirar la pantalla
    turnos = 6 #ls turnos iniciales son establecidos
    print("Tienes", turnos, "intentos")

    time.sleep(0.5)
    print("Es hora de empezar el juego")
    time.sleep(0.5)
    ta = time.process_time()
    #usamos la clase de la modalidad individual
    #calculamos el puntaje como el producto de los turnos restantes y el nivel de dificultad*10
    puntaje1 = int(ahorcadoind.Adivinar.desarrollo(turnos,word)) * lev * 10 #toma el valor (int) de los turnos 
    tb = time.process_time() 
    t1 = tb - ta #el tiempo que le toma al jugador1 adivinar 
    
  #segunda ronda  
    time.sleep(0.5)
    print('\n' * 60)
    print("Ahora " + user2 + " va a adivinar la palabra que escoja " + user1)
    print("")
    print (user2 + " deja de mirar la pantalla mientras " + user1 + " digita la palabra que vas a adivinar")
        
        
    #usamos la clase palabras con el nivel escogido en el ciclo while de lev previo 
    #el jugador 1 digita la palabra a adivinar
    word = palabras.palabra(lev)
    time.sleep(0.5)
    print('\n' * 60)
    winsound.PlaySound("audioahorcado.wav", winsound.SND_ASYNC) #se puede volver a ver la pantalla
    turnos = 6
    print("Tienes", turnos, "intentos")

    time.sleep(0.5)
    print("Es hora de empezar el juego")
    time.sleep(0.5)
    tc = time.process_time()
#establecemos la palabra
        
    td = time.process_time()     
    #calculamos el puntaje como el producto de los turnos restantes y el nivel de dificultad*10
    puntaje2=int(ahorcadoind.Adivinar.desarrollo(turnos,word))*lev*10     #toma el valor (int) de los turnos          
    t2 = td - tc #el tiempo que le toma al jugador2 adivinar
        
    
    #se comparan los puntajes para determinar el ganador
    if puntaje1 < puntaje2:
        print(user2 + " ha ganado la partida con un puntaje de {0}".format(puntaje2),", mientras que " + user1 + " solo ha obtenido {0} puntos.".format(puntaje1))
    elif puntaje2 < puntaje1:
        print(user1 + " ha ganado la partida con un puntaje de {0}".format(puntaje1),", mientras que " + user2 + " solo ha obtenido {0} puntos.".format(puntaje2))
    elif puntaje1 == 0 and puntaje2 == 0:
        print("Ninguno de ustedes logró adivinar las palabras. No hay un ganador")
    else:
        print ("Ambos jugadores han obtenido un puntaje de {0}".format(puntaje1)) #en caso de empate, gana quien haya tardado el menor tiempo
        if t1 < t2:
            print(user1 + " Ha ganado pues ha adivinado en un menor tiempo")
        elif t2 < t1:
            print(user2 + " Ha ganado pues ha adivinado en un menor tiempo")
        else:
            print("Ha habido un empate")
             
# Cerrar la ventana de turtle
    dibujo.Tortuga.fin()           
    
