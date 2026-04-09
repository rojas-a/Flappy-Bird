import pygame
import sys
import random

pygame.init()

# -----------------------------
# SETUP
# -----------------------------
WIDTH = 288
HEIGHT = 512
FLOOR_Y = HEIGHT - 75

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Workshop")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# -----------------------------
# LOAD ASSETS
# -----------------------------
bg_surface = pygame.image.load("assets/background-night.png").convert()
floor_surface = pygame.image.load("assets/base.png").convert()
bird_surface = pygame.image.load("assets/bluebird-midflap.png").convert_alpha()
pipe_surface = pygame.image.load("assets/pipe-green.png").convert()
game_over_surface = pygame.image.load("assets/message.png").convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

bird_rect = bird_surface.get_rect(center=(50, HEIGHT // 2))

# -----------------------------
# GAME VARIABLES
# -----------------------------
gravity = 0.25
bird_movement = 0
game_active = True

floor_x_pos = 0

pipe_list = []
pipe_heights = [200, 250, 300, 350, 400]

score = 0

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# -----------------------------
# FUNCTIONS
# -----------------------------
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, FLOOR_Y))
    screen.blit(floor_surface, (floor_x_pos + floor_surface.get_width(), FLOOR_Y))


def create_pipe():
    random_pipe_pos = random.choice(pipe_heights)

    bottom_rect = pipe_surface.get_rect(midtop=(WIDTH + 50, random_pipe_pos))
    top_rect = pipe_surface.get_rect(midbottom=(WIDTH + 50, random_pipe_pos - 150))

    bottom_pipe = {
        "rect": bottom_rect,
        "flipped": False,
        "scored": False
    }

    top_pipe = {
        "rect": top_rect,
        "flipped": True,
        "scored": False
    }

    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe["rect"].centerx -= 4

    visible_pipes = [pipe for pipe in pipes if pipe["rect"].right > -50]
    return visible_pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe["flipped"]:
            flipped_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flipped_pipe, pipe["rect"])
        else:
            screen.blit(pipe_surface, pipe["rect"])


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe["rect"]):
            return False

    if bird_rect.top <= -50 or bird_rect.bottom >= FLOOR_Y:
        return False

    return True


def update_score():
    global score

    for pipe in pipe_list:
        if not pipe["flipped"] and not pipe["scored"]:
            if pipe["rect"].right < bird_rect.left:
                score += 1
                pipe["scored"] = True


def display_score():
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(score_surface, score_rect)


def reset_game():
    global bird_movement, score

    pipe_list.clear()
    bird_rect.center = (50, HEIGHT // 2)
    bird_movement = 0
    score = 0


# -----------------------------
# MAIN GAME LOOP
# -----------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 5

            elif event.key == pygame.K_SPACE and not game_active:
                game_active = True
                reset_game()

        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface, (0, 0))

    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)

        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        game_active = check_collision(pipe_list)

        update_score()
        display_score()

    else:
        screen.blit(game_over_surface, game_over_rect)
        display_score()

    floor_x_pos -= 1
    if floor_x_pos <= -floor_surface.get_width():
        floor_x_pos = 0
    draw_floor()

    pygame.display.update()
    clock.tick(60)