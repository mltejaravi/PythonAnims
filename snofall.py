import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowfall Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Snowflake class
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.radius = random.randint(1, 4)
        self.speed = random.uniform(1, 3)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)

# Create snowflakes
snowflakes = [Snowflake() for _ in range(200)]

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw snowflakes
    for flake in snowflakes:
        flake.fall()
        flake.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
