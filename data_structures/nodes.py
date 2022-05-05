import pygame
from settings import Settings


class Node:

    def __init__(self, x=0, y=0):
        self.settings = Settings()

        self.x = x
        self.y = y

        self.body_colour = self.settings.snake_colour
        self.rect = pygame.Rect(
            (self.x, self.y, self.settings.snake_size, self.settings.snake_size)
        )


class Body(Node):
    def __init__(self):
        super().__init__()


class Head(Node):

    def __init__(self):
        super().__init__()

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.game_over = False

        self.eye_colour = self.settings.snake_eye_colour

    def update_head(self):
        if self.move_up and self.rect.top >= 0:
            self.y -= self.settings.snake_size
        elif self.move_down and self.rect.bottom <= self.settings.screen_height:
            self.y += self.settings.snake_size
        elif self.move_left and self.rect.left >= 0:
            self.x -= self.settings.snake_size
        elif self.move_right and self.rect.right <= self.settings.screen_width:
            self.x += self.settings.snake_size

        self.rect = pygame.Rect(
            (self.x, self.y, self.settings.snake_size, self.settings.snake_size)
        )

    def game_over_check(self):
        if self.move_up and self.rect.top <= 0:
            self.game_over = True
        if self.move_down and self.rect.bottom >= self.settings.screen_height:
            self.game_over = True
        if self.move_left and self.rect.left <= 0:
            self.game_over = True
        if self.move_right and self.rect.right >= self.settings.screen_width:
            self.game_over = True

    def draw_snake_head(self, screen):
        self.update_head()
        pygame.draw.rect(screen, self.body_colour, self.rect)
        pygame.draw.circle(screen, self.eye_colour, self.rect.center, self.settings.snake_eye_size)
