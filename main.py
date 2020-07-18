import os

import models.pokemon as pokemon
import tuples.types as pokemonType


def createInitialPokemons():
    global pokemon1
    global pokemon2
    global pokemon3
    
    pokemon1 = pokemon.Pokemon('Charmander', pokemonType["FIRE"], 5, ['scratch', 'whipe'])
    pokemon2 = pokemon.Pokemon('Squirtle', pokemonType.WATER, 5, ['scratch', 'whipe'])
    pokemon3 = pokemon.Pokemon('Bulbasaur', pokemonType.GRASS, 5, ['tackle', 'whipe'])

def chooseInitialPokemon():

    canContinue = False
    response = ''
    counter = 1
    initials = [pokemon1, pokemon2, pokemon3]

    while canContinue == False:
        print("What Pokemon do you choose?\n")

        for currentPokemon in initials:
            print(str(counter) + ' - {0} the {1} type.'.format(currentPokemon.name, currentPokemon.type))
            counter += 1

        response = input()
        
        if response == str(1) or response == str(2) or response == str(3):
            canContinue = True
        else:
            counter = 1
            os.system('clear')
    
    intResponse = int(response) - 1
    return initials[intResponse]



# Starting game
createInitialPokemons()
myPokemon = chooseInitialPokemon()
myPokemon.describePokemon()
