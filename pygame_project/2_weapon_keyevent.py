import pygame
import os

##############################################################################################
# 기본 초기화 (무조건 해야 하는 부분)
pygame.init()   # 초기화 (무조건 필요)

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 title
pygame.display.set_caption("PANG")

# FPS
clock = pygame.time.Clock()
##############################################################################################

# 1. 사용자 게임 초기화 (배경화면, 이미지, 좌표, 폰트 등)

current_path = os.path.dirname(__file__)    # 현재 파일의 위치 반환
image_path = os.path.join(current_path,"images")

bg = pygame.image.load(os.path.join(image_path,"bg.png"))

stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_height = stage.get_height()

char = pygame.image.load(os.path.join(image_path,"char.png"))
char_w = char.get_width()
char_h = char.get_height()
char_x = screen_width / 2 - (char_w / 2)
char_y = screen_height - char_h - stage_height
char_to_x = 0
char_speed = 5

weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_w = weapon.get_width()
weapons = []
weapon_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char_to_x -= char_speed
            elif event.key == pygame.K_RIGHT:
                char_to_x += char_speed
            elif event.key == pygame.K_SPACE:
                weapon_pos_x = char_x + (char_w / 2) - (weapon_w / 2)
                weapon_pos_y = char_y
                weapons.append([weapon_pos_x,weapon_pos_y])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                char_to_x = 0
        
    # 3. 게임 캐릭터 위치 정의
    char_x += char_to_x

    if char_x < 0:
        char_x = 0
    elif char_x > screen_width - char_w:
        char_x = screen_width - char_w

    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    # for w_x, w_y in weapons:
    #     weapons = [w_x,w_y - weapon_speed]
    
    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(bg,(0,0))
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(char,(char_x,char_y))

    for w_x, w_y in weapons:
        screen.blit(weapon,(w_x,w_y))
    
    pygame.display.update()     # redraw

# 종료직전 대기
# pygame.time.delay(2000)

# pygame 종료
pygame.quit()