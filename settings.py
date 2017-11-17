class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的移动速度
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 1
        # fleet_dirextion 为1表示向右移动 ，-1向左
        self.fleet_direction = 1
