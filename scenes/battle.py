import pygame
import const.files as cfiles
import const.colors as colors

class Battle:

    def __init__(self, pkmn1, pkmn2):
        self.pkmn1 = pkmn1
        self.pkmn2 = pkmn2


    def printDialogContainer(self, screen, config):
        pygame.draw.rect(screen, colors.WHITE, pygame.Rect(0, config.SCREEN_HEIGHT - config.DIALOG_HEIGHT, config.SCREEN_WIDTH, config.DIALOG_HEIGHT), 0)
        pygame.draw.rect(screen, colors.BLACK, pygame.Rect(0, config.SCREEN_HEIGHT - config.DIALOG_HEIGHT, config.SCREEN_WIDTH, config.DIALOG_HEIGHT), 4)


    def printPkmns(self, screen, config):
        self.printYourPokemon(screen, config)

        pkmn2Image = pygame.image.load(cfiles.PKMN_IMAGES_PATH + "/front-{}.png".format(self.pkmn2.index))


    def printYourPokemon(self, screen, config):
        # Load Pokemon image
        pkmn1Image = pygame.image.load(cfiles.PKMN_IMAGES_PATH + "/back-{}.png".format(self.pkmn1.index))
        pkmn1Image = pygame.transform.scale(pkmn1Image, (config.PKMN_BACK_SCALE, config.PKMN_BACK_SCALE))

        # Load lifer bar images
        pkmn1Lifebar = pygame.image.load("src/assets/pkmn-lifebar.png")
        pkmn1Lifebar = pygame.transform.scale(pkmn1Lifebar, (config.PKMN_LB1_WIDTH, config.PKMN_LB1_HEIGHT))

        # Print lifebar bar (TODO: See how to improve the life bar position)
        pygame.draw.rect(screen, colors.GREEN, pygame.Rect(
            config.SCREEN_WIDTH - 210, 
            config.SCREEN_HEIGHT - config.DIALOG_HEIGHT - config.PKMN_LB1_HEIGHT + 8,
             180,
             10
        ), 0)

        #Print everything
        screen.blit(pkmn1Image, (0, config.SCREEN_HEIGHT - (config.PKMN_BACK_SCALE + config.PKMN_BACK_PLUS_TOP)))
        screen.blit(pkmn1Lifebar, (config.SCREEN_WIDTH - config.PKMN_LB1_WIDTH, config.SCREEN_HEIGHT - config.DIALOG_HEIGHT - config.PKMN_LB1_HEIGHT))