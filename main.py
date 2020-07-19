import os

import sys, pygame

import models.pokemon as pokemon
import const.initials as cinitials
import const.files as cfiles
import helpers.files as hfiles
import helpers.jsonparser as jparser
import const.colors as colors

def chooseInitialPokemon():

    # Get initial's info

    initial1 = jparser.parsePokemon(hfiles.readPkmnByIndex(cfiles.PKMN_JSON_PATH, cinitials.BULBASAUR))
    initial2 = jparser.parsePokemon(hfiles.readPkmnByIndex(cfiles.PKMN_JSON_PATH, cinitials.CHARMANDER))
    initial3 = jparser.parsePokemon(hfiles.readPkmnByIndex(cfiles.PKMN_JSON_PATH, cinitials.SQUIRTLE))

    initials = [initial1, initial2, initial3]

    # Choosing initial

    myInitial = None
    
    while myInitial == None:
        counter = 1
        print("What pokemon do you choose?")

        for currentPkmn in initials:
            print(str(counter) + " - {} the {} type pokemon.".format(initials[counter - 1].name, initials[counter - 1].type))
            counter += 1

        response = input()
        
        if response == str(1) or response == str(2) or response == str(3):
            myInitial = initials[int(response) - 1]
        else:
            os.system("clear")

    return myInitial



# Starting game

# chosenPkmn = chooseInitialPokemon()
# chosenPkmn.describePokemon()


pygame.init()

size = width, height = 350, 240
speed = [2,2]
horizontalSpace = 70
verticalSpace = 70
cursorY = 0
cursorX = 0

screen = pygame.display.set_mode(size)

while 1:
    
    for event in pygame.event.get():
        # Add listener to close the window
        if event.type == pygame.QUIT: sys.exit()

        # Add listener to the cursor
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            cursorX += 70
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            cursorX -= 70
        if pygame.key.get_pressed()[pygame.K_UP]:
            cursorY -= 70
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            cursorY += 70

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

        if counter == 5:
            pkmnMatrix.append(pkmnRow[:])
            counter = 0
            pkmnRow = []

    # Add images
    currentVertical = 0
    for currentRow in pkmnMatrix:
        currentHorizontal = 0
        
        for currentPkmn in currentRow:
            imageToLoad = pygame.image.load(cfiles.PKMN_IMAGES_PATH + "/front-{}.png".format(currentPkmn["Nº"]))
            screen.blit(imageToLoad, (currentHorizontal, currentVertical))
            currentHorizontal += horizontalSpace
        
        currentVertical += verticalSpace

    # Add cursor
    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(cursorX, cursorY, 60, 60), 4)



    pygame.display.update()