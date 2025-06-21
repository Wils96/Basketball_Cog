import pygame

# A gravity constant for our simulation
GRAVITY = 0.5

# filepath: /Users/sarahwilson/Desktop/Repos/Basketball_Cog/basketball/app/game/Ball_sprite.py
import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        # Load your basketball image
        self.image = pygame.image.load("assets/basketball.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.velocity = list(velocity)

    def update(self):
        self.velocity[1] += 0.5  # gravity example
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])
        
        # Bounce off the bottom edge of the screen (assuming window height=600)
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.velocity[1] = -self.velocity[1] * 0.7  # dampen velocity on bounce

        # Optionally remove the ball if it slows down too much
        if abs(self.velocity[0]) < 0.1 and abs(self.velocity[1]) < 0.1:
            self.kill()