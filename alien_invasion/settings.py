class Settings():
    """restore all settings"""

    def __init__(self):
        """default settings"""

        # display setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet config
        self.bullet_speed_factor = 1    # debug 3
        self.bullet_width = 300         # debug 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # alien config
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        
        # 1: move right, -1: move left
        self.fleet_direction = 1