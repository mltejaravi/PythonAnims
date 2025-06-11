import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starry Sky with Moon")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MOON = (245, 245, 220)  # Light beige moon color

# Moon position and radius
moon_x, moon_y = WIDTH // 2, HEIGHT // 2
moon_radius = 60

# Star setup
NUM_STARS = 100
stars = []

for _ in range(NUM_STARS):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    blink_speed = random.uniform(0.02, 0.1)
    stars.append({"x": x, "y": y, "alpha": 255, "dir": -1, "speed": blink_speed})

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Draw moon
    pygame.draw.circle(screen, MOON, (moon_x, moon_y), moon_radius)

    # Draw blinking stars
    for star in stars:
        star["alpha"] += star["dir"] * star["speed"] * 255
        if star["alpha"] <= 50:
            star["dir"] = 1
        elif star["alpha"] >= 255:
            star["dir"] = -1

        alpha = max(50, min(255, int(star["alpha"])))
        star_color = (alpha, alpha, alpha)
        pygame.draw.circle(screen, star_color, (star["x"], star["y"]), 2)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
