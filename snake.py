import pygame
from data_structures.singly_linked_list import LinkedList
from data_structures.nodes import Head, Body


class Snake:

    def __init__(self):
        self.snake = LinkedList()
        self.head = Head()

        self.snake.prepend(self.head)

    def add_body_node(self):
        body = Body()
        self.snake.prepend(body)

    def update_body(self):
        current = self.snake.head
        while current.next:
            next = current.next
            current.value.rect = next.value.rect
            current = current.next

    def draw_body(self, screen):
        self.update_body()
        current = self.snake.head
        while current.next:
            pygame.draw.rect(screen, self.head.body_colour, current.value.rect)
            current = current.next

    def draw_snake(self, screen):
        if self.snake.length > 1:
            self.draw_body(screen)
        self.head.draw_snake_head(screen)
