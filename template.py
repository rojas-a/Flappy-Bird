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
    # TODO:
    # Draw the floor twice so it can scroll seamlessly
    # Hint: use floor_x_pos and floor_surface.get_width()
    pass


def create_pipe():
    # TODO:
    # 1. Pick a random pipe height from pipe_heights
    # 2. Create a bottom pipe coming from the bottom
    # 3. Create a top pipe coming from the top
    # 4. Return both pipes
    #
    # Hint:
    # bottom_pipe = pipe_surface.get_rect(...)
    # top_pipe = pipe_surface.get_rect(...)
    pass


def move_pipes(pipes):
    # TODO:
    # Move every pipe to the left
    # Then return only the pipes still visible on screen
    pass


def draw_pipes(pipes):
    # TODO:
    # Draw bottom pipes normally
    # Flip the image vertically for top pipes
    pass


def check_collision(pipes):
    # TODO:
    # Return False if the bird hits any pipe
    # Return False if the bird flies too high or hits the floor
    # Otherwise return True
    pass


def display_score():
    score_surface = font.render(f"Score: {int(score)}", True, (255, 255, 255))
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
            # TODO:
            # If SPACE is pressed and the game is active:
            #   make the bird jump
            #
            # If SPACE is pressed and the game is over:
            #   restart the game
            pass

        if event.type == SPAWNPIPE and game_active:
            # TODO:
            # Add two new pipes to pipe_list
            pass

    # draw background
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # TODO:
        # 1. Apply gravity to bird_movement
        # 2. Move the bird vertically
        # 3. Draw the bird
        # 4. Move and draw pipes
        # 5. Check for collisions
        # 6. Update score
        # 7. Display score
        pass

    else:
        screen.blit(game_over_surface, game_over_rect)
        display_score()

    # TODO:
    # Scroll the floor to the left
    # Reset floor_x_pos when needed
    # Draw the floor
    pass

    pygame.display.update()
    clock.tick(60)