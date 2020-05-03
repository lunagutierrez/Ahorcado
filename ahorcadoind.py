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
import pygame
from pygame_functions import *



class Adivinar:
    
    def desarrollo(turnos,word):
        
        t=turtle.Turtle()
        dibujo.Tortuga.Ventana(t)
        guesses = ''
        #Lista vacía de los carácteres que han sido adivinados 
        listGuesses = []
        
        msgletra= makeLabel("Adivina una letra:  ", 35, 50, 50,"white","Agency FB", "black")
        showLabel(msgletra)
        
        msgadivinado= makeLabel("Estos son los caracteres que has adivinado hasta ahora: ", 35, 50, 400,"white","Agency FB", "black")
        showLabel(msgadivinado)
        
        x=100
        
        for n in word:
            lin = makeLabel("-", 60, x, 200, "white", "Agency FB", "black")
            showLabel(lin)
            time.sleep(1)
            x= x + 55
        
        
        
        while turnos > 0: 
            # adivine una letra
                                            
                box3=makeTextBox(250, 50, 35, 0, "", 1, 24)
                showTextBox(box3)
                
                guess=textBoxInput(box3)
                
                # de guess a guesses
                guesses += guess
                
                                
            # contados desde 0
                failed = 0             
                posx=100
            # para cada letra en la palabra
                for char in word: 
                                                        
            # mirar si la letra esta en lo adivinado
                    if char in guesses:    
            
                # imprimir el caracter
                        msgchar = makeLabel(char, 60, posx, 200, "white", "Agency FB", "black")
                        showLabel(msgchar)
                        time.sleep(1)
                        
                                            
                    else:
            
                # si no imprimir - por cada uno que no haya sido adivinado (lo hace en una misma linea)
                        msgnochar = makeLabel("-", 60, posx, 200, "white", "Agency FB", "black")
                        showLabel(msgnochar)
                        time.sleep(1)
                        
                # e incrementar el numero de fallas
                        failed += 1
                    
                    posx= posx + 55
        
            # si no hay fallas
                
            # Gano!
                if failed == 0:
                    hideLabel(msgletra)
                    hideLabel(msgadivinado)
                    black= makeLabel("                                              " ,40, 50, 450, "black","Agency FB", "black")
                    black1= makeLabel("                                              " ,40, 50, 50, "black","Agency FB", "black")
                    black2= makeLabel("                                              " ,80, 50, 200, "black","Agency FB", "black")
                    showLabel(black)
                    showLabel(black1)
                    showLabel(black2)
                    msgwin = makeLabel("¡Ganáste!", 60, 300, 200, "white", "Agency FB", "black")
                    showLabel(msgwin)
                    time.sleep(3)
                    break
            # Cerrar la ventana de turtle
            # salir
                
            
            #para cuando                     
                alreadyGuessed = False #falso por default para que cuando sea verdadero retorne el mensaje
                
                for w in listGuesses: #compara lo adivinado con cada uno de los caracteres adivinados
                    if w == guess:
                        alreadyGuessed = True
                        break
                if alreadyGuessed:
                    msgerr= makeLabel(" Ya adivinaste esta letra. Inténtalo de nuevo. ", 35, 50, 680,"white","Agency FB", "black")
                    showLabel(msgerr)
                    pause(1500)
                    hideLabel(msgerr)
                    continue    #comienza el ciclo desde el comienzo y no se penaliza tomanto turnos
                else:
                    listGuesses.append(guess) #añade a la lista el caracter adivinado
                    
                msguesses= makeLabel(str(listGuesses) , 35, 50, 450,"white","Agency FB", "black")
                showLabel(msguesses)
                    
            # si guess no esta en palabra
                if guess not in word:  
                        
                    if not guess.isalpha():
                        msgerr= makeLabel(" Debes adivinar una letra. ", 35, 50, 680,"white","Agency FB", "black")
                        showLabel(msgerr)
                        pause(1500)
                        hideLabel(msgerr)
                        
                    if guess.isalpha():
             # turnos se disminuyen
                        turnos -= 1        
         
            # imprima se equivoco
                        msgerr= makeLabel("Te equivocaste. Ahora tienes  " + str(turnos) + '  intentos', 35, 50, 600,"white","Agency FB", "black")
                        showLabel(msgerr)
                        pause(2500)
                        hideLabel(msgerr)
    
         
            # turnos que quedan
            #Dibujo del ahorcado según los intentos que quedan
                        dibujo.Mistakes.draw(t,turnos)
                        
            #Cuando el jugador pierde
                        
                        if turnos ==0:
                            hideLabel(msgletra)
                            hideLabel(msgadivinado)
                            black= makeLabel("                                              " ,40, 50, 450, "black","Agency FB", "black")
                            black1= makeLabel("                                              " ,40, 50, 50, "black","Agency FB", "black")
                            black2= makeLabel("                                              " ,80, 50, 200, "black","Agency FB", "black")
                            showLabel(black)
                            showLabel(black1)
                            showLabel(black2)
                            msgerr= makeLabel("¡Ahorcado!   La palabra era " +word , 60, 100, 200,"white","Agency FB", "black")
                            showLabel(msgerr)
                            pause(1500)
                          
                                
        dibujo.Tortuga.borrar(t)
        return turnos
        


def setup_ind(): 
            
    screen = screenSize(800 , 800)
    
    username = makeLabel("Nombre de Usuario", 50, 10, 10, "white", "Agency FB", "black")
    showLabel (username)
        
    box1=makeTextBox(350, 25, 300, 0, "", 0, 24)
        #Mostrar la caja de texto
    showTextBox(box1)
    
    user = textBoxInput(box1)
        #bienvenida
    hideLabel(username)
    hideLabel(box1)
    
    pause(1000)
    
    bienvenida= makeLabel("Hola,   " + user + "   Juguemos ahorcado!", 35, 50, 50,"white","Agency FB", "black")
    showLabel(bienvenida)
    
    turnos = 6
    
    pause(1000)
    
    msgturnos = makeLabel("Tienes  " + str(turnos) + "  intentos", 35, 50, 100, "white", "Agency FB", "black")
    showLabel(msgturnos)
    
    pause(1000)
    
    msgnivel = makeLabel("Ahora debes escoger un nivel de dificultad", 35, 50, 200, "white", "Agency FB", "black")
    showLabel(msgnivel)
    
    pause(1000)
    
    #establecemos la palabra
    word = palabras.Nivel.__str__()
    
    hideLabel(bienvenida)
    hideLabel(msgturnos)
    hideLabel(msgnivel)
    
        
    
    pause(1000)
    #se ejecuta la clase para que se desarrolle el juego
    Adivinar.desarrollo(turnos,word)
    
    dibujo.Tortuga.fin() #la tortuga termina su proceso
        
    endWait()
