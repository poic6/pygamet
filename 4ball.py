import pygame

# 게임스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색 정의
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("ball")

# 스크린정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임화면 업데이트 속도
clock = pygame.time.Clock()

# 공 초기 위치, 크기, 속독
ball_x = int(SCREEN_WIDTH/2)
ball_y = int(SCREEN_HEIGHT/2)
ball_dx = 4
ball_dy = 4
ball_size = 40

# 게임 종료 전까지 반복
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    ball_x += ball_dx
    ball_y += ball_dy

    if(ball_x + ball_size) > SCREEN_WIDTH or (ball_x - ball_size) < 0:
        ball_dx = ball_dx*-1
    if(ball_y + ball_size) > SCREEN_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy = ball_dy*-1

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, [ball_x, ball_y], ball_size, 0)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()