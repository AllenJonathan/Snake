import pygame
from settings import Settings

class Score:

    def __init__(self):
        self.settings = Settings()
        self.score = 0

    def increment_score(self, value):
        self.score += value

    def show_score(self,screen):
        score_font = pygame.font.SysFont(self.settings.score_font, self.settings.score_size)
        score_surface = score_font.render('Score : ' + str(self.score), True, self.settings.score_colour)
        score_rect = score_surface.get_rect(
            top = self.settings.score_padding,
            right = self.settings.screen_width - self.settings.score_padding
        )
        screen.blit(score_surface, score_rect)
