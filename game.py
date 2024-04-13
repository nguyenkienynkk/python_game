import pygame, sys, random


# Tạo hàn chơi trò chơi
def draw_floow():  # hàm trong python
    screen.blit(floor, (floor_x_pos, 650))  # hàm blit trả về 2 tham số đó là (x,y)
    # có 600 chạy từ 600 - 1 đế 432 là hết màn hình sau đó lại chạy xuống hàm dưới và cộng tiếp 432
    screen.blit(floor, (floor_x_pos + 432, 650))  # có 600 nhưng chạy từ
    # tạo ra 2 cái sàn để người dùng thấy như nó không có điểm dừng chạy nối tiếp nhau
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos - 650))
    return top_pipe, bottom_pipe
def move_pipe(pipes):  # Tạo vòng lặp chứa list những cái ống rồi di chuyển nó sang trái
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:  # Nếu bị lòi ra ở bottom
            screen.blit(pipe_surface, pipe)
        else:  # Không thì sẽ lật ngược lại
            flip_pipe = pygame.transform.flip(
                pipe_surface, False, True
            )  # False true là trục xy nếu muốn lật theo chiều nào thì true chiều đó
            screen.blit(flip_pipe, pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            die_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
        return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movement * 2, 1)
    # tạo hiệu ứng xoay cho chim
    return new_bird


def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect

def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score
def score_display(game_state) :
    if game_state == 'main game' :
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game over' : #nếu kết thúc thì hiển thị điểm  = hight score
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)
        
        hight_score_surface = game_font.render(f'Hight Score: {int(high_score)}',True,(255,255,255))
        hight_score_rect = hight_score_surface.get_rect(center = (216,630))
        screen.blit(hight_score_surface,hight_score_rect)
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer= 512)
#Chỉnh sửa âm thanh thích hợp
pygame.init()
screen = pygame.display.set_mode((432, 768))
# tạo ra màn hình đen nháy 1 lần
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)
# Tạo các biến cho trò chơi
# Tạo trọng lực
# Tạo các biến cho trò chơi
gravity = 0.05
bird_movement = 0
game_active = True
score = 0
high_score = 0
bg = pygame.image.load(
    "assests/background-night.png"
).convert()  # convert() chuyển file game thành file khác nhẹ hơn #load nhanh hơn
# làm cho bg gấp đôi lên
bg = pygame.transform.scale2x(bg)
# chèn 1 cái sàn vào
floor = pygame.image.load("assests/floor.png")
floor = pygame.transform.scale2x(floor)
# gán biến tọa độ 0 cho cái sàn
floor_x_pos = 0
# tạo chim
bird_down = pygame.transform.scale2x(
    pygame.image.load("assests/yellowbird-downflap.png")
)
bird_mid = pygame.transform.scale2x(pygame.image.load("assests/yellowbird-midflap.png"))
bird_up = pygame.transform.scale2x(pygame.image.load("assests/yellowbird-upflap.png"))
bird_list = [bird_down, bird_mid, bird_up]
bird_index = 0
bird = bird_list[bird_index]
# tạo timer cho bird
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 200)
# bird = pygame.image.load("assests/yellowbird-midflap.png").convert_alpha()
# bird = pygame.transform.scale2x(bird)
# tạo 1 hình chữ nhật xung quanh con chim
bird_rect = bird.get_rect(center=(100, 384))
# tạo ống
pipe_surface = pygame.image.load("assests/pipe-green.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
# Tạo timer
spawnpipe = pygame.USEREVENT  # User event sự kiện người dùng
pygame.time.set_timer(spawnpipe, 1200)  # sau 1.2 giây thì sẽ tạo 1 ống mới
#Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load("assests/message.png"))
game_over_rect = game_over_surface.get_rect(center = (216,384))
# Random pipe
pipe_height = [200, 300, 400]
#Chèn âm thanh
flap_sound = pygame.mixer.Sound("sound/sfx_wing.wav")
hit_sound = pygame.mixer.Sound("sound/sfx_hit.wav")
score_sound = pygame.mixer.Sound("sound/sfx_point.wav")
score_sound_countdown = 100
die_sound = pygame.mixer.Sound("sound/sfx_die.wav")
swooshing_sound = pygame.mixer.Sound("sound/sfx_swooshing.wav")



while True:
    for event in pygame.event.get():  # lấy tất cả sự kiện pygame diễn ra
        # tạo phím để người chơi nhấn vào và thoát cửa sổ game ra
        # thoát khỏi hệ thống
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Khi space
        if event.type == pygame.KEYDOWN:  # chọn phím
            if event.key == pygame.K_SPACE and game_active:  # khi click space
                bird_movement = 0
                bird_movement = -4
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True  # nếu chết active lại
                pipe_list.clear()
                bird_rect.center = (100, 384)
                bird_movement = 0
                score = 0
                # List ống
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()
            # nếu ống mới xuất hiện thì sẽ thêm nó vào 1 cái list
        # Ống
    # Chim
    screen.blit(bg, (0, 0))  # set tọa độ ở góc màn hình bên phía tay trái
    if game_active:
        bird_movement += gravity  # 1,2,3,4,5,6,7,8,9 + 0,25
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += (
            bird_movement  # centery ++ nghĩa là nó sẽ tăng y và từ trên xuống
        )
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)
        pipe_list = move_pipe(pipe_list)  # Move pipes to update their positions
        draw_pipe(pipe_list)  # Draw pipes after updating positions
        score += 0.01
        score_display("main game")
        score_sound_countdown -= 1
        if score_sound_countdown <=0:
            score_sound.play()
            score_sound_countdown = 100
        #làm mượt âm thanh hơn
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score,high_score)
        score_display("game over")
    # chim càng di chuyển trọng lực càng tăng
    # Sàn
    floor_x_pos -= 1
    # sàn sẽ ở tọa độ -1
    # vì dùng hàm while true nên tọa độ floor_x_pos liên tục bị trừ 1 từ 600 về 0
    draw_floow()
    if floor_x_pos <= -432:
        floor_x_pos = 0
        # khi sàn chạy xong sàn 1 thì sẽ lập tức đổi vị trí cho sàn 2
    pygame.display.update()
    clock.tick(120)
    # chỉ số fps là 120
