# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:00:26 2020

@author: lunag
"""
#importar las librerías necesarias

import time
import palabras
import random 
import turtle
import dibujo


#Bienvenida

def setup_ind():
    user = input("¿Nombre de usuario? ")

    print ("Hola, " + user, "Juguemos ahorcado!")
    

#esperar un segundo
    time.sleep(1)

    #lev = int(input("Escoge un nivel de dificultad entre 3 y 10: "))  
    def level():
        while True:
            lev = int(input("Escoge un nivel de dificultad entre 3 y 10: "))  
            try:
                if lev == 3:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    print ("Ya puedes comenzar a adivinar")
                    palabra = palabras.pal3
                    break
                elif lev == 4:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    print ("Ya puedes comenzar a adivinar")
                    palabra = palabras.pal4
                    break
                elif lev == 5:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    print ("Ya puedes comenzar a adivinar")
                    palabra = palabras.pal5
                    break
                elif lev == 6:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    print ("Ya puedes comenzar a adivinar")
                    palabra = palabras.pal6
                    break
                elif lev == 7:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    print ("Ya puedes comenzar a adivinar")
                    palabra = palabras.pal7
                    break
                elif lev ==8:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    print ("Ya puedes comenzar a adivinar")
                    palabra = palabras.pal8
                    break
                elif lev ==9:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    print ("Ya puedes comenzar a adivinar")
                    palabra = palabras.pal9
                    break
                elif lev ==10:
                    print("La palabra que tienes que adivinar tiene {0} letras".format(lev))
                    print ("Ya puedes comenzar a adivinar")
                    palabra = palabras.pal10
                    break
                else:
                    print('{0} no esta entre 3 y 10'.format(lev))
            except ValueError:
                print('{0} no es un entero entre 3 y 10'.format(lev))
                
        pal = random.choice(palabra)
        return pal  
          
         
            
    time.sleep(0.5)

    turnos = 6
    print("Tienes", turnos, "intentos")

    time.sleep(0.5)
    print("Ahora debes escoger un nivel de dificultad")
    time.sleep(0.5)

#establecemos la palabra


#creamos la variable de guesses vacia 
    guesses = ''

#determinamos la palabra y el numero de turnos 
    word = level()
    
#crear la ventana de turtle
    turtle.setup(800,800,0,0)
    wn=turtle.Screen()
    wn.bgcolor("white")
    wn.title("Ahorcado")
    donatello=turtle.Turtle()
    donatello.color("black")
    donatello.pensize(3)
    donatello.hideturtle()
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
            
    # Cerrar la ventana de turtle
    
            turtle.mainloop()
            turtle.done()
            turtle.bye()

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
            
    #Dibujo del ahorcado según los intentos que quedan
    
            if turnos == 5:
                dibujo.horca(donatello)
                dibujo.cabeza(donatello)
            elif turnos == 4:
                dibujo.tronco(donatello)
            elif turnos == 3:
                dibujo.pierna1(donatello)
                dibujo.pie1(donatello)
            elif turnos == 2:
                dibujo.pierna2(donatello) 
                dibujo.pie2(donatello)
            elif turnos == 1:
                dibujo.brazo1(donatello)
                dibujo.mano1(donatello)
                dibujo.brazo2(donatello)
                dibujo.mano2(donatello)
                
            #Cuando el jugador pierde
            
            elif turnos == 0:
                dibujo.cabello(donatello)
                dibujo.ojo1(donatello)
                dibujo.ojo2(donatello)
                dibujo.boca(donatello)
                dibujo.lengua(donatello)
                
                print ("¡Ahorcado!")
                print("La palabra era " +word)
                
         # Cerrar la ventana de turtle
                turtle.mainloop()
                turtle.done()
                turtle.bye()
                
                

#BEGINNING-OF-EXECUTION
setup_ind()
#END-OF-EXECUTION
