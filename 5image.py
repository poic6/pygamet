import pygame
import os

# 게임스크린 크기
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320

# 색 정의
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LAND = (160, 120, 40)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("image")

# 스크린정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 배경이미지 불러오기
background_image = pygame.image.load(os.path.join(assets_path, 'terrain.jpg'))
# 버섯 불러오기
mushroom_image1 = pygame.image.load(os.path.join(assets_path, 'mushroom1.png'))
mushroom_image1 = pygame.transform.scale(mushroom_image1, (50, 50))
mushroom_image2 = pygame.image.load(os.path.join(assets_path, 'mushroom2.png'))
mushroom_image2 = pygame.transform.scale(mushroom_image2, (50, 50))
mushroom_image3 = pygame.image.load(os.path.join(assets_path, 'mushroom3.png'))
mushroom_image3 = pygame.transform.scale(mushroom_image3, (50, 50))

# 게임 종료 전까지 반복
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # 게임 로직
    # 화면삭제
    # 스크린 채우기
    screen.fill(LAND)
    #화면그리기
    screen.blit(background_image, background_image.get_rect())
    screen.blit(mushroom_image1, [300, 200])
    screen.blit(mushroom_image2, [400, 200])
    screen.blit(mushroom_image3, [500, 200])
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()