from os import scandir
from xml.etree.ElementInclude import FatalIncludeError
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

# 적 캐릭터
enemy = pygame.image.load("C:\\py_study\\basic\\py_study\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x = (screen_width / 2) - (enemy_width / 2)
enemy_y = (screen_height / 2) - (enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40)
# 총 시간
total_time = 10
# 시작 시간 정보
start_ticks = pygame.time.get_ticks()   # 시작 tick 가져옴

# event loop
running = True
while running:
    dt = clock.tick(60)     # 초당 프레임 설정 , 프레임별로 이동하는 값이 달라져야함
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

    #  경계값
    if character_x < 0:
        character_x = 0
    if character_x > screen_width - character_width:
        character_x = screen_width - character_width
    if character_y < 0:
        character_y = 0
    if character_y > screen_height - character_height:
        character_y = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

    # 화면 출력
    screen.blit(bg,(0,0))
    screen.blit(character,(character_x,character_y))
    screen.blit(enemy,(enemy_x,enemy_y))

    # 타이머
    # 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        running = False

    pygame.display.update()     # redraw

# 종료직전 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()