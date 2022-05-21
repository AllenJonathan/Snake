import pygame
import random
from settings import Settings


class Food:

    def __init__(self):

        self.settings = Settings()
        self.food_colour = self.settings.food_colour

        self.snake_size = self.settings.snake_size

        self.x = random.randrange(
            self.settings.snake_size // 2, self.settings.screen_width - self.snake_size, self.snake_size
            )
        self.y = random.randrange(
            self.settings.snake_size // 2, self.settings.screen_height - self.snake_size, self.snake_size
            )

    def draw_food(self, screen):
        pygame.draw.circle(
            screen, self.food_colour, (self.x,self.y) , self.settings.snake_size//2 - self.settings.snake_size*0.08
            )


class GoldenFood(Food):

    def __init__(self):
        super().__init__()
        self.food_colour = self.settings.golden_food_color


food_1 = Food()
food_2 = GoldenFood()

print(food_2.__class__ == GoldenFood)
