"""
Creates the environment for a game including
the main window and basic settings.
"""
import pygame


class Game:
    def __init__(self, fps, screen):
        self.FPS = fps  # frames per second; used to control the game clock
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.clock.tick(self.FPS)
