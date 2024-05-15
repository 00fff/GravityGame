import pygame
import os

# Change directory to the specified path
path = "E:/GravityGame/"  # MAC OS DIRECTORY /Volumes/USB1/GravityGame/
os.chdir(path)

# Initialize Pygame
pygame.init()

# Colors
Green = (8, 143, 143)

# Main Loop Variables
clock = pygame.time.Clock()
FPS = 60
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gravity Game")

# Assets
player_idle = pygame.image.load("assets/mc.png").convert_alpha()
ground = pygame.image.load("assets/ground.png").convert_alpha()

# Classes
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_idle
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (30, 367) # Position the player at the specified location
    
    def draw(self, surface):
        surface.blit(self.image, self.rect.bottomleft)
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.image = pygame.transform.rotate(self.image, 180)
            


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = ground
        self.imageflip = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        
    def draw(self, surface):
        surface.blit(self.imageflip, self.rect.topleft)
        flipped_x = self.rect.left
        flipped_y = 400
        surface.blit(self.image, (flipped_x, flipped_y))

# Main Function
def main():
    run = True
    clock = pygame.time.Clock()
    platform = Platform(0, 0)
    player = Character()
    dy = +5
    while run:
        clock.tick(FPS)
        screen.fill(Green)
        platform.draw(screen)
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key = pygame.key.get_pressed()
        player.rect.y += dy
        if player.rect.bottom >= 367:
            player.rect.bottom = 367
        if key[pygame.K_SPACE]:
            player.rect.y -= 20
            
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
