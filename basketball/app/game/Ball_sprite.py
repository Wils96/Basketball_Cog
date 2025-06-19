import pygame

# A gravity constant for our simulation
GRAVITY = 0.5

class Ball(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        # Create a circular ball with transparency support
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)
        self.rect = self.image.get_rect(center=position)
        # Velocity is a list: [x_velocity, y_velocity]
        self.velocity = list(velocity)

    def update(self):
        # Apply gravity
        self.velocity[1] += GRAVITY
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])
        
        # Bounce off the bottom edge of the screen (assuming window height=600)
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.velocity[1] = -self.velocity[1] * 0.7  # dampen velocity on bounce

        # Optionally remove the ball if it slows down too much
        if abs(self.velocity[0]) < 0.1 and abs(self.velocity[1]) < 0.1:
            self.kill()