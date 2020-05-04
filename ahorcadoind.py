# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:00:26 2020
@author: lunag
Este es el módulo para el juego individual
En este modulo se crea una clase que es la base tanto del juego individual como el multijugador
Usamos también el módulo pygame_functions, para crear cuadros de texto y cuadros de inputs que retornen lo que digita el usuario

"""
#importar las librerías necesarias

import time
import palabras
import turtle
import dibujo
import pygame
from pygame_functions import *



class Adivinar: #Clase base del juego, donde el o los usuarios adivinan cuando ya tienen la palabra
    
    def desarrollo(turnos,word):
        
        t=turtle.Turtle() #Deifnir tortuga
        dibujo.Tortuga.Ventana(t) #Abrir la ventana de turtle
        guesses = '' 
         
        listGuesses = []#Lista vacía de los carácteres que han sido adivinados
        
        #Crear mensaje de adivinar letra
        msgletra= makeLabel("Adivina una letra:  ", 35, 50, 50,"white","Agency FB", "black")
        showLabel(msgletra)
        
        #Crear mensaje de caracteres adivinados        
        msgadivinado= makeLabel("Estos son los caracteres que has adivinado hasta ahora: ", 35, 50, 400,"white","Agency FB", "black")
        showLabel(msgadivinado)
        
        #poición inicial guión para poner las letras
        x=100
        
        #Crear los guiones según el número de letras
        for n in word:
            lin = makeLabel("-", 60, x, 200, "white", "Agency FB", "black")
            showLabel(lin)
            time.sleep(1)
            x= x + 55
        
        if turnos == 12: #Si elige el nivel 1
                           
            while turnos > 0: 
                # adivine una letra
                                                
                    box3=makeTextBox(250, 50, 35, 0, "", 1, 24)
                    showTextBox(box3)
                    
                    guess=textBoxInput(box3).lower()
                    
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
                        black= makeLabel("                                                                                " ,40, 50, 450, "black","Agency FB", "black")
                        black1= makeLabel("                                                                               " ,40, 50, 50, "black","Agency FB", "black")
                        black2= makeLabel("                                                                               " ,80, 50, 200, "black","Agency FB", "black")
                        showLabel(black)
                        showLabel(black1)
                        showLabel(black2)
                        msgwin = makeLabel("¡Adivináste!", 60, 300, 200, "white", "Agency FB", "black")
                        showLabel(msgwin)
                        time.sleep(3.3)
                        black3= makeLabel("                                                                                 ", 70, 290, 200, "white", "Agency FB", "black")
                        showLabel(black3)
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
                        msgerr= makeLabel(" Ya adivinaste esta letra. Inténtalo de nuevo. ", 35, 50, 600,"white","Agency FB", "black")
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
                            msgerr= makeLabel(" Debes adivinar una letra. ", 35, 50, 600,"white","Agency FB", "black")
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
                            dibujo.Mistakes.draw1(t,turnos)
                            
                #Cuando el jugador pierde
                            
                            if turnos ==0:
                                hideLabel(msgletra)
                                hideLabel(msgadivinado)
                                black= makeLabel("                                                                                        " ,40, 50, 450, "black","Agency FB", "black")
                                black1= makeLabel("                                                                                       "  ,40, 50, 50, "black","Agency FB", "black")
                                black2= makeLabel("                                                                                       " ,80, 50, 200, "black","Agency FB", "black")
                                showLabel(black)
                                showLabel(black1)
                                showLabel(black2)
                                msgerr= makeLabel("¡Ahorcado! La palabra era " +word , 45, 100, 200,"white","Agency FB", "black")
                                showLabel(msgerr)
                                pause(3000)
                                black3= makeLabel("                                                                                        ", 70, 90, 200, "white", "Agency FB", "black")
                                showLabel(black3)
                                break
                          
        elif turnos == 9: #Si elige el nivel 2
            
            while turnos > 0: 
                # adivine una letra
                                                
                    box3=makeTextBox(250, 50, 35, 0, "", 1, 24)
                    showTextBox(box3)
                    
                    guess=textBoxInput(box3).lower()
                    
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
                        msgwin = makeLabel("¡Adivináste!", 60, 300, 200, "white", "Agency FB", "black")
                        showLabel(msgwin)
                        time.sleep(3.3)
                        black3= makeLabel("                                           ", 70, 290, 200, "white", "Agency FB", "black")
                        showLabel(black3)
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
                        msgerr= makeLabel(" Ya adivinaste esta letra. Inténtalo de nuevo. ", 35, 50, 600,"white","Agency FB", "black")
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
                            msgerr= makeLabel(" Debes adivinar una letra. ", 35, 50, 600,"white","Agency FB", "black")
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
                            dibujo.Mistakes.draw2(t,turnos)
                            
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
                                pause(3000)
                                black3= makeLabel("                                                                       ", 70, 90, 200, "white", "Agency FB", "black")
                                showLabel(black3)
                                break
        
        elif turnos == 6: #Si elige el nivel 3
            while turnos > 0: 
                # adivine una letra
                                                
                    box3=makeTextBox(250, 50, 35, 0, "", 1, 24)
                    showTextBox(box3)
                    
                    guess=textBoxInput(box3).lower()
                    
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
                        black= makeLabel("                                                                      " ,40, 50, 450, "black","Agency FB", "black")
                        black1= makeLabel("                                                                     " ,40, 50, 50, "black","Agency FB", "black")
                        black2= makeLabel("                                                                     " ,80, 50, 200, "black","Agency FB", "black")
                        showLabel(black)
                        showLabel(black1)
                        showLabel(black2)
                        msgwin = makeLabel("¡Adivináste!", 60, 300, 200, "white", "Agency FB", "black")
                        showLabel(msgwin)
                        time.sleep(3.3)
                        black3= makeLabel("                                           ", 70, 290, 200, "white", "Agency FB", "black")
                        showLabel(black3)
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
                        msgerr= makeLabel(" Ya adivinaste esta letra. Inténtalo de nuevo. ", 35, 50, 600,"white","Agency FB", "black")
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
                            msgerr= makeLabel(" Debes adivinar una letra. ", 35, 50, 600,"white","Agency FB", "black")
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
                            dibujo.Mistakes.draw3(t,turnos)
                            
                #Cuando el jugador pierde
                            
                            if turnos ==0:
                                hideLabel(msgletra)
                                hideLabel(msgadivinado)
                                black= makeLabel("                                                                      " ,40, 50, 450, "black","Agency FB", "black")
                                black1= makeLabel("                                                                     " ,40, 50, 50, "black","Agency FB", "black")
                                black2= makeLabel("                                                                     " ,80, 50, 200, "black","Agency FB", "black")
                                showLabel(black)
                                showLabel(black1)
                                showLabel(black2)
                                msgerr= makeLabel("¡Ahorcado!   La palabra era " +word , 60, 100, 200,"white","Agency FB", "black")
                                showLabel(msgerr)
                                pause(3000)
                                black3= makeLabel("                                                                       ", 70, 90, 200, "white", "Agency FB", "black")
                                showLabel(black3)
                                break
            
                        
        dibujo.Tortuga.borrar(t)
        return turnos
        


def setup_ind(): 
            
    screen = screenSize(800 , 800) #inicir pygme unction
    
    #C    
    username = makeLabel("Nombre de Usuario", 50, 10, 10, "white", "Agency FB", "black")
    showLabel (username)
        
    box1=makeTextBox(350, 25, 300, 0, "", 0, 24)
    #Mostrar la caja de texto
    showTextBox(box1)
    
    user = textBoxInput(box1) #Nombre del usuario
    
    #bienvenida
    hideLabel(username)
    hideLabel(box1)
    
    pause(1000)
    
    bienvenida= makeLabel("Hola,   " + user + "   Juguemos ahorcado!", 35, 50, 50,"white","Agency FB", "black")
    showLabel(bienvenida)
    
    turnos = 0
    
    pause(1000)
    
    msgdif = makeLabel("Escoge un nivel de dificultad (1 , 2 o 3)", 35, 50, 100, "white", "Agency FB", "black")
    showLabel(msgdif)
    pause(1000)
    
    
       
    
    while True:
        boxdif=makeTextBox(500, 100, 25, 0, "", 1, 24) #Mostrar la caja de texto
        
        showTextBox(boxdif) 
        niveldif = textBoxInput(boxdif) #retorn el nivel de dificultad elegido
        
        if not niveldif.isalpha():
            
            niveldif=int(niveldif)
            
            if niveldif == 3: #Si elige el nivel 3, solo tiene 6 turnos
                turnos = 6
                msgturnos = makeLabel("Tienes  " + str(turnos) + "  intentos", 35, 50, 200, "white", "Agency FB", "black")
                showLabel(msgturnos)
                pause(2000)
                hideLabel(boxdif)
                break
                
            elif niveldif == 2: #Si elige el nivel 2, tiene 9 turnos
                turnos = 9
                msgturnos = makeLabel("Tienes  " + str(turnos) + "  intentos", 35, 50, 200, "white", "Agency FB", "black")
                showLabel(msgturnos)
                pause(2000)
                hideLabel(boxdif)
                break
            
            elif niveldif == 1: #Si elige el nivel 1, tiene 12 turnos
                turnos = 12
                msgturnos = makeLabel("Tienes  " + str(turnos) + "  intentos", 35, 50, 200, "white", "Agency FB", "black")
                showLabel(msgturnos)
                pause(2000)
                hideLabel(boxdif)
                break
            
            else: #si no digita un número entre 1 y 3
                msgerror = makeLabel("{0} no es un entero entre 1 y 3".format(niveldif), 35, 50, 200, "white", "Agency FB", "black")
                showLabel(msgerror)
                pause(1000)
                hideLabel(msgerror)
                hideLabel(boxdif)
                
        else: #si digita una letra
            msgerror = makeLabel("{0} no es un entero entre 1 y 3".format(niveldif), 35, 50, 200, "white", "Agency FB", "black")
            showLabel(msgerror)
            pause(2000)
            hideLabel(msgerror)
            hideLabel(boxdif)
        
    
        
    #establecemos la palabra
    word = palabras.Nivel.__str__()
    
    #esconder los mensajes creados    
    hideLabel(bienvenida)
    hideLabel(msgdif)
    hideLabel(msgturnos)
    hideLabel(boxdif)
        
    
    pause(1000)
    
    #se ejecuta la clase para que se desarrolle el juego
    Adivinar.desarrollo(turnos,word)
    
    dibujo.Tortuga.fin() #la tortuga termina su proceso
    endWait()
