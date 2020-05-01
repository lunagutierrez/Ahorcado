#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
import ahorcadoind, ahorcadomult

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
#from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800, 800),0,32)

font = pygame.font.SysFont(None, 20)
fontTitle= pygame.font.Font ('freesansbold.ttf', 50) #fuente y tamaño del texto GRANDE
fontBody= pygame.font.Font('freesansbold.ttf', 32) 

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pick = False

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def main_menu():
    while True:

        screen.fill((0,0,0))
        screen.blit(fontTitle.render("Bienvenido a ahorcado", 0, (255,255,255)), (100,180))

        mx, my = pygame.mouse.get_pos()
        
        screen.blit(fontBody.render("jugar", 0, (255,255,255)), (300,300))
        button_1 = pygame.Rect(300, 300, 200, 50)
        
        
        
        if button_1.collidepoint((mx, my)):
            if pick:
                juego()
                
        pygame.draw.rect(screen, (0, 130, 128), button_1)
        textSurf, textRect = text_objects("Jugar!", fontBody)
        textRect.center = (400, 330)
        screen.blit(textSurf, textRect)

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



def juego():
    click = False
    running = True
    while running:
        screen.fill((0,0,0))
        
        screen.blit(fontTitle.render("Escoje una modalidad de juego", 0, (255,255,255)), (10,180))
        
        mx, my = pygame.mouse.get_pos()
        
        button_a = pygame.Rect(270, 300, 250, 50)
        button_b = pygame.Rect(270, 400, 250, 50)
        
        if button_a.collidepoint((mx, my)):
            if click:
                ind()         
                
        pygame.draw.rect(screen, (0, 128, 128), button_a)
        textSurf, textRect = text_objects("Individual", fontBody)
        textRect.center = (397, 326)
        screen.blit(textSurf, textRect)
        
        if button_b.collidepoint((mx, my)):
           if click:
               multi()
        
        pygame.draw.rect(screen, (0, 128, 128), button_b)
        textSurf, textRect = text_objects("Multijugador", fontBody)
        textRect.center = (396, 426)
        screen.blit(textSurf, textRect)
        
        click = False
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
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)
        
def ind():
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(fontTitle.render("Escoje una modalidad de juego", 0, (255,255,255)), (10,180))
        
        pygame.display.update()
        mainClock.tick(60)
        
def multi():
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(fontTitle.render("Escoje una modalidad de juego", 0, (255,255,255)), (10,180))
        
        pygame.display.update()
        mainClock.tick(60)
        
def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()
pygame.quit()
quit()
