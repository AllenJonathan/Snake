import pygame
import sys
import time
import events
from settings import Settings
from snake import Snake
from food import Food


class SnakeGame:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.main_clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        pygame.display.set_caption("Snake")

        self.snake = Snake()
        self.food = Food()

        self.food_exists = False

    def rungame(self):
        while True:
            events.check_events(self.snake)
            self.game_over_check()
            self.check_food_eat()
            self.update_screen()
            self.main_clock.tick(self.settings.FPS)

    def update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.snake.draw_snake(self.screen)
        self.food.draw_food(self.screen)
        pygame.display.flip()

    def game_over_check(self):
        self.snake.head.game_over_check()
        if self.snake.head.game_over:
            return self.game_over()

    def game_over(self):
        time.sleep(2)
        sys.exit()

    def draw_food(self, screen):
        if not self.food_exists:
            self.food_exists = True
            self.food.draw_food(screen)

    def check_food_eat(self):
        if self.snake.head.rect.center == self.food.rect.center:
            self.food = Food()
            self.snake.add_body_node()
