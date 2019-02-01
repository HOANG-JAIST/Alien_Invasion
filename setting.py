#Abstract class
class Settings():
    """ store all settings for game

    #Attrib
    scr_width = 1200
    scr_hight = 800
    bg_color = (0, 191, 255)

    # Method/ Func
    """
    def __init__(self): 
        # Settings for screen
        self.scr_width = 1200   
        self.scr_hight = 800
        self.bg_color = (0, 191, 255)

        #Ship settings 
        self.ship_speed_factor = 1.5


