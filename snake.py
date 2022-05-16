import pygame
from settings import Settings
from data_structures.singly_linked_list import LinkedList
from data_structures.nodes import Head, Body



class Snake:

    def __init__(self):
        self.settings = Settings()

        self.snake = LinkedList()
        self.game_over = False
        self.create_snake()

    def create_snake(self):
        self.head = Head()
        self.snake.prepend(self.head)
        for i in range(4):
            self.add_body_node()

    def add_body_node(self):
        body = Body()
        self.snake.prepend(body)

    def update_body(self):
        current = self.snake.head
        while current.next:
            next = current.next
            current.value.rect = next.value.rect
            current.value.in_rect.center = current.value.rect.center
            current = current.next

    def check_game_over(self):
        current = self.snake.head
        while current.next:
            if current.value.rect == self.head.rect:
                self.game_over = True
            current = current.next

    def draw_body(self, screen):
        self.update_body()
        current = self.snake.head
        while current.next:
            pygame.draw.rect(
                screen, self.settings.snake_border_colour, current.value.rect
                )
            pygame.draw.rect(
                screen, self.settings.snake_colour, current.value.in_rect, border_radius=5
                )
            current = current.next

    def draw_snake(self, screen):
        if self.snake.length > 1:
            self.draw_body(screen)
        self.head.draw_snake_head(screen)
