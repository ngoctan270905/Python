import pygame
import random
import sys

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Đua Xe - Không cần ảnh")

# Màu
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
BLUE = (0, 150, 255)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

# Xe người chơi
player_width, player_height = 50, 100
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

# Xe địch
enemy_width, enemy_height = 50, 100
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -150
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 40)

def draw_road():
    win.fill(GRAY)
    pygame.draw.rect(win, WHITE, (40, 0, 10, HEIGHT))
    pygame.draw.rect(win, WHITE, (WIDTH - 50, 0, 10, HEIGHT))
    for y in range(0, HEIGHT, 80):
        pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, y, 10, 50))

def draw_objects():
    pygame.draw.rect(win, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(win, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    score_text = font.render(f"Score: {score}", True, YELLOW)
    win.blit(score_text, (10, 10))

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width - 50:
        player_x += player_speed

    # Cập nhật vị trí xe địch
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -150
        enemy_x = random.randint(50, WIDTH - 100)
        score += 1
        enemy_speed += 0.2  # tăng tốc độ dần

    # Kiểm tra va chạm
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if player_rect.colliderect(enemy_rect):
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    # Vẽ lại
    draw_road()
    draw_objects()
    pygame.display.update()
