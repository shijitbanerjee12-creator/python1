import pygame
import sys
pygame.font.init() 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Elements Example")
font = pygame.font.SysFont(None, 48)
text_surface = font.render('Hello, Pygame!', True, WHITE)
text_rect = text_surface.get_rect() 
text_rect.center = (SCREEN_WIDTH // 2, 50) 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK) 
    pygame.draw.rect(screen, BLUE, (100, 150, 200, 100), 0) 
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
pygame.quit()
sys.exit()
