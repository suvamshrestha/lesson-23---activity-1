import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders Easy with Images")

# Load and scale images
player_img = pygame.transform.scale(pygame.image.load("lol.jpg"), (40, 40))
enemy_img = pygame.transform.scale(pygame.image.load("p.jpg"), (40, 40))

# Player
player_x = 370
player_y = 480
player_speed = 5

# Enemies
enemies = []
for i in range(7):
    enemies.append([random.randint(0, 760), random.randint(50, 150)])
enemy_speed = 1

# Score
score = 0
font = pygame.font.Font(None, 36)

# Frame rate control
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep player on screen
    player_x = max(0, min(player_x, 800 - 40))
    player_y = max(0, min(player_y, 600 - 40))

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw enemies + move + check collision
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > 600:
            enemy[0] = random.randint(0, 760)
            enemy[1] = random.randint(50, 150)

        screen.blit(enemy_img, (enemy[0], enemy[1]))

        player_rect = pygame.Rect(player_x, player_y, 40, 40)
        enemy_rect = pygame.Rect(enemy[0], enemy[1], 40, 40)
        if player_rect.colliderect(enemy_rect):
            score += 1
            enemy[0] = random.randint(0, 760)
            enemy[1] = random.randint(50, 150)

    # Show score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

