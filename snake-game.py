import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (40, 44, 52)
RED = (255, 99, 71)
GREEN = (50, 205, 50)
BLUE = (30, 144, 255)
PURPLE = (147, 112, 219)
ORANGE = (255, 140, 0)
PINK = (255, 182, 193)

# Game speeds for different difficulty levels
SPEED_EASY = 10
SPEED_MEDIUM = 15
SPEED_HARD = 20

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.colors = [BLUE]  # Single color for snake
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + x) % GRID_WIDTH, (cur[1] + y) % GRID_HEIGHT)
        if new in self.positions[3:]:
            return False
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def reset(self):
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1),
                        random.randint(0, GRID_HEIGHT-1))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.speed = SPEED_EASY

    def draw_menu(self):
        self.screen.fill(BLACK)
        title = self.font.render('SNAKE GAME', True, PINK)
        easy = self.font.render('1. Easy', True, GREEN)
        medium = self.font.render('2. Medium', True, ORANGE)
        hard = self.font.render('3. Hard', True, RED)
        quit_text = self.font.render('4. Quit', True, PURPLE)

        self.screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 100))
        self.screen.blit(easy, (WINDOW_WIDTH//2 - easy.get_width()//2, 200))
        self.screen.blit(medium, (WINDOW_WIDTH//2 - medium.get_width()//2, 250))
        self.screen.blit(hard, (WINDOW_WIDTH//2 - hard.get_width()//2, 300))
        self.screen.blit(quit_text, (WINDOW_WIDTH//2 - quit_text.get_width()//2, 350))
        pygame.display.flip()

    def handle_menu(self):
        while True:
            self.draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.speed = SPEED_EASY
                        return True
                    if event.key == pygame.K_2:
                        self.speed = SPEED_MEDIUM
                        return True
                    if event.key == pygame.K_3:
                        self.speed = SPEED_HARD
                        return True
                    if event.key == pygame.K_4:
                        return False

    def run(self):
        while True:
            if not self.handle_menu():
                break

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                        if event.key == pygame.K_UP and self.snake.direction != DOWN:
                            self.snake.direction = UP
                        if event.key == pygame.K_DOWN and self.snake.direction != UP:
                            self.snake.direction = DOWN
                        if event.key == pygame.K_LEFT and self.snake.direction != RIGHT:
                            self.snake.direction = LEFT
                        if event.key == pygame.K_RIGHT and self.snake.direction != LEFT:
                            self.snake.direction = RIGHT

                if not self.snake.update():
                    running = False

                if self.snake.get_head_position() == self.food.position:
                    self.snake.length += 1
                    self.snake.score += 1
                    self.food.randomize_position()

                self.screen.fill(BLACK)

                for p in self.snake.positions:
                    pygame.draw.rect(self.screen, BLUE,
                                (p[0] * GRID_SIZE, p[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

                pygame.draw.rect(self.screen, self.food.color,
                            (self.food.position[0] * GRID_SIZE, self.food.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

                score_text = self.font.render(f'Score: {self.snake.score}', True, PINK)
                self.screen.blit(score_text, (5, 5))

                pygame.display.flip()
                self.clock.tick(self.speed)

            self.reset()

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()