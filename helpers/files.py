import json

def writeJSONInFile(path, text):
    try:
        file = open(path, "w")
        file.write(text)
    except:
        print("there was an error")

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