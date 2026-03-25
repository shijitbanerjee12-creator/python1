import pygame

# Initialize Pygame
pygame.init()

# Set up the game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define the Sprite class
class RectangleSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        # Create a surface for the sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Get the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move(self, dx, dy):
        """Moves the sprite and keeps it within the screen boundaries."""
        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(screen.get_rect())

# Create two sprite objects
player = RectangleSprite(BLUE, 50, 50, 100, 100) # Controllable sprite
obstacle = RectangleSprite(RED, 60, 40, 400, 300) # Static sprite

# Add sprites to a group for easy management
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(obstacle)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Movement Controls (for the Blue sprite)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-player.speed, 0)
    if keys[pygame.K_RIGHT]:
        player.move(player.speed, 0)
    if keys[pygame.K_UP]:
        player.move(0, -player.speed)
    if keys[pygame.K_DOWN]:
        player.move(0, player.speed)

    # 3. Drawing
    screen.fill(WHITE)           # Clear the screen
    all_sprites.draw(screen)      # Draw all sprites in the group
    pygame.display.flip()         # Update the display

    # 4. Control Frame Rate (60 FPS)
    clock.tick(60)

pygame.quit()
