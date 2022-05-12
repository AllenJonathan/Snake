import pygame
import sys
import random
import time
import events
from settings import Settings
from snake import Snake
from food import Food, GoldenFood
from score import Score



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
        self.score = Score()

    def rungame(self):
        while True:
            events.check_events(self.snake)
            self.check_food_eat()
            self.update_screen()
            self.check_game_over()
            self.main_clock.tick(self.settings.FPS)

    def update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.food.draw_food(self.screen)
        self.snake.draw_snake(self.screen)
        self.score.show_score(self.screen)
        pygame.display.flip()

    def draw_food(self, screen):
        if not self.food_exists:
            self.food.draw_food(screen)

    def check_food_eat(self):
        if self.snake.head.rect.center == self.food.rect.center:
            del self.food
            self.add_food()


    def add_food(self):
        n = random.randint(0,self.settings.golden_food_prob)
        if n <= self.settings.golden_food_prob - 1:
            self.food = Food()
            self.snake.add_body_node()
            self.score.increment_score(self.settings.score_incement)
        else:
            self.food = GoldenFood()
            for i in range(3):
                self.snake.add_body_node()
            self.score.increment_score(self.settings.score_incement + 100)


    def check_game_over(self):
        self.snake.check_game_over()
        if self.snake.game_over:
            return self.game_over()

    def game_over(self):
        time.sleep(2)
        sys.exit()
