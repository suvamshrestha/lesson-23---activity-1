import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Add Image to Screen')
background_image = pygame.transform.scale(pygame.image.load('penguin.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
penguin_image = pygame.transform.scale(pygame.image.load('penguin.jpg').convert_alpha(), (100, 100))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
text = pygame.font.Font(None, 36).render('hello world', True,pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
def game_Loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_Loop()

