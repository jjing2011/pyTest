class GameStats():
    """Track game stats"""

    def __init__(self, ai_settings):
        """init"""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit