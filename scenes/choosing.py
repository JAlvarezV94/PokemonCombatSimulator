import const.colors as colors
import const.files as cfiles

class Choosing:

    def __init__(self, pkmnFont, config):
        self.horizontalSpace = config.HORIZONTAL_SPACE
        self.verticalSpace = config.VERTICAL_SPACE
        self.cursorY = config.CURSOR_INITIAL_POSITION_Y
        self.cursorX = config.CURSOR_INITIAL_POSITION_X
        self.firstRow = 0
        self.selectedPkmn = [0,0]
        self.title = pkmnFont.render("CHOOSE YOUR POKEMON", False, colors.BLACK, None)
        self.titleRect = self.title.get_rect()
        self.titleRect.center = (int(config.SCREEN_WIDTH / 2), int(config.CURSOR_INITIAL_POSITION_Y / 2))
        self.pkmnNameTxt = pkmnFont.render("", False, colors.BLACK, None)
        self.pkmnNameRect = self.pkmnNameTxt.get_rect()
        self.pkmnNameRect.center = (int(config.SCREEN_WIDTH / 2), int(config.CURSOR_INITIAL_POSITION_Y * 5))

    def printText(self, screen, pkmnMatrix, pkmnFont):
        #Get current Pokemon name
        completePokemon = pkmnMatrix[self.selectedPkmn[0]][self.selectedPkmn[1]]
        self.pkmnNameTxt = pkmnFont.render(completePokemon["NAME"], False, colors.BLACK, None)

        #Display screen text
        screen.blit(self.title, self.titleRect)
        screen.blit(self.pkmnNameTxt, self.pkmnNameRect)

    def printPkmns(self, pygame, screen, pkmnMatrix, config):
        currentVertical = config.INIT_VERTICAL
        maxRows = self.firstRow + config.MAX_ROWS
        for index in range(self.firstRow, maxRows):
            currentHorizontal = config.INIT_HORIZONTAL
            currentRow = pkmnMatrix[index]
            for currentPkmn in currentRow:
                imageToLoad = pygame.image.load(cfiles.PKMN_IMAGES_PATH + "/front-{}.png".format(currentPkmn["Nº"]))
                screen.blit(imageToLoad, (currentHorizontal, currentVertical))
                currentHorizontal += self.horizontalSpace
            currentVertical += self.verticalSpace
    
    def printCursor(self, pygame, screen):
        pygame.draw.rect(screen, colors.BLACK, pygame.Rect(self.cursorX, self.cursorY, config.CURSOR_WIDTH, config.CURSOR_HEIGHT), 4)