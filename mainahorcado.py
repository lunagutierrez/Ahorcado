# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:21:29 2020

@author: lunag
"""

import ahorcadoind
import ahorcadomult

def juego():
    print("\nBienvenido al Juego de Ahorcado")
    for i in range(4):
        print("")
        
    while True:
        version = int(input("Individual [1] o Multijugador? [2]  \n"))
        if version == 1:
            ahorcadoind.setup_ind()
            break
        elif version == 2:
            ahorcadomult.setup_mult()
            break
        else:
            print("Por favor, elige 1 o 2")
        
        

#BEGINNING-OF-EXECUTION
juego()
#END-OF-EXECUTION
