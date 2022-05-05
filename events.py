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
    elif event.key == pygame.K_SPACE:
        snake.add_body_node()
    elif event.key == pygame.K_UP and (not snake.head.move_down):
        _reset_movement(snake)
        snake.head.move_up = True
    elif event.key == pygame.K_DOWN and (not snake.head.move_up):
        _reset_movement(snake)
        snake.head.move_down = True
    elif event.key == pygame.K_RIGHT and (not snake.head.move_left):
        _reset_movement(snake)
        snake.head.move_right = True
    elif event.key == pygame.K_LEFT and (not snake.head.move_right):
        _reset_movement(snake)
        snake.head.move_left = True


def _reset_movement(snake):
    snake.head.move_up = False
    snake.head.move_down = False
    snake.head.move_right = False
    snake.head.move_left = False
