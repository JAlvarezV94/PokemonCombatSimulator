import pygame
import const.scenes as cscenes
import scenes.choosing as choosing

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
        screen = pygame.display.set_mode((self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT))
        pkmnFont = pygame.font.Font("./src/fonts/pkmn_classic.ttf", 20)

        choosingScene = choosing.Choosing(pkmnFont, self.config)
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

            pygame.display.update()

