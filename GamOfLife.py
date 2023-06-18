import pygame #pip install pygame
import numpy as np #pip install numpy
import time

pygame.init()

#ancho y alto de la pantalla
width, height = 800, 800
#creación de la pantalla 
screen = pygame.display.set_mode((height, width))

#color del fondo = Casi negro, casi oscuro
bg = 25, 25 ,25
#Pintamos el fondo con el color elegido
screen.fill(bg)

#cantidad de celdas
nxC, nyC = 50, 50

#dimensiones de las celdas
dimCW = width / nxC
dimCH = height / nyC


#Estado de las celdas. Vivas = 1, Muertas = 0
gameState = np.zeros((nxC, nyC))


#automata palo.
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1

#control de ejecucion del juego
pauseExect = False
##############################

running = True
#bucle de ejecución
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
            
    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)

    # Registramos eventos de teclado y ratón
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()
        

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]
            
        
##############################################################################################

    for y in range(0, nxC):
        for x in range(0, nyC):
            #Calculamos el numero de vecinos cercanos.

            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False

            if not pauseExect:
                n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
                        gameState[(x)   % nxC, (y-1) % nyC] + \
                        gameState[(x+1) % nxC, (y-1) % nyC] + \
                        gameState[(x-1) % nxC, (y)   % nyC] + \
                        gameState[(x+1) % nxC, (y)   % nyC] + \
                        gameState[(x-1) % nxC, (y+1) % nyC] + \
                        gameState[(x)   % nxC, (y+1) % nyC] + \
                        gameState[(x+1) % nxC, (y+1) % nyC]

                #RULE 1 = una celula está muerta con exactamente 3 vecinas vivas revives, "revive"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1

                #RUE 2 = una célula viva con menos de 2 vivas o con más de 3 vecinas vivas, "muere"
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y] = 0

                #Creamos el poligono de cada celda a dibujar
                poly = [((x)     * dimCW, y * dimCH),
                        ((x + 1) * dimCW, y * dimCH),
                        ((x + 1) * dimCW, (y + 1) * dimCH),
                        ((x)     * dimCW, (y + 1) * dimCH)]

                #dibujamos la celda para cada par de x, y.
                if newGameState[x,y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, width = 1)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

        
    #Actualizamos el estado del juego
    gameState = np.copy(newGameState)

    #Actualizamos la pantalla
    pygame.display.flip()
    pygame.display.set_caption("Conway's Game of Life")
    