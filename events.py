import sys
import pygame

def check_events(snake):
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(event, snake)

def _check_keydown_events(event, snake):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP:
        snake.head.change_to = 'up'
    elif event.key == pygame.K_DOWN:
        snake.head.change_to = 'down'
    elif event.key == pygame.K_RIGHT:
        snake.head.change_to = 'right'
    elif event.key == pygame.K_LEFT:
        snake.head.change_to = 'left'
