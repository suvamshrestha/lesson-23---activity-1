import pygame
import random
# Initialize Pygame
pygame.init()
# Window size
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colorful Bounce")
clock = pygame.time.Clock()
rect_width, rect_height = 60, 40
x, y = random.randint(0, width - rect_width), random.randint(0, height - rect_height)
x_vel, y_vel = 5, 4
rect_color = (255, 0, 0)
bg_color = (0, 0, 0)
# Function to generate random color
def random_color():
      return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
running = True
while running:
    screen.fill(bg_color)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        running = False
# Move rectangle
    x += x_vel
    y += y_vel
# Bounce and change colors
    if x <= 0 or x + rect_width >= width:
      x_vel *= -1
      rect_color = random_color()
      bg_color = random_color()
    if y <= 0 or y + rect_height >= height:
      y_vel *= -1
      rect_color = random_color()
      bg_color = random_color()
# Draw rectangle
    pygame.draw.rect(screen, rect_color, (x, y, rect_width, rect_height))
# Update display
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
