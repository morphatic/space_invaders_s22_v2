"""
Primarily used to launch the program
"""
import pygame
from settings import FPS, WIDTH, HEIGHT
from game import Game


def main():
    """
    This will setup the infrastructure for and
    run the game.
    """
    # intialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    game = Game(FPS, screen)
    game.run()
    return 0


if __name__ == "__main__":
    main()
