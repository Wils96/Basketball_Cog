# game/core/game_logic.py

import pygame
from enum import Enum

class GameState(Enum):
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3

class Scenario:
    """
    Represents a live 2D scenario triggered by the player entering a zone.
    """
    def __init__(self, id: str, trigger_zone: pygame.Rect, callback: callable):
        self.id = id                                # unique identifier
        self.trigger_zone = trigger_zone            # pygame.Rect where scenario triggers
        self.callback = callback                    # function to call when triggered
        self.has_triggered = False                  # ensure one-time activation per entry

    def try_trigger(self, player_rect: pygame.Rect, game_state):
        """
        If the player enters the trigger_zone for the first time,
        call the associated callback if the game is in PLAYING state.
        """
        if game_state == GameState.PLAYING and not self.has_triggered and self.trigger_zone.colliderect(player_rect):
            self.has_triggered = True
            self.callback(self)

class GameLogic:
    """
    Manages all live scenarios and dispatches callbacks.
    """
    def __init__(self):
        self.scenarios = self._load_scenarios()
        self.score = 0
        self.game_state = GameState.PLAYING
        self.timer = 0  # example timer for a scenario or game phase

    def _load_scenarios(self):
        # Define trigger zones and their callbacks
        return [
            Scenario(
                id="fast_break",
                trigger_zone=pygame.Rect(700, 0, 100, 600),
                callback=self._on_fast_break
            ),
            Scenario(
                id="pass_under_pressure",
                trigger_zone=pygame.Rect(350, 200, 100, 200),
                callback=self._on_pass_under_pressure
            ),
            Scenario(
                id="rebound_challenge",
                trigger_zone=pygame.Rect(400, 500, 200, 100),
                callback=self._on_rebound_challenge
            ),
            # ... add more scenarios here as needed
        ]

    def update(self, player_rect: pygame.Rect):
        """
        Call once per frame with the player's current bounding rect.
        """
        # Example: update a timer (could be used in a scenario)
        self.timer += 1

        for scenario in self.scenarios:
            scenario.try_trigger(player_rect, self.game_state)
    
    # --- Scenario callbacks below ---
    def _on_fast_break(self, scenario: Scenario):
        """
        Called when the player enters the fast break zone.
        You might spawn defenders, start a timer, adjust score, etc.
        """
        print("[Fast Break] You’ve hit open court! Drive to the basket!")
        # Example: spawn defenders or impact physics elsewhere.
        self.score += 10

    def _on_pass_under_pressure(self, scenario: Scenario):
        print("[Pressure] Defender closing in — choose to pass or drive!")
        # Example: change game state or reduce player speed.
        self.score += 5

    def _on_rebound_challenge(self, scenario: Scenario):
        print("[Rebound] Ball is loose! Fight for position!")
        # Example: update ball physics or add a mini-game challenge.
        self.score += 8

    # Additional methods can include resetting scenarios,
    # handling transitions between game states, or advanced physics interactions