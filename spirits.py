import pygame
import sys
# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Sprites")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
sprite1 = pygame.Rect(100, 100, 50, 50)  # Controlled by user
sprite2 = pygame.Rect(300, 300, 50, 50)  # Static
speed = 5
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite1.x += speed
    if keys[pygame.K_UP]:
        sprite1.y -= speed
    if keys[pygame.K_DOWN]:
        sprite1.y += speed
    pygame.draw.rect(screen, RED, sprite1)
    pygame.draw.rect(screen, BLUE, sprite2)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
