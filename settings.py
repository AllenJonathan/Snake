class Settings:

    def __init__(self):

        # screen
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_colour = (169,204,102)

        # FPS
        self.FPS = 5
        self.game_speed_increase = 0.01

        # snake
        self.snake_size = 30
        self.snake_colour = (0,0,0)
        self.snake_border_colour = (169,204,102)
        self.snake_eye_colour = (0,0,240)
        self.snake_eye_size = 3

        # food
        self.food_colour = (175,0,0)
        self.golden_food_color = (250,250,0)
        self.golden_food_prob = 2 # lesser the more chances

        # score
        self.score_font = 'calibri'
        self.score_size = 30
        self.score_colour = (250,250,255)
        self.score_padding = 20
        self.score_incement = 50
        self.gold_multiplier = 3

        # game over
        self.game_over_font = 'times new roman'
        self.game_over_size = 60
        self.game_over_colour = (0,0,0)
