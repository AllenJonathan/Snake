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
        score_surface = score_font.render('Score : ' + str(self.score), True, (255,255,255))
        score_rect = score_surface.get_rect(top=0, right=self.settings.screen_width)
        screen.blit(score_surface, score_rect)
