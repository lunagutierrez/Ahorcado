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
import pygame
from pygame_functions import *


class palabras: #clase de palabras que permite escribir la palabra a adivinar tomando en cuenta el nivel de dificultad escogido
    def palabra(lev):
            while True:
                msgin = makeLabel( "Escribe una palabra de la longitud escogida", 35, 50, 25,"white","Agency FB", "black")
                showLabel(msgin)
                
                wordbox=makeTextBox(50, 75, 350, 0, "", 0, 24)
                showTextBox(wordbox)
                
                word=str(textBoxInput(wordbox)).lower()
    
                try: 
                    if not word.isalpha():#si no escribe letras
                        msga = makeLabel( "Los caracteres de tu palabra solo pueden ser letras", 35, 50, 125,"white","Agency FB", "black")
                        showLabel(msga)
                        pause(2500)
                        hideLabel(msga)
                        
                    elif lev != len(word):#si escribe una palabra de longitud incorrecta
                        msga = makeLabel( "Tu palabra debe ser de la longitud escogida", 35, 50, 125,"white","Agency FB", "black")
                        showLabel(msga)
                        pause(2500)
                        hideLabel(msga)
                        
                    else: #retornar la palabra
                        hideLabel(msgin)
                        hideLabel(wordbox)
                        return word
                        break
                    
                except: #si escribe algo sin sentido
                    msga = makeLabel( "Lo digitado no es válido", 35, 50, 125,"white","Agency FB", "black")
                    showLabel(msga)
                    pause(2500)
                    hideLabel(msga)
                    
                #Esconder mensajes
                hideLabel(msgin)
                hideLabel(wordbox)
            
            


#Bienvenida
def setup_mult():
    
    screen = screenSize(800 , 800)
    
    #Usuario 1
    username1 = makeLabel("Nombre de Usuario del jugador 1", 50, 10, 10, "white", "Agency FB", "black")
    usbox1 = makeTextBox(550, 25, 150, 0, "", 0, 24)
    showLabel (username1)
    showTextBox(usbox1)
    user1 = str(textBoxInput(usbox1))
    hideLabel(username1)
    hideLabel(usbox1)
    
    #Usuario 2    
    username2 = makeLabel("Nombre de Usuario del jugador 2", 50, 10, 10, "white", "Agency FB", "black")
    usbox2 = makeTextBox(550, 25, 150, 0, "", 0, 24)
    showLabel (username2)
    showTextBox(usbox2)
    user2 = str(textBoxInput(usbox2))
    hideLabel(username2)
    hideLabel(usbox2)
    
    pause(1000)
    
    #Bienvenida
    bienvenida = makeLabel("Hola " +user1+ " y " +user2+ " Juguemos ahorcado!", 35, 50, 25,"white","Agency FB", "black")
    showLabel(bienvenida)
    
    pause(1000)
    
    #Orden en el que tienen que adivinar    
    orden = makeLabel("Primero va a adivinar  " + user1 + "  la palabra que escoja  " + user2, 35, 50, 100,"white","Agency FB", "black")
    showLabel(orden)
     
 
#esperar un segundo
    pause(1000)
   
    t=turtle.Turtle()
    #Creamos la ventana del juego en turtle
    dibujo.Tortuga.Ventana(t)
    
    msgturnos1 = makeLabel( "Escojan un nivel de dificultad (1 , 2 o 3)", 35, 50, 175,"white","Agency FB", "black")
    showLabel(msgturnos1)
    
    #número de turnos según el nivel de dificultad    
    while True:
        boxdif=makeTextBox(500, 175, 25, 0, "", 1, 24)
        #Mostrar la caja de texto
        showTextBox(boxdif)
        niveldif = textBoxInput(boxdif) 
        
        if not niveldif.isalpha():
            
            niveldif=int(niveldif)
            
            if niveldif == 3: 
                turnos = 6
                msgturnos = makeLabel("Tienes  " + str(turnos) + "  intentos", 35, 50, 250, "white", "Agency FB", "black")
                showLabel(msgturnos)
                pause(3000)
                hideLabel(boxdif)
                hideLabel(msgturnos)
                break
                
            elif niveldif == 2:
                turnos = 9
                msgturnos = makeLabel("Tienes  " + str(turnos) + "  intentos", 35, 50, 250, "white", "Agency FB", "black")
                showLabel(msgturnos)
                pause(3000)
                hideLabel(boxdif)
                hideLabel(msgturnos)
                break
            
            elif niveldif == 1:
                turnos = 12
                msgturnos = makeLabel("Tienes  " + str(turnos) + "  intentos", 35, 50, 250, "white", "Agency FB", "black")
                showLabel(msgturnos)
                pause(3000)
                hideLabel(boxdif)
                hideLabel(msgturnos)
                break
            
            else:
                msgerror = makeLabel("{0} no es un entero entre 1 y 3".format(niveldif), 35, 50, 250, "white", "Agency FB", "black")
                showLabel(msgerror)
                pause(1000)
                hideLabel(msgerror)
                hideLabel(boxdif)
                
        else:
            msgerror = makeLabel("{0} no es un entero entre 1 y 3".format(niveldif), 35, 50, 250, "white", "Agency FB", "black")
            showLabel(msgerror)
            pause(2000)
            hideLabel(msgerror)
            hideLabel(boxdif)
            
   
    hideLabel(msgturnos1)
    
     #ciclo while para determinar la longitud de las palabras a adivinar
    while True: 
        
        msgnivel= makeLabel("Escojan la longitud de la palabra (entre 3 y 10): ", 35, 50, 175,"white","Agency FB", "black")
        showLabel(msgnivel)
            
        box4=makeTextBox(567, 175, 40, 0, "", 2, 24)
        showTextBox(box4)
                            
        lev = textBoxInput(box4)
        
        if not lev.isalpha():
            
            lev=int(lev)
                   
            if 3 <= lev <= 10:
                num= makeLabel("Las palabras que tienen que adivinar tienen {0} letras".format(lev), 35, 50, 250,"white","Agency FB", "black")
                showLabel(num)
                pause(2500)
                hideLabel(bienvenida)
                hideLabel(orden)  
                hideLabel(msgnivel)
                hideLabel(box4)  
                hideLabel(num)     
                break
                
            else:
                num= makeLabel("{0} no es un entero entre 3 y 10".format(lev), 35, 50, 250,"white","Agency FB", "black")
                showLabel(num)
                pause(2000)
                hideLabel(num)
        
        else:
            num= makeLabel("{0} no es un entero entre 3 y 10".format(lev), 35, 50, 250,"white","Agency FB", "black")
            showLabel(num)
            pause(2000)
            hideLabel(num)
            
        hideLabel(msgnivel)
        hideLabel(box4)
                
    msg2 = makeLabel( user1 + " cierra los ojos mientras " + user2 + " digita la palabra", 35, 50, 25,"white","Agency FB", "black")
    showLabel(msg2)
    
    msg3 = makeLabel("Puedes abrir los ojos cuando escuches el sonido", 35, 50, 100,"white","Agency FB", "black")
    showLabel(msg3)    
    
    pause(5000)
    
    hideLabel(msg2)
    hideLabel(msg3)
          
    #usamos la clase palabras con el nivel escogido en el ciclo while de lev previo 
    #el jugador 2 digita la palabra a adivinar
    word = palabras.palabra(lev)
    
    time.sleep(0.5)
    
    winsound.PlaySound("audioahorcado.wav", winsound.SND_ASYNC) #El jugador que adivina es advertido que puede mirar la pantalla
       
    
    time.sleep(0.5)
    msgempezar1 = makeLabel( "¡Vamos a empezar!", 35, 50, 75,"white","Agency FB", "black")
    showLabel(msgempezar1)
    
    pause(2000)
    
    hideLabel(msgturnos1)
    hideLabel(msgempezar1)
    
    ta = time.process_time()
    #usamos la clase de la modalidad individual
    #calculamos el puntaje como el producto de los turnos restantes y el nivel de dificultad*10
    puntaje1 = int(ahorcadoind.Adivinar.desarrollo(turnos,word)) * lev * 10 #toma el valor (int) de los turnos 
    tb = time.process_time() 
    t1 = tb - ta #el tiempo que le toma al jugador1 adivinar 
    
  #segunda ronda  
    time.sleep(0.5)
    
    orden2 = makeLabel("Ahora " + user2 + " va a adivinar la palabra que escoja " + user1, 35, 50, 25,"white","Agency FB", "black")
    showLabel(orden2)
    
    pause(1000)
    
    msg2 = makeLabel( user2 + " cierra los ojos mientras " + user1 + " digita la palabra", 35, 50, 100,"white","Agency FB", "black")
    showLabel(msg2)
    
    msg3 = makeLabel("Puedes abrirlos cuando escuches el sonido", 35, 50, 175,"white","Agency FB", "black")
    showLabel(msg3) 
    
    pause(5000)
    
    hideLabel(msg2)
    hideLabel(msg3)
    hideLabel(orden2)
        
    #usamos la clase palabras con el nivel escogido en el ciclo while de lev previo 
    #el jugador 1 digita la palabra a adivinar
    word = palabras.palabra(lev)
    
    time.sleep(0.5)
    winsound.PlaySound("audioahorcado.wav", winsound.SND_ASYNC) #se puede volver a ver la pantalla
    
    if niveldif == 3:
        turnos = 6
        
    elif niveldif == 2:
        turnos = 9
        
    elif niveldif == 1:
        turnos = 12
    
    msgturnos1 = makeLabel( user2+ " tienes " +str(turnos)+ " intentos ", 35, 50, 25,"white","Agency FB", "black")
    showLabel(msgturnos1)
    
    time.sleep(0.5)
    msgempezar1 = makeLabel( "¡Vamos a empezar!", 35, 50, 75,"white","Agency FB", "black")
    showLabel(msgempezar1)
    
    pause(2000)
    
    hideLabel(msgturnos1)
    hideLabel(msgempezar1)
    
    
    tc = time.process_time()
    #establecemos la palabra
    puntaje2=int(ahorcadoind.Adivinar.desarrollo(turnos,word))*lev*10     #toma el valor (int) de los turnos    
    
    td = time.process_time()     
    #calculamos el puntaje como el producto de los turnos restantes y el nivel de dificultad*10
              
    t2 = td - tc #el tiempo que le toma al jugador2 adivinar
        
    
    #se comparan los puntajes para determinar el ganador
    if puntaje1 < puntaje2:
        print1 = makeLabel(user2 + " ha ganado la partida con un puntaje de {0}".format(puntaje2), 35, 50, 25,"white","Agency FB", "black")
        showLabel(print1)
        print2 = makeLabel(", mientras que " + user1 + " solo ha obtenido {0} puntos.".format(puntaje1), 35, 50, 100,"white","Agency FB", "black")
        showLabel(print2)
        pause(4000)
        hideLabel(print1)
        hideLabel(print2)
    
    elif puntaje2 < puntaje1:
        print1 = makeLabel(user1 + " ha ganado la partida con un puntaje de {0}".format(puntaje1), 35, 50, 25,"white","Agency FB", "black")
        showLabel(print1)
        print2 = makeLabel(", mientras que " + user2 + " solo ha obtenido {0} puntos.".format(puntaje2), 35, 50, 100,"white","Agency FB", "black")
        showLabel(print2)
        pause(4000)
        hideLabel(print1)
        hideLabel(print2)
        
    elif puntaje1 == 0 and puntaje2 == 0:
        print1 = makeLabel("Ninguno de los dos logró adivinar las palabras. No hay un ganador", 35, 50, 25,"white","Agency FB", "black")
        showLabel(print1)
        pause(4000)
        hideLabel(print1)
    
    else:
        print1 = makeLabel("Ambos jugadores han obtenido un puntaje de {0}".format(puntaje1), 35, 50, 25,"white","Agency FB", "black")
        showLabel(print1)
        
        if t1 < t2:
            print2 = makeLabel( user1 + " ha ganado pues ha adivinado en un menor tiempo", 35, 50, 100,"white","Agency FB", "black")
            showLabel(print2)
            pause(4000)
            hideLabel(print1)
            hideLabel(print2)
            
        elif t2 < t1:
            print2 = makeLabel( user2 + " ha ganado pues ha adivinado en un menor tiempo", 35, 50, 100,"white","Agency FB", "black")
            showLabel(print2)
            pause(4000)
            hideLabel(print1)
            hideLabel(print2)
            
        else:
            print2 = makeLabel("Ha habido un empate", 35, 50, 100,"white","Agency FB", "black")
            showLabel(print2)
            pause(4000)
            hideLabel(print1)
            hideLabel(print2)
            
# Cerrar la ventana de turtle
    endWait()
    dibujo.Tortuga.fin()
