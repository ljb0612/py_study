import pygame

##############################################################################################
# 기본 초기화 (무조건 해야 하는 부분)
pygame.init()   # 초기화 (무조건 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 title
pygame.display.set_caption("Game Test")

# FPS
clock = pygame.time.Clock()
##############################################################################################

# 1. 사용자 게임 초기화 (배경화면, 이미지, 좌표, 폰트 등)

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # 3. 게임 캐릭터 위치 정의    
    
    # 4. 충돌 처리

    # 5. 화면에 그리기
    
    pygame.display.update()     # redraw

# 종료직전 대기
# pygame.time.delay(2000)

# pygame 종료
pygame.quit()