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

class palabras:
    def palabra(lev):
            while True:  
                word = input("Escribe una palabra en minusula de la longitud del nivel de dificultad escogido ")
                try:
                    if not word.isalpha():
                        print("Los caracteres de tu palabra solo pueden ser letras.")
                    elif lev != len(word):
                        print("Tu palabra debe ser de la longitud del nivel de dificultad escogido")
                    else:
                        return word
                        break
                except ValueError:
                    print('Lo digitado no es valido')
    

#import random

#Bienvenida
def setup_mult():
    user1 = input("¿Nombre de usuario jugador 1? ")
    user2 = input("¿Nombre de usuario jugador 2? ")
    
    print ("Hola, " + user1 + " y " + user2 + " Juguemos ahorcado!")
    

    print("Primero va a adivinar " + user1 + " la palabra que escoja " + user2)
#esperar un segundo
    time.sleep(1)
    
           
    def game():
        t=turtle.Turtle()
        dibujo.Tortuga.Ventana(t)
        while True: 
            lev = int(input("Escojan un nivel de dificultad entre 3 y 10: "))
            try:
                if 3 <= lev <= 10:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    break
                else:
                    print('{0} no esta entre 3 y 10'.format(lev))
            except ValueError:
                print('{0} no es un entero entre 3 y 10'.format(lev))
                
        
        print ("\n" + user1 + " deja de mirar la pantalla mientras " + user2 + " digita la palabra que vas a adivinar")   
        
        word = palabras.palabra(lev)
        time.sleep(0.5)
        print('\n' * 60)
        winsound.PlaySound("audioahorcado.wav", winsound.SND_ASYNC)
        turnos = 6
        print("Tienes", turnos, "intentos")

        time.sleep(0.5)
        print("Es hora de empezar el juego")
        time.sleep(0.5)
        ta = time.process_time()

        ahorcadoind.Adivinar.desarrollo(turnos,word)
        
        # Perdio!
        
        tb = time.process_time() 
        puntaje1 = turnos * lev * 10
        t1 = tb - ta
    
        time.sleep(0.5)
        print('\n' * 60)
    
        print("Ahora " + user2 + " va a adivinar la palabra que escoja " + user1)
        print("")
        print (user2 + " deja de mirar la pantalla mientras " + user1 + " digita la palabra que vas a adivinar")
        
        

        word = palabras.palabra(lev)
        time.sleep(0.5)
        print('\n' * 60)
        winsound.PlaySound("audioahorcado.wav", winsound.SND_ASYNC)
        turnos = 6
        print("Tienes", turnos, "intentos")

        time.sleep(0.5)
        print("Es hora de empezar el juego")
        time.sleep(0.5)
        tc = time.process_time()
#establecemos la palabra
        
        
        ahorcadoind.Adivinar.desarrollo(turnos,word)
        
        td = time.process_time()     
        puntaje2=turnos*lev*10              
        t2 = td - tc
             
        if puntaje1 < puntaje2:
           print(user2 + " ha ganado la partida con un puntaje de {0}".format(puntaje2),", mientras que " + user1 + " solo ha obtenido {0} puntos.".format(puntaje1))
        elif puntaje2 < puntaje1:
            print(user1 + " ha ganado la partida con un puntaje de {0}".format(puntaje1),", mientras que " + user2 + " solo ha obtenido {0} puntos.".format(puntaje2))
        else:
            print ("Ambos jugadores han obtenido un puntaje de {0}".format(puntaje1))
            if t1 < t2:
                print(user1 + " Ha ganado pues ha adivinado en un menor tiempo")
            elif t2 < t1:
                print(user2 + " Ha ganado pues ha adivinado en un menor tiempo")
            else:
                print("Ha habido un empate")
# Cerrar la ventana de turtle
        dibujo.Tortuga.fin()           
    
    game()

