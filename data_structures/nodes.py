import pygame
from settings import Settings


class Body:

    def __init__(self, x=0, y=0):
        self.settings = Settings()

        self.x = x
        self.y = y

        self.rect = pygame.Rect(
            (self.x, self.y, self.settings.snake_size, self.settings.snake_size)
        )
        self.in_rect = pygame.Rect(self.rect.x, self.rect.y, self.settings.snake_size - 2, self.settings.snake_size - 2)

class Head(Body):

    def __init__(self):
        super().__init__()
        self.direction = 'right'
        self.change_to = None


    def change_direction(self):
        if self.change_to == 'up' and self.direction != 'down':
            self.direction = 'up'
        if self.change_to == 'down' and self.direction != 'up':
            self.direction = 'down'
        if self.change_to == 'left' and self.direction != 'right':
            self.direction = 'left'
        if self.change_to == 'right' and self.direction != 'left':
            self.direction = 'right'

    def update_head(self):
        # print(self.rect)
        if self.direction == 'up':
            if self.rect.top > 0:
                self.y -= self.settings.snake_size
            else:
                self.y = self.settings.screen_height - self.settings.snake_size
        if self.direction == 'down':
            if self.rect.bottom < self.settings.screen_height:
                self.y += self.settings.snake_size
            else:
                self.y = 0
        if self.direction == 'left':
            if self.rect.left > 0:
                self.x -= self.settings.snake_size
            else:
                self.x = self.settings.screen_width - self.settings.snake_size
        if self.direction == 'right':
            if self.rect.right < self.settings.screen_width:
                self.x += self.settings.snake_size
            else:
                self.x = 0

        self.rect = pygame.Rect(
            (self.x, self.y, self.settings.snake_size, self.settings.snake_size)
        )
        self.in_rect.center = self.rect.center

    def draw_snake_head(self, screen):
        self.change_direction()
        self.update_head()
        pygame.draw.rect(screen, self.settings.snake_border_colour, self.rect)
        pygame.draw.rect(screen, self.settings.snake_colour, self.in_rect, border_radius=5)
        pygame.draw.circle(screen, self.settings.snake_eye_colour, self.rect.center, self.settings.snake_eye_size)
