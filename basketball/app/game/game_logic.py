# game/core/game_logic.py

import pygame

class Scenario:
    """
    Represents a live 2D scenario triggered by the player entering a zone.
    """
    def __init__(self, id: str, trigger_zone: pygame.Rect, callback: callable):
        self.id = id                                # unique identifier
        self.trigger_zone = trigger_zone            # pygame.Rect where scenario triggers
        self.callback = callback                    # function to call when triggered
        self.has_triggered = False                  # ensure one-time activation per entry

    def try_trigger(self, player_rect: pygame.Rect):
        """
        If the player enters the trigger_zone for the first time,
        call the associated callback.
        """
        if not self.has_triggered and self.trigger_zone.colliderect(player_rect):
            self.has_triggered = True
            self.callback(self)
            

class GameLogic:
    """
    Manages all live scenarios and dispatches callbacks.
    """
    def __init__(self):
        self.scenarios = self._load_scenarios()
        self.score = 0

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
            # ... add more scenarios here
        ]

    def update(self, player_rect: pygame.Rect):
        """
        Call once per frame with the player's current bounding rect.
        """
        for scenario in self.scenarios:
            scenario.try_trigger(player_rect)

    # --- Scenario callbacks below ---
    def _on_fast_break(self, scenario: Scenario):
        """
        Called when the player enters the fast break zone.
        You might spawn defenders, start a timer, etc.
        """
        print("[Fast Break] You’ve hit open court! Drive to the basket!")
        # e.g. self.spawn_defenders(), start timer, highlight court, etc.

    def _on_pass_under_pressure(self, scenario: Scenario):
        print("[Pressure] Defender closing in — choose to pass or drive!")
        # e.g. slow player speed, flash UI options, enable pass key

    def _on_rebound_challenge(self, scenario: Scenario):
        print("[Rebound] Ball is loose! Fight for position!")
        # e.g. drop ball sprite, enable grip controls, track rebound outcome

    # You can add more callbacks for different scenarios,
    # each manipulating the game state, UI, sprites, and self.score as needed.
