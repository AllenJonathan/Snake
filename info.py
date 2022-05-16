import pygame
from settings import Settings


class Info:

    def __init__(self, snake):
        self.settings = Settings()
        self.snake = snake
        self.snake_length = 0
        self.high_score = 0
        self.update_high_score()

    def update_high_score(self):
        with open('other_files/high_score.txt') as f:
            line = f.readline()
        self.high_score = int(line)

    def update_snake_length(self):
        self.snake_length = self.snake.snake.length


    def show_info(self, screen):

        self.update_snake_length()

        high_score_font = pygame.font.SysFont(self.settings.score_font, self.settings.score_size)
        high_score_surface = high_score_font.render('High Score : ' + str(self.high_score), True, self.settings.score_colour)
        high_score_rect = high_score_surface.get_rect(
            top = self.settings.score_padding,
            left = self.settings.score_padding
        )

        snake_length_font = pygame.font.SysFont(self.settings.score_font, self.settings.score_size)
        snake_length_surface = snake_length_font.render('Snake Length: ' + str(self.snake_length), True, self.settings.score_colour)
        snake_length_rect = snake_length_surface.get_rect(
            top = high_score_rect.bottom,
            left = self.settings.score_padding
        )

        screen.blit(high_score_surface, high_score_rect)
        screen.blit(snake_length_surface, snake_length_rect)
