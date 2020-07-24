import pygame

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
        self.currentScene = cscenes.BATTLE_SCENE

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
        battleScene = battle.Battle(pkmn1, pkmn2)

        while not self.exit:
            for event in pygame.event.get():
                # Add listener to close the window
                if event.type == pygame.QUIT:
                    self.exit = True
                # Add listener to the movements
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        choosingScene.moveToRight(self.config, self.pkmnMatrix)

                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        choosingScene.moveToLeft(self.config, self.pkmnMatrix)

                if pygame.key.get_pressed()[pygame.K_UP]:
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        choosingScene.moveToUp(self.config, self.pkmnMatrix)

                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    if self.currentScene == cscenes.CHOOSING_SCENE:
                        choosingScene.moveToDown(self.config, self.pkmnMatrix)

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

            pygame.display.update()

