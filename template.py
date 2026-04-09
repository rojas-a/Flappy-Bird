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

# custom event for spawning pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# -----------------------------
# FUNCTIONS
# -----------------------------
def draw_floor():
    # TODO:
    # Draw the floor twice so it scrolls continuously
    # Hint:
    #   one floor starts at floor_x_pos
    #   the second starts right after the first one ends
    pass


def create_pipe():
    # TODO:
    # 1. Pick a random height from pipe_heights
    # 2. Create a bottom pipe rect
    # 3. Create a top pipe rect
    # 4. Store each pipe in a dictionary with:
    #       "rect"
    #       "flipped"
    #       "scored"
    # 5. Return both pipes
    #
    # Hint:
    # bottom_pipe = {
    #     "rect": ...,
    #     "flipped": False,
    #     "scored": False
    # }
    #
    # top_pipe should have "flipped": True
    pass


def move_pipes(pipes):
    # TODO:
    # Move every pipe to the left
    # Each pipe is a dictionary, so use pipe["rect"]
    #
    # Then return only the pipes that are still visible
    pass


def draw_pipes(pipes):
    # TODO:
    # Loop through each pipe
    # If pipe["flipped"] is True, draw a flipped version
    # Otherwise draw the normal pipe
    pass


def check_collision(pipes):
    # TODO:
    # If bird_rect collides with any pipe rect, return False
    # If bird goes too high or hits the floor, return False
    # Otherwise return True
    pass


def update_score():
    global score

    # TODO:
    # Only score bottom pipes:
    #   if not pipe["flipped"]
    #
    # Only score pipes once:
    #   if not pipe["scored"]
    #
    # When the pipe has fully passed the bird,
    # increase score by 1 and mark it as scored
    #
    # Hint:
    # if pipe["rect"].right < bird_rect.left:
    #     ...
    pass


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
            # TODO:
            # If SPACE is pressed and the game is active:
            #   reset bird_movement to 0
            #   make the bird jump upward
            #
            # If SPACE is pressed and the game is over:
            #   restart the game
            pass

        if event.type == SPAWNPIPE and game_active:
            # TODO:
            # Add the new top and bottom pipes to pipe_list
            pass

    # draw background
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # TODO:
        # 1. Apply gravity to bird_movement
        # 2. Move the bird vertically
        # 3. Draw the bird
        screen.blit(bird_surface, bird_rect)

        # TODO:
        # 4. Move pipes
        # 5. Draw pipes
        # 6. Check for collisions
        # 7. Update score when pipes are passed
        # 8. Display score
        pass

    else:
        screen.blit(game_over_surface, game_over_rect)
        display_score()

    # TODO:
    # Scroll the floor to the left
    # Reset it when it goes too far
    # Then draw the floor
    pass

    pygame.display.update()
    clock.tick(60)