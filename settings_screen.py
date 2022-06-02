import pygame
from settings import Settings
import events as ev

class SettingsScreen:

    def __init__(self):
        pygame.init()
        self.settings = Settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        self.main_font = pygame.font.SysFont(self.settings.main_menu_font, self.settings.main_menu_font_size, True)
        self.title_font = pygame.font.SysFont(self.settings.main_menu_font, self.settings.main_menu_title_font_size, True)

        self.options = ['game_size', 'snake_colour', 'food_colour']
        self.current = 0
        self.choose = -1

        self.settings_options = {
            'game_size': [30, 40, 60],
            'snake_colour': [(0,0,0), (128,64,0), (174,12,0)],
            'food_colour': [(175,0,0), (255,192,203), (0,0,128)]
        }
        # retrive updated settings
        self.game_size_current = self.settings_options['game_size'].index(self.settings.snake_size)
        self.snake_colour_current = self.settings_options['snake_colour'].index(self.settings.snake_colour)
        self.food_colour_current = self.settings_options['food_colour'].index(self.settings.food_colour)

    def render_screen(self):
        while True:
            self.screen.fill(self.settings.bg_colour)
            if self.check_events():
                break
            self.display_text()
            pygame.display.flip()

    def display_text(self):

        # retrive updated settings
        self.game_size_current = self.settings_options['game_size'].index(self.settings.snake_size)
        self.snake_colour_current = self.settings_options['snake_colour'].index(self.settings.snake_colour)
        self.food_colour_current = self.settings_options['food_colour'].index(self.settings.food_colour)

        # creating text surface
        title_surface = self.title_font.render(
            "SETTINGS", True, self.settings.main_menu_font_colour)

        if self.current == 0:
            game_size_surface = self.main_font.render(
                "GAME SIZE               :                          " + " < " + str(self.settings_options['game_size'][self.game_size_current]) + " > ",
                True,
                self.settings.main_menu_select_colour
                )
        else:
            game_size_surface = self.main_font.render(
                "GAME SIZE               :                          " + str(self.settings_options['game_size'][self.game_size_current]),
                True,
                 self.settings.main_menu_font_colour
                 )
        if self.current == 1:
            snake_colour_surface = self.main_font.render(
                "SNAKE COLOUR      :                          " + " < " + str(self.settings_options['snake_colour'][self.snake_colour_current]) + " > ",
                True,
                self.settings.main_menu_select_colour
                )
        else:
            snake_colour_surface = self.main_font.render(
                "SNAKE COLOUR      :                          " + str(self.settings_options['snake_colour'][self.snake_colour_current]),
                True,
                self.settings.main_menu_font_colour
                )
        if self.current == 2:
            food_colour_surface = self.main_font.render(
                "FOOD COLOUR        :                          " + " < " + str(self.settings_options['food_colour'][self.food_colour_current]) + " > ",
                True,
                self.settings.main_menu_select_colour
                )
        else:
            food_colour_surface = self.main_font.render(
                "FOOD COLOUR        :                          " + str(self.settings_options['food_colour'][self.food_colour_current]),
                True,
                self.settings.main_menu_font_colour
                )

        # getting rect
        title_rect = title_surface.get_rect()
        game_size_rect = game_size_surface.get_rect()
        snake_colour_rect = snake_colour_surface.get_rect()
        food_colour_rect = food_colour_surface.get_rect()

        # positioning rects
        title_rect.center = (self.settings.screen_width // 2, self.settings.screen_height / 3)
        game_size_rect.center = (self.settings.screen_width // 3, self.settings.screen_height // 1.8)
        snake_colour_rect.center = (self.settings.screen_width // 3, game_size_rect.bottom + 100)
        food_colour_rect.center = (self.settings.screen_width // 3, snake_colour_rect.bottom + 100)

        game_size_rect.left = self.settings.screen_width//5 - 100
        snake_colour_rect.left = self.settings.screen_width//5 - 100
        food_colour_rect.left = self.settings.screen_width//5 - 100


        # blit
        self.screen.blit(title_surface, title_rect)
        self.screen.blit(game_size_surface, game_size_rect)
        self.screen.blit(snake_colour_surface, snake_colour_rect)
        self.screen.blit(food_colour_surface, food_colour_rect)


    def check_events(self):
        if self.current == 0:
            self.choose = self.game_size_current
        elif self.current == 1:
            self.choose == self.snake_colour_current
        elif self.current == 2:
            self.choose == self.food_colour_current

        events = ev.check_events_settings(self.current, self.choose)
        if events:
            self.current, self.choose, escape = events
            if escape:
                return True
        if self.choose != -1:
            if self.current == 0:
                new_setting = self.settings_options[self.options[self.current]][self.choose]
                self.settings.snake_size = new_setting
            elif self.current == 1:
                new_setting = self.settings_options[self.options[self.current]][self.choose]
                self.settings.snake_colour = new_setting
            elif self.current == 2:
                new_setting = self.settings_options[self.options[self.current]][self.choose]
                self.settings.food_colour = new_setting
