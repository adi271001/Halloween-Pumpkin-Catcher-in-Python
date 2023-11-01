import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
PUMPKIN_SIZE = 50
PLAYER_SIZE = 50
PLAYER_SPEED = 5
PUMPKIN_SPEED = 3

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spooky Pumpkin Catcher")

# Load images
player_img = pygame.image.load("player.png")
pumpkin_img = pygame.image.load("pumpkin.png")

# Initialize player position
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = HEIGHT - PLAYER_SIZE

# Initialize pumpkins
pumpkins = []

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Game loop
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED

    # Create new pumpkins
    if len(pumpkins) < 5:
        pumpkin_x = random.randint(0, WIDTH - PUMPKIN_SIZE)
        pumpkin_y = 0
        pumpkins.append([pumpkin_x, pumpkin_y])

    # Move and draw pumpkins
    for pumpkin in pumpkins:
        pumpkin[1] += PUMPKIN_SPEED
        screen.blit(pumpkin_img, (pumpkin[0], pumpkin[1]))

    # Remove pumpkins that go off the screen
    pumpkins = [p for p in pumpkins if p[1] < HEIGHT]

    # Check for collisions
    for pumpkin in pumpkins:
        if (
            player_x < pumpkin[0] + PUMPKIN_SIZE
            and player_x + PLAYER_SIZE > pumpkin[0]
            and player_y < pumpkin[1] + PUMPKIN_SIZE
            and player_y + PLAYER_SIZE > pumpkin[1]
        ):
            pumpkins.remove(pumpkin)
            score += 1

    # Clear the screen
    screen.fill(BLACK)

    # Draw the player
    screen.blit(player_img, (player_x, player_y))

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
