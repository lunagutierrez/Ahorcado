# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:00:26 2020
@author: lunag
"""
#importar las librerías necesarias
import time
import palabras
import turtle
import dibujo
import sys

class Adivinar:
    
    def desarrollo(turnos,word):
        #
        t=turtle.Turtle()
        dibujo.Tortuga.Ventana(t)
        guesses = ''
        listGuesses = []
        while turnos > 0:         
                
            # contados desde 0
                failed = 0             
        
            # para cada letra en la palabra
                for char in word: 
                
            # mirar si la letra esta en lo adivinado
                    if char in guesses:    
            
                # imprimir el caracter
                        sys.stdout.write(char )    
        
                    else:
            
                # si no imprimir -
                        sys.stdout.write("_ ")     
               
                # e incrementar el numero de fallas
                        failed += 1
        
            # si no hay fallas
        
            # Gano!
                if failed == 0:        
                    print ("¡Ganáste!") 
                    break
            # Cerrar la ventana de turtle
            # salir
                print(" ")
                print("Estos son los caracteres que has adivinado hasta ahora: " + str(listGuesses))
            # adivine una letra
                guess = input("Adivina una letra: ").lower()
        
            # de guess a guesses
                guesses += guess                    
                
                    
                alreadyGuessed = False
                for w in listGuesses:
                    if w == guess:
                        alreadyGuessed = True
                        break
                if alreadyGuessed:
                    print("\n Ya adivinaste esta letra. Inténtalo de nuevo. \n")
                    continue
                else:
                    listGuesses.append(guess)
                    
            # si guess no esta en palabra
                if guess not in word:  
                        
                    if not guess.isalpha():
                        print("Debes adivinar una letra")
                    
                    if guess.isalpha():
             # turnos se disminuyen
                        turnos -= 1        
         
            # imprima se equivoco
                        print ("Te equivocaste...")    
         
            # turnos que quedan
                        print ("Ahora tienes", + turnos, 'intentos')
                    
            #Dibujo del ahorcado según los intentos que quedan
                        dibujo.Mistakes.draw(t,turnos)
                    #Cuando el jugador pierde
                    
        print ("¡Ahorcado!")
        print("La palabra era " +word)    
        
        return turnos


#Bienvenida

def setup_ind():
    user = input("¿Nombre de usuario? ")

    print ("Hola, " + user, "Juguemos ahorcado!")
    
#esperar un segundo y medio
    time.sleep(1.5)

    turnos = 6
    print("Tienes", turnos, "intentos")

    time.sleep(0.5)
    print("Ahora debes escoger un nivel de dificultad")
    time.sleep(0.5)

#establecemos la palabra
    word = palabras.Nivel.__str__()
    Adivinar.desarrollo(turnos,word)
    dibujo.Tortuga.fin()
