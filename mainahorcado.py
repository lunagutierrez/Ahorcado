Este es el archivo principal, desde el cual debe ejecutarse el programa.
Importa el módulo ahorcadoind, que corresponde a la modalidad individual y el módulo ahorcadomult, que corresponde a la modalidad multijugador
Requiere de la librería pygame y la librería sys
"""
import pygame, sys
#import ahorcadoind, ahorcadomult

#Definición que nos permite crear botones
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def main_menu():
    #import ahorcadoind, ahorcadomult

    #Crear la ventana de pygame
    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Ahorcado')
    screen = pygame.display.set_mode((800, 800),0,32)
    
    #Crear los tipos y tamaños de letra que se utilizarán     
    fontTitle= pygame.font.Font ('freesansbold.ttf', 50) #fuente y tamaño del texto GRANDE
    fontBody= pygame.font.Font('freesansbold.ttf', 32) 


    pick = False

    #Empieza el ciclo
    while True:
        
        #Hacer que la ventana sea completamente negra al inicio
        screen.fill((0,0,0))
        
        #Mensaje de Bienvenida
        screen.blit(fontTitle.render("Bienvenido a Ahorcado", 0, (255,255,255)), (100,180))

        #Posición del Mouse
        mx, my = pygame.mouse.get_pos()
        
        #Crear el primer botón        
        screen.blit(fontBody.render("jugar", 0, (255,255,255)), (300,300))
        button_1 = pygame.Rect(300, 300, 200, 50)
        
        
        #Si se da click al primer botón
        if button_1.collidepoint((mx, my)):
            if pick:
                click = False
                running = True
                
                #Ciclo para escoger una modalidad de juego
                while running:
                    screen.fill((0,0,0))
                    
                    screen.blit(fontTitle.render("Escoje una modalidad de juego", 0, (255,255,255)), (10,180))
                    
                    mx, my = pygame.mouse.get_pos()
                    
                    button_a = pygame.Rect(270, 300, 250, 50)
                    button_b = pygame.Rect(270, 400, 250, 50)
                    
                    
                    #Si se escoge el modo individual
                    if button_a.collidepoint((mx, my)):
                        if click:
                            running = True
                            while running:
                                screen.fill((0,0,0))
                        
                                screen.blit(fontBody.render('Modo: Individual', 0,(0, 128, 128)), (50,80))
                                #ahorcadoind.setup_ind()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            running = False
                                
                                pygame.display.update()
                                mainClock.tick(60)        
                            
                    pygame.draw.rect(screen, (0, 128, 128), button_a)
                    textSurf, textRect = text_objects("Individual", fontBody)
                    textRect.center = (397, 326)
                    screen.blit(textSurf, textRect)
                    
                    #Si se escoge el modo multijugador                    
                    if button_b.collidepoint((mx, my)):
                       if click:
                           running = True
                           while running:
                               screen.fill((0,0,0))
                        
                               screen.blit(fontBody.render('Modo: Multijugador', 0,(0, 128, 128)), (50,80))
                               #ahorcadomult.setup_mult()
                               for event in pygame.event.get():
                                   if event.type == pygame.QUIT:
                                       pygame.quit()
                                       sys.exit()
                                   if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            running = False
                                
                               pygame.display.update()
                               mainClock.tick(60)


                    
                    pygame.draw.rect(screen, (0, 128, 128), button_b)
                    textSurf, textRect = text_objects("Multijugador", fontBody)
                    textRect.center = (396, 426)
                    screen.blit(textSurf, textRect)
                    
                    #Si se da click en la equis roja, salir                    
                    click = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                    
                    pygame.display.update()
                    mainClock.tick(60)
                    
                
        pygame.draw.rect(screen, (0, 130, 128), button_1)
        textSurf, textRect = text_objects("Jugar!", fontBody)
        textRect.center = (400, 330)
        screen.blit(textSurf, textRect)

        #Si se da click en la equis roja, salir  
        pick = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pick = True

        pygame.display.update()
        mainClock.tick(60)

  

main_menu()
pygame.quit()
quit()
