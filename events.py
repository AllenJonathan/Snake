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

def check_events_main_menu(current):
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            return _check_keydown_events_main_menu(event, current)

def _check_keydown_events_main_menu(event, current):
    selected = False
    if event.key == pygame.K_RETURN:
        if current == 0:
            selected = 1
        elif current == 1:
            selected = 2
        elif current == 2:
            selected = 3
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP:
        if current != 0:
            current -= 1
    elif event.key == pygame.K_DOWN:
        if current != 2:
            current += 1
    return selected, current

def check_events_settings(current, choose):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return _check_keydown_events_settings(event, current, choose)

def _check_keydown_events_settings(event, current, choose, escape=None):
    print('keydown')
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_ESCAPE:
        escape = True
    elif event.key == pygame.K_UP:
        if current != 0:
            current -= 1
    elif event.key == pygame.K_DOWN:
        if current != 2:
            current += 1
    if choose != -1:
        if event.key == pygame.K_LEFT:
            if choose != 0:
                choose -= 1
        elif event.key == pygame.K_RIGHT:
            if choose != 2:
                choose += 1
    return current, choose, escape
