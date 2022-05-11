"""
Primarily used to launch the program.
"""
import pygame
from pygame.font import Font
from settings import FPS, GLITCH_FONT_PATH, WIDTH, HEIGHT
from game import Game


def main():
    """
    This will setup the infrastructure for and
    run the game.
    """
    # intialize pygame
    pygame.init()

    # setup fonts
    GLITCH_FONT = Font(GLITCH_FONT_PATH, 60)

    # create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # draw the initial screen
    pygame.display.update()

    # create an instance of the Game class
    game = Game(FPS, screen, GLITCH_FONT)
    game.show_home_screen()

    # while the player wants to continue playing
    while game.is_not_over:
        # start a new game
        game.run()

    # quit pygame
    pygame.quit()
    return 0


if __name__ == "__main__":
    main()
