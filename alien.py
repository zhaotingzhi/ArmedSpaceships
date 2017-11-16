import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星飞船"""

    def __init__(self, ai_settings, screen):
        """初始化并设置外星人的起始位置"""
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载外型飞船的图像并获取其rect
        self.image = pygame.image.load("images/alien.png").convert_alpha()
        self.rect = self.image.get_rect()
        # 所有外星船最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘 返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
