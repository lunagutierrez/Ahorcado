# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:00:26 2020

@author: lunag
"""
#importar time
import time

#Bienvenida
user = input("¿Nombre de usuario? ")

print ("Hola, " + user, "Juguemos ahorcado!")

#esperar un segundo
time.sleep(1)

lev = int(input("Escoge un nivel de dificultad entre 3 y 6: "))  
while True:
    if 3 <= lev <= 6:
        print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
    else:
        my_error = ValueError("Debes escoger un nivel entre 3 y 6")
        raise my_error
    
time.sleep(0.5)

turnos = int(lev-1)
print("Tienes", turnos, "intentos")

time.sleep(0.5)
print ("Ya puedes comenzar a adivinar")
time.sleep(0.5)

#aqui se establece la palabra
word = "python"

#creo una variable vacia 
guesses = ''

#determino los turns y creo un ciclo while

#mientras se tengan oportunidades de adivinar
while turnos > 0:         

    # contador de intentos fallidos
    fail = 0             

    # para cada caracter en la palabra  
    for char in word:      

    # si el caracter esta en lo adivinado por el jugador
        if char in guesses:    
    
        # imprimir letra
            print (char)    

        else:
    
        # si no imprimir _
            print ("_")     
       
        # sumar 1 al contador de fallas
            fail += 1    

    # si no hay fallas

    # ganaste
    if failed == 0:        
        print ("¡Ganáste!")  

    # salir del script
        break              

    print

    # adivine una letra al usuario
    guess = input("Adivina una letra: ") 

    # 
    guesses += guess                    

    # si la letra no esta en la palabra
    if guess not in word:  
 
     # los turnos se disminuyen
        turnos -= 1        
 
    # mal
        print ("Te equivocaste...")    
 
    # cuantos turnos quedan
        print ("Ahora tienes", + turnos, 'intentos')
 
    # cuando se llega a 0 en turnos
        if turnos == 0:           
    
        # perdiste
            print ("Perdiste")
