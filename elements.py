import pygame  
import sys     
pygame.init()  
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game Window")
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
font = pygame.font.SysFont(None, 50)
text = font.render("Hello Pygame!", True, green)
running = True
while running:
    screen.fill(white)  
    pygame.draw.rect(screen, blue, (100, 100, 200, 100))
    pygame.draw.polygon(screen, red, [(400, 100), (500, 200), (300, 200)])
    screen.blit(text, (300, 300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()  
pygame.quit()
sys.exit()
