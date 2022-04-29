"""
Creates the environment for a game including
the main window and basic settings.
"""
import pygame
from settings import RED


class Game:
    def __init__(self, fps, screen, title_font):
        self.FPS = fps  # frames per second; used to control the game clock
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.is_not_over = True
        self.title_font = title_font

    def run(self):
        self.is_running = True
        while self.is_running:
            # see if anything happened in this frame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.clock.tick(self.FPS)

    def show_home_screen(self):
        """
        Draws the "home" screen
        """
        # set the text and font for the title
        title = self.title_font.render("SPACE INVADERS", True, RED)
        # center the rectangle for the title text
        title_rect = title.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(title, title_rect)
        pygame.display.update()
