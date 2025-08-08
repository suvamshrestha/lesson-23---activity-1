import random
import pygame
import sys
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Collision")
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))
white = (255, 255, 255)
font = pygame.font.SysFont(None, 55)
player = pygame.Rect(100, 100, 50, 50)
enemy = pygame.Rect(600,400,50,50)
player_color = (0, 128, 255)
enemy_color = (255, 0, 0)
speed = 2
def show_message(text):
    msg = font.render(text, True, (255, 255, 0))
    rect = msg.get_rect(center=(screen_width//2, screen_height//2))
    screen.blit(msg, rect)
    pygame.display.flip()
    pygame.time.delay(2000)
def restart_prompt():
    while True:
     screen.fill(white)
     show_message("You Win! Press Y to Restart or N to Exit")
     pygame.display.flip()
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_y:
         return True
        elif event.key == pygame.K_n:
          pygame.quit()
          sys.exit()
def game_loop():
   global player
   player = pygame.Rect(100, 100, 50, 50)
   while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      player.x -= speed
    if keys[pygame.K_RIGHT]:
      player.x += speed
    if keys[pygame.K_UP]:
      player.y -= speed
    if keys[pygame.K_DOWN]:
      player.y += speed
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, enemy_color, enemy)
    if player.colliderect(enemy):
      show_message("You Win!")
      if restart_prompt():
       game_loop()
    pygame.display.update()
game_loop()



