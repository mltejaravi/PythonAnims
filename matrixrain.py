import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")

# Font and symbols
FONT_SIZE = 20
FONT = pygame.font.SysFont("consolas", FONT_SIZE)
SYMBOLS = [chr(i) for i in range(33, 127)]  # Printable ASCII

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 70)
DARK_GREEN = (0, 180, 50)

# Calculate columns
columns = WIDTH // FONT_SIZE
drops = [random.randint(-20, 0) for _ in range(columns)]

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw symbols for each column
    for i in range(columns):
        char = random.choice(SYMBOLS)
        x = i * FONT_SIZE
        y = drops[i] * FONT_SIZE

        # Bright green character (the leading symbol)
        text = FONT.render(char, True, GREEN)
        screen.blit(text, (x, y))

        # Darker trailing character
        trail_y = y - FONT_SIZE
        if trail_y >= 0:
            trail_char = random.choice(SYMBOLS)
            trail_text = FONT.render(trail_char, True, DARK_GREEN)
            screen.blit(trail_text, (x, trail_y))

        drops[i] += 1

        # Reset drop to top randomly
        if y > HEIGHT or random.random() > 0.975:
            drops[i] = random.randint(-20, 0)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
