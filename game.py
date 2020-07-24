import pygame
import random

import const.scenes as cscenes
import const.files as cfiles
import scenes.choosing as choosing
import scenes.battle as battle
import helpers.jsonparser as parser
import helpers.files as hfiles

class Game:

    def __init__(self, config, colors, pkmnMatrix):
        self.exit = False
        self.config = config
        self.sceenColor = colors.WHITE
        self.pkmnMatrix = pkmnMatrix
        self.currentScene = cscenes.CHOOSING_SCENE

    def initGame(self):
        pygame.init()
        pygame.display.set_caption('Pkmn Combat Simulator')
        icon = pygame.image.load("./src/pcs-icon.png")
        pygame.display.set_icon(icon)
        screen = pygame.display.set_mode((self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT))
        pkmnFont = pygame.font.Font("./src/fonts/pkmn_classic.ttf", 20)

        choosingScene = choosing.Choosing(pkmnFont, self.config)
        pkmn1 = parser.parsePokemon(hfiles.readPkmnByIndex(cfiles.PKMN_JSON_PATH, "004"))
        pkmn2 = parser.parsePokemon(hfiles.readPkmnByIndex(cfiles.PKMN_JSON_PATH, "001"))
        battleScene = battle.Battle(pkmn1, pkmn2, pkmnFont, self.config)

        while not self.exit:
            for event in pygame.event.get():
                # Add listener to close the window
                if event.type == pygame.QUIT:
                    self.exit = True

                # Add listener to the movements
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    print("RIGHT")
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        choosingScene.moveToRight(self.config, self.pkmnMatrix)

                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    print("LEFT")
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        choosingScene.moveToLeft(self.config, self.pkmnMatrix)

                if pygame.key.get_pressed()[pygame.K_UP]:
                    print("UP")
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        choosingScene.moveToUp(self.config, self.pkmnMatrix)

                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    print("DOWN")
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        choosingScene.moveToDown(self.config, self.pkmnMatrix)

                # Add listener to A B buttons
                if pygame.key.get_pressed()[pygame.K_z]:
                    print("Z")
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        chosedPkmn = choosingScene.choosePokemon(self.pkmnMatrix)
                    
                        if chosedPkmn != None:
                            battleScene.pkmn1 = chosedPkmn
                            battleScene.pkmn2 = self.randomEnemy()
                            self.currentScene = cscenes.BATTLE_SCENE
                    if self.currentScene == cscenes.BATTLE_SCENE:
                        battleScene.pressAButton()

            # Adding configs
            screen.fill(self.sceenColor)
            
            # Displaying scenes
            if self.currentScene == cscenes.CHOOSING_SCENE:
                choosingScene.printText(screen, self.pkmnMatrix, pkmnFont)
                choosingScene.printPkmns(screen, self.pkmnMatrix, self.config)
                choosingScene.printCursor(screen, self.config)
            elif self.currentScene == cscenes.BATTLE_SCENE:
                battleScene.printPkmns(screen, self.config)
                battleScene.printDialogContainer(screen, self.config)
                battleScene.printText(screen, pkmnFont)

            pygame.display.flip()

    def randomEnemy(self):
        chosenRow = random.randint(0, len(self.pkmnMatrix))
        chosenColumn = random.randint(0, len(self.pkmnMatrix[chosenRow]))
        chosenPkmn = self.pkmnMatrix[chosenRow][chosenColumn]

        pkmnJson = hfiles.readPkmnByIndex(cfiles.PKMN_JSON_PATH, chosenPkmn["Nº"])

        return parser.parsePokemon(pkmnJson)