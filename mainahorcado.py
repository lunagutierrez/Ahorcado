# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:21:29 2020

@author: lunag
"""

import ahorcadoind

def juego():
    print("\nWelcome to 'Hangman'")
    
    while True:
        try:
            version = int(input("Individual [1] o Multiplayer? [2]\n"))

            if version == 1:
                ahorcadoind()
                break
#            elif version == 2:
#                ahorcadomult()
                break
            else:
                print("\nPlease pick '1' or '2'")  
        except:
            print("Please pick '1' or '2'")

juego()