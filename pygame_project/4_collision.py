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

# 배경
bg = pygame.image.load(os.path.join(image_path,"bg.png"))

# 스테이지
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_height = stage.get_height()

# 캐릭터 위치, 좌표
char = pygame.image.load(os.path.join(image_path,"char.png"))
char_w = char.get_width()
char_h = char.get_height()
char_x = screen_width / 2 - (char_w / 2)
char_y = screen_height - char_h - stage_height
char_to_x = 0
char_speed = 5

# 무기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_w = weapon.get_width()
weapons = []
weapon_speed = 10

# 공
balls_images = [
    pygame.image.load(os.path.join(image_path,"ball1.png")),
    pygame.image.load(os.path.join(image_path,"ball2.png")),
    pygame.image.load(os.path.join(image_path,"ball3.png")),
    pygame.image.load(os.path.join(image_path,"ball4.png"))
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

balls = []
balls.append({"pos_x" : 50, "pos_y" : 50, "img_idx" : 0, "to_x" : 3, "to_y" : -6, "init_speed_y" : ball_speed_y[0]})

# 사라질 무기, 공 정보 저장
weapon_to_remove = -1
ball_to_remove = -1

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

    # 무기 위치
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]

        ball_size = balls_images[ball_img_idx].get_rect().size
        ball_w = ball_size[0]
        ball_h = ball_size[1]

        # 튕겨나오는 공
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_w:
            val["to_x"] = val["to_x"] * -1
        # 스테이지에 튕겨서 올라감
        if ball_pos_y >= screen_height - stage_height - ball_h:
            val["to_y"] = val["init_speed_y"]
        else:
            val["to_y"] += 0.5

        val["pos_x"] += val["to_x"]
        val["pos_y"] += val["to_y"]

    # 4. 충돌 처리

        # 캐릭터 rect
    char_rc = char.get_rect()
    char_rc.left = char_x
    char_rc.top = char_y

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]

        ball_rc = balls_images[ball_img_idx].get_rect()
        ball_rc.left = ball_pos_x
        ball_rc.top = ball_pos_y

        # 공과 캐릭터 충돌
        if char_rc.colliderect(ball_rc):
            running = False
            break

        # 공과 무기 충돌
        for weapon_idx, weapon_val in enumerate(weapons):
            w_x = weapon_val[0]
            w_y = weapon_val[1]

            w_rc = weapon.get_rect()
            w_rc.left = w_x
            w_rc.top = w_y

            if w_rc.colliderect(ball_rc):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_img_idx
                break

    # 충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 5. 화면에 그리기
    screen.blit(bg,(0,0))
    for w_x, w_y in weapons:
        screen.blit(weapon,(w_x,w_y))
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(balls_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(char,(char_x,char_y))

    pygame.display.update()     # redraw

# 종료직전 대기
# pygame.time.delay(2000)

# pygame 종료
pygame.quit()