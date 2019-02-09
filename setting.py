
class Settings():
    """ 
    A class contains all settings of the game
    """
    def __init__(self):
        # Sceen settings
        self.screen_width = 1200   
        self.screen_height = 800
        self.bg_color = (0, 191, 255)

        # Ship settings 
        self.ship_speed_factor = 50
        self.ship_limit = 15

        # Bullet settings
        self.bullet_speed_factor = 15
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 50

        # Alien settings
        self.alien_speed_factor = 5
        self.fleet_droop_speed = 10

        # Fleet direction of 1 represents right, -1 represent left
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """
        Initialize settings that change through the game
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        # Scoring 
        self.alien_points = 50

    def increase_speed(self):
        """
        Increase speed settings
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *- self.speedup_scale
        
