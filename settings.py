class Settings:

    def __init__(self):

        # screen
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_colour = (0,0,0)

        # FPS
        self.FPS = 30

        # snake
        self.snake_size = 30
        self.snake_colour = (100,255,100)
        self.snake_eye_colour = (0,0,0)
        self.snake_eye_size = 3

        # food
        self.food_colour = (175,0,0)
        self.golden_food_color = (250,250,0)
        self.golden_food_prob = 2 # lesser the more chances

        # score
        self.score_font = 'ariel'
        self.score_size = 30
        self.score_incement = 50
