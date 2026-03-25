import pygame
import random
pygame.init()
screen = pygame.display.set_mode([600, 400])
clock = pygame.time.Clock()
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000) 
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def change_color(self):
        self.image.fill(random.choice(COLORS))
all_sprites = pygame.sprite.Group()
s1, s2 = ColorSprite((255,0,0), 150, 150), ColorSprite((0,0,255), 400, 150)
all_sprites.add(s1, s2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == CHANGE_COLOR:
            for sprite in all_sprites: sprite.change_color()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
