from os import scandir
import pygame

pygame.init()   # 초기화 (무조건 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 title
pygame.display.set_caption("Game Test")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
bg = pygame.image.load("C:\\py_study\\basic\\py_study\\pygame_basic\\bg.png")

# 스프라이트 불러오기
character = pygame.image.load("C:\\py_study\\basic\\py_study\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x = screen_width / 2 - (character_width / 2)
character_y = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# event loop
running = True
while running:
    dt = clock.tick(30)     # 초당 프레임 설정 , 프레임별로 이동하는 값이 달라져야함
    #print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():    # 무조건 필요 (마우스,키보드 이벤트 체크)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 이동
    # dt = 프레임 계산
    character_x += to_x * dt
    character_y += to_y * dt

    if character_x < 0:
        character_x = 0
    if character_x > screen_width - character_width:
        character_x = screen_width - character_width
    if character_y < 0:
        character_y = 0
    if character_y > screen_height - character_height:
        character_y = screen_height - character_height

    # 화면 출력
    screen.blit(bg,(0,0))
    screen.blit(character,(character_x,character_y))
    pygame.display.update()     # redraw

# pygame 종료
pygame.quit()