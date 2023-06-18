############################################
import pygame
import numpy as np
import time

pygame.init()
width, height = 700, 700
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas, Viva = 1; Muerta = 0
gameState = np.zeros((nxC, nyC))

gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

pauseExect = False

while True:

    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)

    # log de mouse and key
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()
        

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]


    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:  
                # Calcular el número de vecinos cercanos.
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                    gameState[(x) % nxC, (y - 1) % nyC] + \
                    gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                    gameState[(x - 1) % nxC, (y) % nyC] + \
                    gameState[(x + 1) % nxC, (y) % nyC] + \
                    gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                    gameState[(x) % nxC, (y + 1) % nyC] + \
                    gameState[(x + 1) % nxC, (y + 1) % nyC]
#############################################################
                if gameState[x, y] == 0 and n_neigh == 3:
                        newGameState[x, y] = 1 ####---------> Aca tuviste un problema con los signos iguales. Es una puesta a valor por lo que es asi------>{newGameState[x, y] = 1}
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh >3):
                        newGameState[x, y] = 0 ####--------> Acá tuviste el mismo error que antes. Y se soluciona igual --------> {newGameState[x, y] = 1}
#############################################################
        
#############################################################      
                poly = [((x) * dimCW, y * dimCH),
                        ((x+1) * dimCW, y*dimCH),
                        ((x+1) * dimCW, (y+1)*dimCH),
                        ((x) * dimCW, (y+1) * dimCH)]
              
                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    
    gameState = np.copy(newGameState)
      
   #Actualizamos la pantalla
   
    pygame.display.flip()