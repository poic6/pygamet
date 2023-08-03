import pygame
import os

# 게임스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색 정의
GREEN = (100, 200, 100)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("mouse")

# 스크린정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 초기설정
mouse_image = pygame.image.load(os.path.join(assets_path, 'mouse.png'))
mouse_image = pygame.transform.scale(mouse_image, [50, 50])
mouse_x = int(SCREEN_WIDTH/2)
mouse_y = int(SCREEN_HEIGHT/2)
pygame.mouse.set_visible(False)

# 게임 종료 전까지 반복
done = False

# 게임 반복구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 게임 로직
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    
    # 스크린 채우기
    screen.fill(GREEN)

    #화면그리기
    screen.blit(mouse_image, [mouse_x, mouse_y])
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()