import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        # For demonstration, we use three colored surfaces as frames
        self.images = []
        for color in [(255, 0, 0), (200, 0, 0), (150, 0, 0)]:
            image = pygame.Surface((50, 50))
            image.fill(color)
            self.images.append(image)
            
        self.current_frame = 0
        self.image = self.images[self.current_frame]
        self.rect = self.image.get_rect(topleft=position)
        self.animation_timer = 0
        self.animation_delay = 200  # milliseconds

    def update(self):
        self.animate()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.animation_timer > self.animation_delay:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]
            self.animation_timer = now

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        