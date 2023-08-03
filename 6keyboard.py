import pygame
import os

# 게임스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색 정의
GRAY = (200, 200, 200)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("keyboard")

# 스크린정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 초기설정
keyboard_image = pygame.image.load(os.path.join(assets_path, 'keyboard.png'))
keyboard_image = pygame.transform.scale(keyboard_image, [50, 50])
keyboard_x = int(SCREEN_WIDTH/2)
keyboard_y = int(SCREEN_HEIGHT/2)
keyboard_dx = 0
keyboard_dy = 0

# 게임 종료 전까지 반복
done = False

# 게임 반복구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -3
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 3
            elif event.key == pygame.K_UP:
                keyboard_dy = -3
            elif event.key == pygame.K_DOWN:
                keboard_dy = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                keyboard_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                keyboard_dy = 0
    # 게임 로직
    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy
    
    # 스크린 채우기
    screen.fill(GRAY)

    #화면그리기
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()