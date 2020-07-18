import json

import models.pokemon as pkmn

def parsePokemon(jsonPkmnStr):
    jsonPkmn = json.loads(jsonPkmnStr)

    return pkmn.Pokemon(
        jsonPkmn["NAME"],
        jsonPkmn["Nº"],
        jsonPkmn["TYPE 1"],
        jsonPkmn["TYPE 2"],
        jsonPkmn["HP"],
        jsonPkmn["ATTACK"],
        jsonPkmn["DEFENSE"],
        jsonPkmn["SP ATTACK"],
        jsonPkmn["SP DEFENSE"],
        jsonPkmn["SPEED"],
        jsonPkmn["TOTAL"],
        5
    )