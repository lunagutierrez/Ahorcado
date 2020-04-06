# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:00:26 2020

@author: lunag
"""
#importar time
import time
import palabras
import random 
#import random

#Bienvenida

def setup_ind():
    user = input("¿Nombre de usuario? ")

    print ("Hola, " + user, "Juguemos ahorcado!")
    

#esperar un segundo
    time.sleep(1)

    def lev():
        while True:
            lev = int(input("Escoge un nivel de dificultad entre 3 y 6: "))  
            try:
                if 3 <= lev <= 6:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    break
                else:
                    print('{0} is not between 4 and 16'.format(lev))
            except ValueError:
                print('{0} is not an integer between 4 and 16'.format(lev))
                
    lev()
    
                
    time.sleep(0.5)

    turnos = 5
    print("Tienes", turnos, "intentos")

    time.sleep(0.5)
    print ("Ya puedes comenzar a adivinar")
    time.sleep(0.5)

#establecemos la palabra
    
    def len_word(lev):
        for lev in range(3,7):
            if lev == 3:
                w = palabras.pal3
                break 
            elif lev == 4:
                w = palabras.pal4
                break    
            elif lev == 5:
                w = palabras.pal5
                break    
            elif lev == 6:
                w = palabras.pal6
                break
            else:
                print("No es valido el nivel de dificultad escogido")

        word = w[random.randint(0, 46)]
        return word

#creamos la variable de guesses vacia 
    guesses = ''

#determinamos la palabra y el numero de turnos 
    word = len_word(lev)
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
                print ("Perdiste")


setup_ind()
