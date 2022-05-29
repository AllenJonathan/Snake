import pygame
import sys
from snake_game import SnakeGame
from settings import Settings


class MainMenu:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        self.main_font = pygame.font.SysFont(self.settings.main_menu_font, self.settings.main_menu_font_size, True)
        self.title_font = pygame.font.SysFont(self.settings.main_menu_font, self.settings.main_menu_title_font_size, True)

        self.options = ['play', 'settings', 'quit']
        self.current = 0


    def render_screen(self):

        while True:
            self.screen.fill(self.settings.bg_colour)
            self.check_events()
            self.display_text()
            pygame.display.flip()

    def display_text(self):
        # creating text surface
        title_surface = self.title_font.render(
            "SNAKE GAME", True, self.settings.main_menu_font_colour)

        if self.current == 0:
            play_surface = self.main_font.render(
                "PLAY", True, self.settings.main_menu_select_colour)
        else:
            play_surface = self.main_font.render(
                "PLAY", True, self.settings.main_menu_font_colour)
        if self.current == 1:
            settings_surface = self.main_font.render(
                "SETTINGS", True, self.settings.main_menu_select_colour)
        else:
            settings_surface = self.main_font.render(
                "SETTINGS", True, self.settings.main_menu_font_colour)
        if self.current == 2:
            quit_surface = self.main_font.render(
                "QUIT", True, self.settings.main_menu_select_colour)
        else:
            quit_surface = self.main_font.render(
                "QUIT", True, self.settings.main_menu_font_colour)

        # getting rect
        title_rect = title_surface.get_rect()
        play_rect = play_surface.get_rect()
        settings_rect = settings_surface.get_rect()
        quit_rect = quit_surface.get_rect()

        # positioning rects
        title_rect.center = (self.settings.screen_width // 2, self.settings.screen_height / 3)
        play_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 1.8)
        settings_rect.center = (self.settings.screen_width // 2, play_rect.bottom + 100)
        quit_rect.center = (self.settings.screen_width // 2, settings_rect.bottom + 100)

        # blit
        self.screen.blit(title_surface, title_rect)
        self.screen.blit(play_surface, play_rect)
        self.screen.blit(settings_surface, settings_rect)
        self.screen.blit(quit_surface, quit_rect)

    def check_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.current == 0:
                        self.play_game()
                    elif self.current == 1:
                        pass
                    elif self.current == 2:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    if self.current != 0:
                        self.current -= 1
                elif event.key == pygame.K_DOWN:
                    if self.current != 2:
                        self.current += 1

    def play_game(self):
        game = SnakeGame()
        game.rungame()



main_menu = MainMenu()
main_menu.render_screen()
