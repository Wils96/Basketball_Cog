import pygame
from game_logic import GameLogic
from Player_sprite import Player
jls_extract_var = Ball_sprite
from jls_extract_var import Ball

def main():
    pygame.init()
    
    # Create a window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Wheelchair Basketball Simulation")
    
    clock = pygame.time.Clock()
    
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    
    # Create a player sprite with animation
    player = Player((100, 500))
    all_sprites.add(player)
    
    # Create an instance of your game logic (manages scenarios)
    logic = GameLogic()
    
    # We'll allow shooting a ball using spacebar; there will be one ball at a time.
    ball = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Handle input for player movement and shooting
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move(5, 0)
                elif event.key == pygame.K_LEFT:
                    player.move(-5, 0)
                elif event.key == pygame.K_UP:
                    player.move(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.move(0, 5)
                elif event.key == pygame.K_SPACE:
                    # Shoot a ball (if none is active) with an initial velocity
                    if ball is None:
                        ball = Ball(player.rect.center, (5, -10))
                        all_sprites.add(ball)
        
        # Update game logic using the player's current position
        logic.update(player.rect)
        
        # Update sprites (animations and physics updates)
        all_sprites.update()
        
        # Render
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()