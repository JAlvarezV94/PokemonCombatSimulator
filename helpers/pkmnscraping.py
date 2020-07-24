import requests
import json
import pathlib
from bs4 import BeautifulSoup
import urllib.request
import files
import pathlib
import os

baseURL = "http://pokedream.com"
imagesURL = "/pokedex/images/gold/{}/{}.png"
gen1URL = "/pokedex/pokemon?display=gen1"
PKMN_JSON_PATH = str(os.path.dirname(pathlib.Path(__file__))) + "/../pkmn.json"
PKMN_IMAGES_PATH = str(os.path.dirname(pathlib.Path(__file__))) + "/../src/images"
FRONT = "front"
BACK = "back"

def getPokemonList():
    pkmonJsonString = "{\n\t\"firstGen\": [\n"
    pokedreamPage = requests.get(baseURL + gen1URL)
    soup = BeautifulSoup(pokedreamPage.content, "html.parser")

    pkmnTable = soup.find(id="pokemon-table")

    tableRows = pkmnTable.find_all("tr")

    for counter in range(1, 152):
        currentRow = tableRows[counter].find_all("td")

        # Get pokemon name
        firstColumn = currentRow[0]
        aElement = firstColumn.find_all("a")
        pkmnName = aElement[0].getText()

        # Get pokemon index
        secondColumn = currentRow[1]
        pkmnIndex = secondColumn.getText()

        # Get type 1
        fourthColumn = currentRow[3]
        type1 = fourthColumn.get("class")[0].upper()

        # Get type 2
        fifthColumn = currentRow[4]
        type2 = fifthColumn.get("class")

        if type2 != None:
            type2 = type2[0].upper()
        else:
            type2 = "---"

        # Attributes
        hp = currentRow[5].getText()
        attack = currentRow[6].getText()
        defense = currentRow[7].getText()
        spAttack = currentRow[8].getText()
        spDefense = currentRow[9].getText()
        speed = currentRow[10].getText()
        total = currentRow[11].getText()

        # Writing in pkmnJson
        pkmonJsonString += '\t\t{{\n' \
            '\t\t\t"NAME": "{0}", \n' \
            '\t\t\t"Nº": "{1}", \n' \
            '\t\t\t"TYPE 1": "{2}", \n' \
            '\t\t\t"TYPE 2": "{3}", \n' \
            '\t\t\t"HP": {4}, \n' \
            '\t\t\t"ATTACK": {5}, \n' \
            '\t\t\t"DEFENSE": {6}, \n' \
            '\t\t\t"SP ATTACK": {7}, \n' \
            '\t\t\t"SP DEFENSE": {8}, \n' \
            '\t\t\t"SPEED": {9}, \n' \
            '\t\t\t"TOTAL": {10} \n \t\t}},\n'.format(pkmnName, pkmnIndex, type1, type2, hp, attack, defense, spAttack, spDefense,speed, total)


    pkmonJsonString = pkmonJsonString[:len(pkmonJsonString) -5 ]
    pkmonJsonString += "\n\t\t}"
    pkmonJsonString += "\n\t]\n}"

    files.writeJSONInFile(PKMN_JSON_PATH, pkmonJsonString)

# Scrapping images
def scrappingImages():
    
    # Getting the name of all pkmn
    firstGenJSON = files.readAllPkmn(PKMN_JSON_PATH)

    for currentPokemon in firstGenJSON:
        currentNumber = currentPokemon["Nº"]
        currentName = currentPokemon["NAME"]

        urllib.request.urlretrieve(baseURL + imagesURL.format(FRONT, currentNumber), PKMN_IMAGES_PATH + "/{}-{}.png".format(FRONT, currentNumber))
        urllib.request.urlretrieve(baseURL + imagesURL.format(BACK, currentNumber), PKMN_IMAGES_PATH + "/{}-{}.png".format(BACK, currentNumber))

        print(currentName + "...Ok")

print(PKMN_JSON_PATH)
getPokemonList()
scrappingImages()