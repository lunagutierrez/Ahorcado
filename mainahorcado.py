# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:21:29 2020
@author: lunag
"""

import ahorcadoind
import ahorcadomult


print("\nBienvenido al Juego de Ahorcado") #Bienvenida al juego
for i in range(4):
    print("")
    
    
def juego():
    Main = True #partimos de true por default
    while Main == True: #así al correr el programa siempre se abre el menu ppal
        print("""Menu principal:
            [1] Jugar
            [2] Salir""")
        mainin = input()
        
        if mainin == "1": #se muestran las modalidades de juego disponibles o se puede regresar al menu ppal
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
            Main = False #se cierra el menu ppal y se termina el programa
        else:
            print("Seleccione una opción válida.")
            
juego()
