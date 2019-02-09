import pygame.font

class Scoreboard():
    """
    Class to report score information
    """
    def __init__(self, settings, screen, stats):
        """
        Initialize score keeping attribute
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font setting for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initialize score image
        self.prep_score()

    def prep_score(self):
        """
        Turn score into image
        """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display score at the top-right of the screen
        self.score_rect = self.score_image.get_ret()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        Draw score to screen
        """
        self.screen.blit(self.score_image, self.score_rect)