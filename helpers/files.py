import json

def writeJSONInFile(path, text):
    try:
        file = open(path, "w")
        file.write(text)
    except:
        print("there was an error")
