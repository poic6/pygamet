import pygame
import os
import sys
import random
from time import sleep

# 게임스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 게임화면 바둑판 설정
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT/GRID_SIZE

# 방향에 대한 설정
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 색 정의
WHITE = (255,255,255)
ORANGE = (250, 150, 0)
GRAY = (100, 100, 100)

# 뱀 객체
class Snake():
    def __init__(self):
        self.create()
    def create(self):
        self.length = 2
        self.positions = [(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    def control(self, xy):
        if(xy[0]*-1, xy[1]*-1) == self.direction:
            return
        else:
            self.direction = xy
    def move(self):
        cur = self.positions[0]
        x, y = self.direction

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("pygame")

# 스크린정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()