# Randon Li
# creation time: 2022/8/19 11:14
import pygame
# set_mode(resolution=(0,0),flags=0，depth=0) -> Surface
# ·作用--创建游戏显示窗口
# ·参数
# resolution指定屏幕的宽和高,默认创建的窗口大小和屏幕大小一致
# flags参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
# depth参数表示颜色的位数，默认自动匹配

pygame.init()
# 创建游戏的窗口  480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图形数据
background = pygame.image.load("./images/background.png")
# 2> blit 绘制图像
screen.blit(background, (0, 0))
# 3> update 更新屏幕显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

# 游戏循环
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= -hero_rect.height:
        hero_rect.y = 700

    # 3. 调用blit方法绘制图像
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)
    # 4. 调用update方法更新显示
    pygame.display.update()
    pass

pygame.quit()
