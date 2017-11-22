import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((900,600))  # 创建一个窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")  # 创建标题

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()
    # 创建一个外星人群组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 设置背景色（RGB 浅灰色）
    # bg_color = (230,230,230)

    # 创建一个外型飞船
    # alien = Alien(ai_settings, screen)

    # 开始游戏的主循环

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            # 更新子弹的位置并删除已消失的子弹
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen,stats,sb,  ship, aliens, bullets)

        # bullets.update()
        #
        # # 删除以消失的子弹
        # for bullet in bullets.copy():
        # 	if bullet.rect.bottom <=0:
        # 		bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)
        # for event in pygame.event.get():
        # 	if event.type == pygame.QUIT:
        # 		sys.exit()

        # # 每次循环时都重绘屏幕
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # # 让最近绘制的屏幕可见
        # pygame.display.flip()


run_game()
