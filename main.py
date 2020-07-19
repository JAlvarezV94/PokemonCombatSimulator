import os

import sys, pygame

import models.pokemon as pokemon
import const.initials as cinitials
import const.files as cfiles
import helpers.files as hfiles
import helpers.jsonparser as jparser
import const.colors as colors
import configuration as config

# Initializing parameters
size = width, height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
speed = [2,2]
horizontalSpace = config.HORIZONTAL_SPACE
verticalSpace = config.VERTICAL_SPACE
cursorY = config.CUSROR_INITIAL_POSITION_Y
cursorX = config.CUSROR_INITIAL_POSITION_X
firstRow = 0

# Starting game
pygame.init()
pygame.display.set_caption('Pkmn Combat Simulator')
screen = pygame.display.set_mode(size)

while 1:
    
    for event in pygame.event.get():
        # Add listener to close the window
        if event.type == pygame.QUIT: sys.exit()

        # Add listener to move the cursor
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            cursorX += config.HORIZONTAL_SPACE
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            cursorX -= config.HORIZONTAL_SPACE
        if pygame.key.get_pressed()[pygame.K_UP]:
            cursorY -= config.VERTICAL_SPACE
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            cursorY += config.VERTICAL_SPACE

    # Add some color and title
    screen.fill(colors.WHITE)

    # Get pokemons in a matrix
    pkmnMatrix = []
    pkmnRow = []
    pkmnJSON = hfiles.readAllPkmn(cfiles.PKMN_JSON_PATH)
    counter = 0

    for currentPkmn in pkmnJSON:
        
        pkmnRow.append(currentPkmn)
        counter += 1

        if counter == config.MAX_COLUMNS:
            pkmnMatrix.append(pkmnRow[:])
            counter = 0
            pkmnRow = []

    # Display the matrix
    currentVertical = config.INIT_VERTICAL
    maxRows = firstRow + config.MAX_ROWS
    for index in range(firstRow, maxRows):
        currentHorizontal = config.INIT_HORIZONTAL
        currentRow = pkmnMatrix[index]
        for currentPkmn in currentRow:
            imageToLoad = pygame.image.load(cfiles.PKMN_IMAGES_PATH + "/front-{}.png".format(currentPkmn["Nº"]))
            screen.blit(imageToLoad, (currentHorizontal, currentVertical))
            currentHorizontal += horizontalSpace
        currentVertical += verticalSpace

    # Add cursor
    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(cursorX, cursorY, config.CURSOR_WIDTH, config.CURSOR_HEIGHT), 4)



    pygame.display.update()