import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainfall Animation")

# Colors
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)  # Light blue raindrops

# Raindrop class
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.length = random.randint(10, 20)
        self.speed = random.uniform(4, 8)
        self.thickness = random.randint(1, 2)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        end_y = self.y + self.length
        pygame.draw.line(surface, BLUE, (self.x, self.y), (self.x, end_y), self.thickness)

# Create raindrops
raindrops = [Raindrop() for _ in range(300)]

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw raindrops
    for drop in raindrops:
        drop.fall()
        drop.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
