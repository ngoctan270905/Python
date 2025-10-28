import pygame
import sys
import random

# ---------- Cấu hình ----------
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20           # kích thước mỗi ô (pixel)
FPS = 10                 # tốc độ game (tăng để nhanh hơn)

# Màu (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (200, 0, 0)
DARK_GRAY = (40, 40, 40)
YELLOW = (230, 200, 0)

# ---------- Hàm trợ giúp ----------
def draw_grid(surface):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, DARK_GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, DARK_GRAY, (0, y), (WINDOW_WIDTH, y))

def random_food_position(snake):
    cols = WINDOW_WIDTH // CELL_SIZE
    rows = WINDOW_HEIGHT // CELL_SIZE
    while True:
        pos = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if pos not in snake:
            return pos

def draw_cell(surface, position, color):
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)

def show_text(surface, text, size, color, pos):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    surface.blit(img, pos)

# ---------- Game ----------
def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake - Python + Pygame")
    clock = pygame.time.Clock()

    # Khởi tạo snake: list các ô theo (col, row)
    start_x = (WINDOW_WIDTH // CELL_SIZE) // 2
    start_y = (WINDOW_HEIGHT // CELL_SIZE) // 2
    snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
    direction = (1, 0)  # bắt đầu sang phải (dx, dy)
    pending_dir = direction

    food = random_food_position(snake)
    score = 0
    running = True
    game_over = False

    while running:
        # ---------- xử lý sự kiện ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    pending_dir = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    pending_dir = (0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    pending_dir = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    pending_dir = (1, 0)
                elif event.key == pygame.K_r and game_over:
                    # reset game
                    return True  # signal to restart
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # Không cho quay ngược 180 độ trực tiếp
        if (pending_dir[0] * -1, pending_dir[1] * -1) != direction:
            direction = pending_dir

        if not game_over:
            # ---------- di chuyển snake ----------
            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])

            # va chạm tường?
            max_cols = WINDOW_WIDTH // CELL_SIZE
            max_rows = WINDOW_HEIGHT // CELL_SIZE
            if not (0 <= new_head[0] < max_cols and 0 <= new_head[1] < max_rows):
                game_over = True

            # va chạm chính mình?
            if new_head in snake:
                game_over = True

            if not game_over:
                snake.insert(0, new_head)  # thêm đầu mới
                # ăn thức ăn?
                if new_head == food:
                    score += 1
                    food = random_food_position(snake)
                else:
                    snake.pop()  # bỏ đuôi (di chuyển bình thường)

        # ---------- vẽ ----------
        screen.fill(BLACK)
        # draw_grid(screen)  # nếu muốn lưới thì mở lên

        # vẽ thức ăn
        draw_cell(screen, food, RED)

        # vẽ snake
        for i, cell in enumerate(snake):
            color = GREEN if i == 0 else YELLOW
            draw_cell(screen, cell, color)

        # hiển thị điểm
        show_text(screen, f"Score: {score}", 24, WHITE, (10, 10))

        if game_over:
            # overlay game over
            show_text(screen, "GAME OVER", 64, RED, (WINDOW_WIDTH // 2 - 160, WINDOW_HEIGHT // 2 - 50))
            show_text(screen, f"Score: {score}", 40, WHITE, (WINDOW_WIDTH // 2 - 60, WINDOW_HEIGHT // 2 + 10))
            show_text(screen, "Press R to Restart or ESC to Quit", 26, WHITE, (WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 + 60))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    return False

def main():
    restart = True
    while restart:
        restart = game_loop()

if __name__ == "__main__":
    main()
