# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:04:53 2020

@author: lunag
"""

import time

#import random

#Bienvenida
def setup_mult():
    user1 = input("¿Nombre de usuario jugador 1? ")
    user2 = input("¿Nombre de usuario jugador 2? ")
    print ("Hola, " + user1 + " y " + user2 + " Juguemos ahorcado!")
    

    print("Primero va a adivinar " + user2 + " la palabra que escoja " + user1)
#esperar un segundo
    time.sleep(1)
    
    lev = int(input("Escoge un nivel de dificultad entre 3 y 10: "))

    def level():
        while True:    
            try:
                if 3 <= lev <= 10:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    break
                else:
                    print('{0} no esta entre 3 y 10'.format(lev))
            except ValueError:
                print('{0} no es un entero entre 3 y 10'.format(lev))
        
    level()
    
    word = input("Escribe una palabra en minusula de la longitud del nivel de dificultad escogido ")
    
    def palabra():
        while True:  
            try:
                if not word.isalpha():
                    print("Los caracteres de tu palabra solo pueden ser letras.")
                elif lev != len(word):
                    print("Tu palabra debe ser de la longitud del nivel de dificultad escogido")
                else:
                    return word
            except ValueError:
                print('Lo digitado no es valido')
    
#    palabra()
                
    def game():
        time.sleep(0.5)

        turnos = 5
        print("Tienes", turnos, "intentos")

        time.sleep(0.5)
        print("Ahora debes escoger un nivel de dificultad")
        time.sleep(0.5)

#establecemos la palabra


#creamos la variable de guesses vacia 
        guesses = ''

#determinamos la palabra y el numero de turnos 
        word = palabra()
# ciclo while 

#cmientras hayan turnos se ejecuta la funcion
        while turnos > 0:         

    # contados desde 0
            failed = 0             
            puntaje = 100
    # para cada letra en la palabra
            for char in word:      

    # mirar si la letra esta en lo adivinado
                if char in guesses:    
    
        # imprimir el caracter
                    print (char)    

                else:
    
        # si no imprimir -
                    print ("_")     
       
        # e incrementar el numero de fallas
                    failed += 1 
                    puntaje -= 20

    # si no hay fallas

    # Gano!
            if failed == 0:        
                print ("¡Ganáste!")  

    # salir
                break              

            print

    # adivine una letra
            guess = input("Adivina una letra: ") 

# de guess a guesses
            guesses += guess                    

    # si guess no esta en palabra
            if guess not in word:  
 
     # turnos se disminuyen
                turnos -= 1        
 
    # imprima se equivoco
                print ("Te equivocaste...")    
 
    # turnos que quedan
                print ("Ahora tienes", + turnos, 'intentos')
 
    # si se queda sin turnos
                if turnos == 0:           
    
        # Perdio!
                    print ("Perdiste!")
                    print("La palabra era " +word)

    game()
                   
                
setup_mult()