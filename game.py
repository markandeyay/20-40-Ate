import pygame
import sys
import random
from src.utils import draw_text, Button
from src.audio import play_music, toggle_music

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
TILE_SIZE = WIDTH // COLS
FPS = 10
game_music = "assets/music/game_music.mp3"

DIRS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

def random_empty_cell(snake):
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in [seg[0] for seg in snake]:
            return pos

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [[(COLS // 2, ROWS // 2), 2]]
        self.direction = "RIGHT"
        self.next_dir = "RIGHT"
        self.food = random_empty_cell(self.snake)
        self.food_value = random.choice([2, 4])
        self.score = 0
        self.game_over = False
        self.paused = False

    def move(self):
        head_pos, _ = self.snake[0]
        dx, dy = DIRS[self.direction]
        new_head = (head_pos[0] + dx, head_pos[1] + dy)

        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            self.game_over = True
            return
        if new_head in [seg[0] for seg in self.snake]:
            self.game_over = True
            return

        if new_head == self.food:
            self.snake.insert(0, [new_head, self.food_value])
            self.spawn_food()
            self.merge_tiles()
        else:
            self.snake.insert(0, [new_head, None])
            self.snake.pop()
            self.merge_tiles()

    def spawn_food(self):
        self.food = random_empty_cell(self.snake)
        self.food_value = random.choice([2, 4])

    def merge_tiles(self):
        values = [v for _, v in self.snake if v is not None]
        merged = []
        i = 0
        while i < len(values):
            if i + 1 < len(values) and values[i] == values[i + 1]:
                merged.append(values[i] * 2)
                self.score += values[i] * 2
                i += 2
            else:
                merged.append(values[i])
                i += 1
        j = 0
        for k in range(len(self.snake)):
            if j < len(merged):
                self.snake[k][1] = merged[j]
                j += 1
            else:
                self.snake[k][1] = None

def run_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = Game()
    play_music(game_music)

    # Countdown
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        draw_text(screen, str(i), (WIDTH // 2 - 10, HEIGHT // 2 - 10))
        pygame.display.flip()
        pygame.time.wait(1000)
    draw_text(screen, "GO!", (WIDTH // 2 - 20, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(500)

    def resume():
        game.paused = False

    def return_to_menu():
        from src.menu import run_menu
        run_menu()

    def reset_game():
        game.reset()

    pause_buttons = [
        Button((200, 200, 200, 40), "Resume", resume),
        Button((200, 250, 200, 40), "Toggle Music", toggle_music),
        Button((200, 300, 200, 40), "Reset", reset_game),
        Button((200, 350, 200, 40), "Main Menu", return_to_menu),
    ]

    while True:
        screen.fill((30, 30, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_p, pygame.K_ESCAPE]:
                    game.paused = not game.paused
                elif event.key == pygame.K_r:
                    game.reset()
                elif event.key == pygame.K_UP and game.direction != "DOWN":
                    game.next_dir = "UP"
                elif event.key == pygame.K_DOWN and game.direction != "UP":
                    game.next_dir = "DOWN"
                elif event.key == pygame.K_LEFT and game.direction != "RIGHT":
                    game.next_dir = "LEFT"
                elif event.key == pygame.K_RIGHT and game.direction != "LEFT":
                    game.next_dir = "RIGHT"
            if event.type == pygame.MOUSEBUTTONDOWN and game.paused:
                for b in pause_buttons:
                    b.check_click(event.pos)

        if not game.paused and not game.game_over:
            game.direction = game.next_dir
            game.move()

        fx, fy = game.food
        pygame.draw.rect(screen, (255, 165, 0), (fx * TILE_SIZE, fy * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        draw_text(screen, str(game.food_value), (fx * TILE_SIZE + 10, fy * TILE_SIZE + 10))

        for pos, val in game.snake:
            x, y = pos
            pygame.draw.rect(screen, (50, 205, 50), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if val:
                draw_text(screen, str(val), (x * TILE_SIZE + 8, y * TILE_SIZE + 8))

        draw_text(screen, f"Score: {game.score}", (10, 10))

        if game.game_over:
            draw_text(screen, "Game Over! Press R to restart", (160, 280))

        if game.paused:
            for b in pause_buttons:
                b.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
