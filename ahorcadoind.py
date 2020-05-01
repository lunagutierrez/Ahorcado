# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:00:26 2020
@author: lunag
"""
import time
import palabras
import turtle
import dibujo
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

class Adivinar:
    
    def desarrollo(turnos,word):
        #
        t=turtle.Turtle()
        dibujo.Tortuga.Ventana(t)
        guesses = ''
        #Lista vacía de los carácteres que han sido adivinados 
        listGuesses = []
        
        while turnos > 0:         
                
            # contados desde 0
                failed = 0             
                print()
            # para cada letra en la palabra
                for char in word: 
                
            # mirar si la letra esta en lo adivinado
                    if char in guesses:    
            
                # imprimir el caracter
                        win.blit(fontTitle.render(char, 0,(255, 255, 255)),(50,310))   
                        pygame.display.update()
                    else:
            
                # si no imprimir - por cada uno que no haya sido adivinado (lo hace en una misma linea)
                        win.blit(fontTitle.render("_", 0,(0, 230, 230)), (0,310))     
                        pygame.display.update()
                # e incrementar el numero de fallas
                        failed += 1
        
            # si no hay fallas
                
            # Gano!
                if failed == 0:   
                    #win.blit(fontTitle.render("")
                    win.blit(fontTitle.render("¡Ganáste!", 0,(0, 230, 230)), (20,310)) 
                    pygame.display.update()
                    time.sleep(3)
                    break
            # Cerrar la ventana de turtle
            # salir
                #win.blit(fontTitle.render(("")
                win.blit(fontBody.render("Estos son los caracteres que has adivinado hasta ahora: " + str(listGuesses), 0,(0, 230, 230)), (50,480))
            # adivine una letra
                guess = input("Adivina una letra: ").lower()
        
            # de guess a guesses
                guesses += guess                    
                
            #para cuando                     
                alreadyGuessed = False #falso por default para que cuando sea verdadero retorne el mensaje
                for w in listGuesses: #compara lo adivinado con cada uno de los caracteres adivinados
                    if w == guess:
                        alreadyGuessed = True
                        break
                if alreadyGuessed:
                    win.blit(fontBody.render("\n Ya adivinaste esta letra. Inténtalo de nuevo. \n", 0,(255, 255, 255)), (50,480))
                    pygame.display.update()
                    continue    #comienza el ciclo desde el comienzo y no se penaliza tomanto turnos
                else:
                    listGuesses.append(guess) #añade a la lista el caracter adivinado
                    
            # si guess no esta en palabra
                if guess not in word:  
                        
                    if not guess.isalpha():
                        win.blit(fontBody.render("Debes adivinar una letra", 0,(255, 255, 255)), (250,480))  #condicional para cuando lo adivinado no es una letra (no se penaliza)
                        pygame.display.update()
                    if guess.isalpha():
             # turnos se disminuyen
                        turnos -= 1        
         
            # imprima se equivoco
                        win.blit(fontBody.render("Te equivocaste...", 0,(255, 10, 10)), (250,480))   
         
            # turnos que quedan
                        win.blit(fontBody.render("Ahora tienes", + turnos, 'intentos', 0,(255, 255, 255)), (250,70))
                        pygame.display.update()
            #Dibujo del ahorcado según los intentos que quedan
                        dibujo.Mistakes.draw(t,turnos)
                        
            #Cuando el jugador pierde
                        
                        if turnos ==0:
                             win.blit(fontTitle.render("¡Ahorcado!", 0,(255, 0, 0)), (100,310))
                             win.blit(fontBody.render("La palabra era " +word, 0,(255, 255, 255)), (150,310))  
        
        dibujo.Tortuga.borrar(t)
        return turnos
        


def setup_ind(): 
    user = input("¿Nombre de usuario? ")
    #bienvenida
    win.blit(fontTitle.render("Hola, " + user, "Juguemos ahorcado!", 0,(0, 128, 128)), (50,80))
    
    #esperar un segundo y medio
    time.sleep(1.5)

    turnos = 6
    win.blit(fontTitle.render("Tienes", turnos, "intentos", 0,(255, 255, 255)), (50,280))

    time.sleep(0.5)
    win.blit(fontTitle.render("Ahora debes escoger un nivel de dificultad", 0,(255, 255, 255)), (50,450))
    time.sleep(0.5)
    
    pygame.display.update()
    
    #establecemos la palabra
    word = palabras.Nivel.__str__()
    #se ejecuta la clase para que se desarrolle el juego
    Adivinar.desarrollo(turnos,word)
    dibujo.Tortuga.fin() #la tortuga termina su proceso 
    
