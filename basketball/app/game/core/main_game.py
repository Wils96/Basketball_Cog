
from pygame import Rect
from game_logic import GameLogic
from sprites import PlayerSprite

# initialize Pygame…
player = PlayerSprite(...)
logic  = GameLogic()

running = True
while running:
    # … event handling …

    # 1) Update player sprite
    player.update()

    # 2) Check for scenario triggers
    logic.update(player.rect)

    # 3) Render court, all sprites, any scenario UI overlays
    screen.fill((0,0,0))
    # draw court, player, defenders, UI…
    pygame.display.flip()
