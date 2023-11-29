import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
SNAKE_SIZE = 20
SNAKE_SPEED = 15
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (0, 0)

food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
        random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

game_over = False

score = 0
font = pygame.font.Font(None, 36)

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

def check_collision(snake, food):
    return snake[0] == food

def check_self_collision(snake):
    return snake[0] in snake[1:]

def game_over_screen():
    game_over_text = font.render("Game Over", True, RED)
    score_text = font.render("Score: " + str(score), True, RED)
    screen.fill(DARK_GRAY)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - 50, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            if event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            if event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            if event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    new_head = (snake[0][0] + snake_direction[0] * SNAKE_SIZE, snake[0][1] + snake_direction[1] * SNAKE_SIZE)
    snake.insert(0, new_head)

    if check_collision(snake, food):
        score += 10
        food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
    else:
        snake.pop()

    if check_self_collision(snake):
        game_over = True

    if snake[0][0] < 0:
        snake[0] = (WIDTH - SNAKE_SIZE, snake[0][1])
    elif snake[0][0] >= WIDTH:
        snake[0] = (0, snake[0][1])
    elif snake[0][1] < 0:
        snake[0] = (snake[0][0], HEIGHT - SNAKE_SIZE)
    elif snake[0][1] >= HEIGHT:
        snake[0] = (snake[0][0], 0)

    screen.fill(DARK_GRAY)

    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    draw_snake(snake)

    score_text = font.render("Score: " + str(score), True, LIGHT_GRAY)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    pygame.time.Clock().tick(SNAKE_SPEED)

game_over_screen()

pygame.quit()