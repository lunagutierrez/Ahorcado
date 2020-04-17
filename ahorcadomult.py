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
    

    print("Primero va a adivinar " + user1 + " la palabra que escoja " + user2)
#esperar un segundo
    time.sleep(1)
    
    def game():
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
                
        print (user1 + " deja de mirar la pantalla mientras " + user2 + " digita la palabra que vas a adivinar")
                
        def palabra1():
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
                
        word = palabra1()
        time.sleep(0.5)
        print('\n' * 60)
        turnos = 5
        print("Tienes", turnos, "intentos")

        time.sleep(0.5)
        print("Es hora de empezar el juego")
        time.sleep(0.5)

#establecemos la palabra


#creamos la variable de guesses vacia 
        guesses = ''
        
#determinamos la palabra y el numero de turnos 
        
# ciclo while 

#cmientras hayan turnos se ejecuta la funcion
        while turnos > 0:         

    # contados desde 0
            failed = 0             
            
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
                    

    # si no hay fallas

    # Gano!
            if failed == 0:        
                print ("¡Adivinaste!")  

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
            
        puntaje1 = turnos * lev * 10
    
    
        time.sleep(0.5)
        print('\n' * 60)
    
        print("Ahora " + user2 + " va a adivinar la palabra que escoja " + user1)
        print("")
        print (user2 + " deja de mirar la pantalla mientras " + user1 + " digita la palabra que vas a adivinar")

   
        def palabra2():
            while True:  
                word = input("escribe una palabra en minusula de la longitud del nivel de dificultad escogido ")
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

        
        word = palabra2()
        time.sleep(0.5)
        print('\n' * 60)
        turnos = 5
        print("Tienes", turnos, "intentos")

        time.sleep(0.5)
        print("Es hora de empezar el juego")
        time.sleep(0.5)

#establecemos la palabra


#creamos la variable de guesses vacia 
        guesses = ''
#determinamos la palabra y el numero de turnos 
        
# ciclo while 

#cmientras hayan turnos se ejecuta la funcion
        while turnos > 0:         

    # contados desde 0
            failed = 0             
            
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
                    
    # si no hay fallas

    # Gano!
            if failed == 0:        
                print ("¡Adivinaste!")  

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
                    
        puntaje2 = turnos * lev * 10
             
        if puntaje1 < puntaje2:
           print(user2 + " ha ganado la partida con un puntaje de {0}".format(puntaje2),", mientras que " + user1 + " solo ha obtenido {0} puntos.".format(puntaje1))
        elif puntaje2 < puntaje1:
            print(user1 + " ha ganado la partida con un puntaje de {0}".format(puntaje1),", mientras que " + user2 + " solo ha obtenido {0} puntos.".format(puntaje2))
        else:
            print ("Ha habido un empate, ambos jugadores han obtenido un puntaje de {0}".format(puntaje1))
            
    
    game()

setup_mult()
