import os

import sys, pygame

import models.pokemon as pokemon
import const.initials as cinitials
import const.files as cfiles
import helpers.files as hfiles
import helpers.jsonparser as jparser

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

size = width, height = 320, 240
speed = [2,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    

    screen.fill(black)
    pygame.display.flip()