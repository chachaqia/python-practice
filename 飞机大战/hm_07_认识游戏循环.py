# Randon Li
# creation time: 2022/8/19 11:14
import pygame
# 游戏的初始化
pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
# 每次调用update代表一帧
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
i = 0
# 游戏循环 ->意味着游戏的正式开始！
while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    i += 1
    print(i)
    pass

pygame.quit()
