# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:21:29 2020
@author: lunag
"""

import ahorcadoind
import ahorcadomult


print("\nBienvenido al Juego de Ahorcado")
for i in range(4):
    print("")
    
    
def juego():
    Main = True 
    while Main == True:
        print("""Menu principal:
            [1] Jugar
            [2] Salir""")
        mainin = input()
        
        if mainin == "1":
            print("""¿En qué modalidad de juego te gustaría jugar?:
    [1] Individual
    [2] Multijugador
    [3] Regresar al menu principal""")
            version = input()
            if version == "1":
                ahorcadoind.setup_ind()
            elif version == "2":
                ahorcadomult.setup_mult()
            elif version == "3":
                continue
            else:
                print("Por favor seleccione una opción válida")
        elif mainin == "2":
            Main = False
        else:
            print("Seleccione una opción válida.")
            
juego()
