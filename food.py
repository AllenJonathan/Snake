import pygame
import random
from settings import Settings


class Food:

    def __init__(self):

        self.settings = Settings()
        self.food_colour = self.settings.food_colour

        self.snake_size = self.settings.snake_size

        self.x = random.randrange(0,self.settings.screen_width - self.snake_size, self.snake_size)
        self.y = random.randrange(0,self.settings.screen_height - self.snake_size, self.snake_size)

        self.rect = pygame.Rect(
            self.x, self.y, self.settings.snake_size, self.settings.snake_size
            )

    def draw_food(self, screen):
        pygame.draw.rect(screen, self.food_colour, self.rect)


class GoldenFood(Food):

    def __init__(self):
        super().__init__()
        self.food_colour = self.settings.golden_food_color
