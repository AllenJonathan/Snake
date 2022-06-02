class Settings:

    # screen
    screen_width = 1920
    screen_height = 1080
    bg_colour = (169,204,102)

    # FPS
    FPS = 5
    game_speed_increase = 0.01

    # snake
    snake_size = 30 # 20 40 60 can be used
    snake_colour = (0,0,0) # cab be changed
    # -> Brown (128, 64, 0)
    # -> Maroon (174,12,0)
    snake_border_colour = bg_colour
    snake_eye_colour = (0,0,240)
    snake_eye_size = 3

    # food
    food_colour = (175,0,0)
    # Pink -> (255, 192, 203)
    # Navy Blue -> (0, 0, 128)
    golden_food_color = (250,215,0)
    golden_food_prob = 10 # lesser the more chances

    # score
    score_font = 'calibri'
    score_size = 30
    score_colour = (250,250,255)
    score_padding = 20
    score_incement = 50
    gold_multiplier = 3

    # game over
    game_over_font = 'times new roman'
    game_over_size = 60
    game_over_colour = (0,0,0)

    # main menu
    main_menu_font = 'calibri'
    main_menu_font_size = 70
    main_menu_font_colour = (255,255,255)
    main_menu_title_font_size = 150
    main_menu_select_colour = (0,0,0)
