#Abstract class
class Settings():
    """ 
    scr_width = 1200
    scr_hight = 800
    bg_color = (0, 191, 255)

    """
    def __init__(self): 
        # Sceen settings
        self.scr_width = 1200   
        self.scr_hight = 800
        self.bg_color = (0, 191, 255)

        # Ship settings 
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 30

