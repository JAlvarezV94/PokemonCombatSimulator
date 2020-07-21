import pygame
import const.scenes as cscenes

from scenes.choosing import choosing

class Game:

    def __init__(self, config, colors, pkmnMatrix):
        self.exit = False
        self.size = width, height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        self.config = config
        self.sceenColor = colors.WHITE
        self.pkmnMatrix = pkmnMatrix
        self.currentScene = cscenes.CHOOSING_SCENE

    def initGame(self):
        pygame.init()
        pygame.display.set_caption('Pkmn Combat Simulator')
        screen = pygame.display.set_mode(self.size)
        pkmnFont = pygame.font.Font("./src/fonts/pkmn_classic.ttf", 20)

        choosingScene = choosing.Choosing(pkmnFont, self.config)
        while not self.exit:
            for event in pygame.event.get():
                # Add listener to close the window
                if event.type == pygame.QUIT:
                    self.exit = True
            
            # Adding configs
            screen.fill(self.sceenColor)
            
            # Displaying scene
            if self.currentScene == cscenes.CHOOSING_SCENE:
                choosingScene.printText(screen, self.pkmnMatrix, pkmnFont)
                choosingScene.printPkmns(pygame, screen, self.pkmnMatrix, self.config)
                choosingScene.printCursor(pkmnFont, screen)


            pygame.display.update()

