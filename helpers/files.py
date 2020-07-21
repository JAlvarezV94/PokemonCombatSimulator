import json

def writeJSONInFile(path, text):
    try:
        file = open(path, "w")
        file.write(text)
    except:
        print("there was an error.")

def readPkmnByIndex(path, index):
    try:
        chosenPkmn = None
        file = open(path, "r")
        jsonString = file.read()
        pkmnJson = json.loads(jsonString)
        firstGen = pkmnJson["firstGen"]
        
        for currentPkmn in firstGen:
            if currentPkmn["Nº"] == index:
                chosenPkmn = currentPkmn
                break
    except:
        print("something went worng.")
    
    strChosenPkmn = str(chosenPkmn).replace("'", "\"")
    return str(strChosenPkmn)

def readAllPkmn(path):
    try:
        file = open(path, "r")
        jsonString = file.read()
        pkmnJson = json.loads(jsonString)
        firstGen = pkmnJson["firstGen"]

    except:
        print("something went worng.")
    
    return firstGen

def readPkmnInMatrix(path, maxColumns):
    pkmnMatrix = []
    pkmnRow = []
    pkmnJSON = readAllPkmn(path)
    counter = 0

    for currentPkmn in pkmnJSON:
        
        pkmnRow.append(currentPkmn)
        counter += 1

        if counter == maxColumns or int(currentPkmn["Nº"]) == len(pkmnJSON):
            pkmnMatrix.append(pkmnRow[:])
            counter = 0
            pkmnRow = []
    
    return pkmnMatrix