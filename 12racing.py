import pygame
import os
import random
from time import sleep

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150,150,150)
RED = (200,0,0)

CAR_COUNT = 3 # 자동차 개수
LANE_COUNT = 5 # 차선 개수
SPEED = 10

current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, 'assets')
car_path = os.path.join(assets_path, 'car')

class Car():
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        # 자동차들
        image_file_list = os.listdir(car_path)
        self.image_path_list = [os.path.join(car_path, file) for file in image_file_list if file.endwith(".png")]
        # 그 외 이미지
        self.crash_image = pygame.image.load(os.path.join(assets_path, "crash.png"))
        self.crash_sound = pygame.mixer.Sound(os.path.join(assets_path, "crash.wav"))
        self.collision_sound = pygame.mixer.Sound(os.path.join(assets_path, "collision.wav"))
        self.engine_sound = pygame.mixer.Sound(os.path.join(assets_path, "engine.wav"))
    
    def load_image(self):
        choice_car_path = random.choice(self.image_path_list)
        self.image = pygame.image.load(choice_car_path)
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.rect = self.image.get_rect()

    # player 자동차 불러오기
    def load(self):
        self.load_image()
        self.x = SCREEN_WIDTH//2
        self.y = SCREEN_HEIGHT-self.height
        self.dx = 0
        self.dy = 0
        self.engine_sound.play()

    #  컴퓨터 자동차 불러오기
    def load_random(self):
        self.load_image()
        self.x = random.randrange(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.dx = 0
        self.dy = random.randint(4, 9)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def out_of_screen(self):
        if self.x + self.width > SCREEN_WIDTH or self.x < 0:
            self.x -= self.dx
        if self.y + self.height > SCREEN_HEIGHT or self.y < 0:
            self.y -= self.dy
    
    def check_carsh(self, car):
        if self.rect.colliderect(car.rect):
            return True
        else:
            return False
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def draw_crash(self, screen):
        width = self.crash_image.get_rect().width
        height = self.crash_image.get_rect().height
        draw_x = self.x + self.width//2 - width//2
        draw_y = self.y + self.height//2 - height//2
        screen.blit(self.crash_image, (draw_x, draw_y))
        pygame.display.update()

class Lane():
    def __init__(self):
        self.color = WHITE
        self.width = 10
        self.height = 80
        self.gap = 20
        self.space = (SCREEN_WIDTH - (self.width*LANE_COUNT)) / (LANE_COUNT-1)
        self.count = 10
        self.x = 0
        self.y = -self.height

    def move(self, speed, screen):
        self.y += speed
        # 차선이 다 보이고 나면 다시 위로 올려
        if self.y>0:
            self.y = -self.height
        self.draw(screen)

    def draw(self, screen):
        next_lane = self.y
        for i in range(self.count):
            pygame.draw.rect(screen, self.color, (self.x, next_lane, self.width, self.height))
            next_lane += self.height + self.gap

class Game():
    def __init__(self):
        self.image_intro = pygame.image.load(os.path.join(assets_path,"menu_car.png"))
        pygame.mixer.music.load(os.path.join(assets_path, "race.wav"))
        self.font_40 = pygame.font.SysFont("맑은 고딕", 40, False, False)
        self.font_30 = pygame.font.SysFont("맑은 고딕", 30, False, False)
        # 도로 차선생성
        self.lanes = []
        for i in range(LANE_COUNT):
            lane = Lane()
            lane.x = i*int(lane.space+lane.width)
            self.lanes.append(lane)
        # 컴퓨터 자동차 생성
        self.cars = []
        for i in range(CAR_COUNT):
            car = Car()
            self.cars.append(car)
        # player자동차 생성
        self.player = Car()

        self.score = 0
        self.menu_on = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                return False
        if self.menu_on:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                    self.score = 0
                    self.menu_on = False

                    self.player.load()
                    for car in self.card:
                        car.load_random()
                    sleep(4)
        else:
            if event.type == pygame.KEYDOWN:
                