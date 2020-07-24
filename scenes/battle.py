import pygame
import const.files as cfiles
import const.colors as colors

class Battle:

    def __init__(self, pkmn1, pkmn2, pkmnFont, config):
        self.pkmn1 = pkmn1
        self.pkmn2 = pkmn2
        self.mainText = pkmnFont.render("", False, colors.BLACK, None)
        self.mainTextRect = self.mainText.get_rect()
        # self.mainTextRect.center = (int(config.SCREEN_WIDTH / 2), int(config.CURSOR_INITIAL_POSITION_Y / 2))
        self.mainTextRect.midleft = (config.DIALOG_MARGIN_SIDES, (config.SCREEN_HEIGHT - config.DIALOG_HEIGHT) + config.DIALOG_MARGIN_TOP)


    # PUBLIC METHODS
    def printDialogContainer(self, screen, config):
        pygame.draw.rect(screen, colors.WHITE, pygame.Rect(0, config.SCREEN_HEIGHT - config.DIALOG_HEIGHT, config.SCREEN_WIDTH, config.DIALOG_HEIGHT), 0)
        pygame.draw.rect(screen, colors.BLACK, pygame.Rect(0, config.SCREEN_HEIGHT - config.DIALOG_HEIGHT, config.SCREEN_WIDTH, config.DIALOG_HEIGHT), 4)


    def printPkmns(self, screen, config):
        self.__printPokemon(screen, config)
        self.__printLifebars(screen, config)

    def printText(self, screen, text, pkmnFont):
        self.mainText = pkmnFont.render(text, False, colors.BLACK, None)

        screen.blit(self.mainText, self.mainTextRect)

    # PRIVATE METHODS
    def __printLifebars(self, screen, config):

        # Load lifer bar image
        pkmn1Lifebar = pygame.image.load("src/assets/pkmn-lifebar.png")
        pkmn1Lifebar = pygame.transform.scale(pkmn1Lifebar, (config.PKMN_LB1_WIDTH, config.PKMN_LB1_HEIGHT))

        # Load enemy life bar image
        pkmn2Lifebar = pygame.image.load("src/assets/pkmn-enemy-lifebar.png")
        pkmn2Lifebar = pygame.transform.scale(pkmn2Lifebar, (config.PKMN_LB1_WIDTH, config.PKMN_LB1_HEIGHT))

        # Print lifebar bar (TODO: See how to improve the life bar position)
        pygame.draw.rect(screen, colors.GREEN, pygame.Rect(
            config.SCREEN_WIDTH - 210, 
            config.SCREEN_HEIGHT - config.DIALOG_HEIGHT - config.PKMN_LB1_HEIGHT + 8,
             180,
             10
        ), 0)

        # Print enemy lifebar bar (TODO: See how to improve the life bar position)
        pygame.draw.rect(screen, colors.GREEN, pygame.Rect(90, 28, 180, 10))

        # Print everything
        screen.blit(pkmn1Lifebar, (config.SCREEN_WIDTH - config.PKMN_LB1_WIDTH, config.SCREEN_HEIGHT - config.DIALOG_HEIGHT - config.PKMN_LB1_HEIGHT))
        screen.blit(pkmn2Lifebar, (0,0))

    def __printPokemon(self, screen, config):
        # Load Pokemon image
        pkmn1Image = pygame.image.load(cfiles.PKMN_IMAGES_PATH + "/back-{}.png".format(self.pkmn1.index))
        pkmn1Image = pygame.transform.scale(pkmn1Image, (config.PKMN_BACK_SCALE, config.PKMN_BACK_SCALE))

        # Load enemy Pokemon image
        pkmn2Image = pygame.image.load(cfiles.PKMN_IMAGES_PATH + "/front-{}.png".format(self.pkmn2.index))
        pkmn2Image = pygame.transform.scale(pkmn2Image, (config.PKMN_FRONT_SCALE, config.PKMN_FRONT_SCALE))

        #Print everything
        screen.blit(pkmn1Image, (0, config.SCREEN_HEIGHT - (config.PKMN_BACK_SCALE + config.PKMN_BACK_PLUS_TOP)))
        screen.blit(pkmn2Image, (config.SCREEN_WIDTH - config.PKMN_FRONT_SCALE, 0))
        