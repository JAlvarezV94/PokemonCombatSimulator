# PokemonCombatSimulator

## Installing dependencies

```bash
pip3 install pygame
pip3 install requests
pip3 install bs4
```

## Get the Pokemon in local

Before to run the game you must scrap all the Pokemon and save them in a json in local, this is how our game works with data. To launch the scrapper just type the next line in the terminal:

```bash
python3 helpers/pkmnscraping.py 
```


After the execution you should have a file called pkmn.json in the project path and a src/images folder with all the 1st generation Pokemon sprites in it.
