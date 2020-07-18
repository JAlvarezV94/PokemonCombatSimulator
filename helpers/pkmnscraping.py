import requests
import json
from bs4 import BeautifulSoup


baseURL = "http://pokedream.com"
gen1URL = "/pokedex/pokemon?display=gen1"

pokedreamPage = requests.get(baseURL + gen1URL)
soup = BeautifulSoup(pokedreamPage.content, "html.parser")

pkmnTable = soup.find(id="pokemon-table")

tableRows = pkmnTable.find_all("tr")

for counter in range(1, 10):
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

    print("--------------------------------------------")
    print("NAME: " + pkmnName)
    print("Nº " + pkmnIndex)
    print("TYPE 1: " + type1)
    print("TYPE 2: " + type2)
    print("HP: " + hp)
    print("ATTACK: " + attack)
    print("DEFENSE: " + defense)
    print("SP ATTACK: " + spAttack)
    print("SP DEFENSE: " + spDefense)
    print("SPEED: " + speed)
    print("TOTAL: " + total)
    print("--------------------------------------------")