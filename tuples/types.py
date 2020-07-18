import json

types = json.loads({ 
    "GRASS": {
        "name": "GRASS"
    },
    "FIRE": {
        "name": "FIRE"
    } 
})

# types = {
#     "GRASS": {   
#         "name": "GRASS",
#         "strong": ["WATER"],
#         "lose": ["FIRE"]
#     },
#     "FIRE": {   
#         "name": "FIRE",
#         "strong": ["GRASS"],
#         "lose": ["WATER"]
#     },
#     "WATER": {   
#         "name": "WATER",
#         "strong": ["FIRE"],
#         "lose": ["GRASS"]
#     },
# }