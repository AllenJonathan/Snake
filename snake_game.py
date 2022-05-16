import pygame
import sys
import random
import time
import events
from settings import Settings
from snake import Snake
from food import Food, GoldenFood
from score import Score
from info import Info


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
        self.info = Info(self.snake)

    def rungame(self):
        while True:
            print((self.food.x, self.food.y), self.snake.head.rect.center)
            events.check_events(self.snake)
            self.check_food_eat()
            self.update_screen()
            self.increase_game_speed()
            self.check_game_over()
            self.main_clock.tick(self.settings.FPS)

    def update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.food.draw_food(self.screen)
        self.snake.draw_snake(self.screen)
        self.score.show_score(self.screen)
        self.info.show_info(self.screen)
        pygame.display.flip()

    def draw_food(self, screen):
        if not self.food_exists:
            self.food.draw_food(screen)

    def check_food_eat(self):
        if self.snake.head.rect.center == (self.food.x, self.food.y):
            if isinstance(self.food, Food):
                self.score.increment_score(self.settings.score_incement)
            elif isinstance(self.food, GoldenFood):
                self.score.increment_score(self.settings.score_incement * self.settings.gold_multiplier)
            del self.food
            self.add_food()
            self.snake.add_body_node()


    def add_food(self):
        n = random.randint(0,self.settings.golden_food_prob)
        if n <= self.settings.golden_food_prob - 1:
            self.food = Food()
        else:
            self.food = GoldenFood()
            self.score.increment_score(self.settings.score_incement * self.settings.gold_multiplier)

    def increase_game_speed(self):
        if self.settings.FPS < 60:
            self.settings.FPS += self.settings.game_speed_increase

    def check_game_over(self):
        self.snake.check_game_over()
        if self.snake.game_over:
            return self.game_over()

    def game_over(self):
        my_font = pygame.font.SysFont(self.settings.game_over_font, self.settings.game_over_size)
        game_over_surface = my_font.render(
            'Your Score is : ' + str(self.score.score), True, self.settings.game_over_colour)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.center = (self.settings.screen_width/2, self.settings.screen_height/2)

        self.screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        self.update_high_score()

        time.sleep(5)
        pygame.quit()
        quit()

    def update_high_score(self):
        if self.score.score > self.info.high_score:
            with open('other_files/high_score.txt', 'w') as f:
                f.write(str(self.score.score))
