import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders Easy")
WHITE = (255, 255, 255)
player = pygame.Rect(370, 480, 40, 40)

enemies = []
for i in range(7):
    enemies.append(pygame.Rect(random.randint(0, 760), random.randint(50, 150), 40, 40))
score = 0
font = pygame.font.Font(None, 36)
running = True
while running:
    screen.fill((0, 0, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    pygame.draw.rect(screen, (0, 255, 0), player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 760)
            enemy.y = random.randint(50, 150)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()
