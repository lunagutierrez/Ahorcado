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

#here we set the secret
word = "python"

#creates an variable with an empty value
guesses = ''

#determine the number of turns

# Create a while loop

#check if the turns are more than zero
while turnos > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char)    

        else:
    
        # if not found, print a dash
            print ("_")     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("¡Ganáste!")  

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess = input("Adivina una letra: ") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turnos -= 1        
 
    # print wrong
        print ("Te equivocaste...")    
 
    # how many turns are left
        print ("Ahora tienes", + turnos, 'intentos')
 
    # if the turns are equal to zero
        if turnos == 0:           
    
        # print "You Lose"
            print ("Perdiste")