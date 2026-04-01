import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
player_size = 50
player = pygame.Rect(WIDTH//2, HEIGHT//2, player_size, player_size)
player_speed = 5
enemy_size = 40
enemies = []
for _ in range(7):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, HEIGHT - enemy_size)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))
score = 0
font = pygame.font.SysFont(None, 36)
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    player.clamp_ip(screen.get_rect())
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, WIDTH - enemy_size)
            enemy.y = random.randint(0, HEIGHT - enemy_size)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()