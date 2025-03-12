# game_logic.py

class Scenario:
    """
    A small helper class to hold the data for each scenario.
    """
    def __init__(self, description, choices):
        self.description = description   # string describing situation
        self.choices = choices           # dict of {choice: {score_change, outcome_text}}

# Create a sequence of scenarios
SCENARIOS = [
    Scenario(
        description="You have the ball at the top of the key. An opponent is closing in. Do you pass, shoot, or block?",
        choices={
            "pass":  {"score_change": 2,  "outcome_text": "You passed successfully to a teammate."},
            "shoot": {"score_change": 3,  "outcome_text": "You took a shot. It's good!"},
            "block": {"score_change": 0,  "outcome_text": "You can't block while you have the ball. No gain."}
        }
    ),
    Scenario(
        description="You are under heavy defense. A teammate signals they're open. Do you pass or try to shoot through the defense?",
        choices={
            "pass":  {"score_change": 1,  "outcome_text": "Safe pass, minimal risk."},
            "shoot": {"score_change": 2,  "outcome_text": "Challenging shot, but you made it!"},
            "block": {"score_change": -1, "outcome_text": "Attempting to block isn't relevant here. You lost time."}
        }
    ),
    Scenario(
        description="An opponent is about to shoot. You can attempt a block or focus on rebounding. Your move?",
        choices={
            "block":   {"score_change": 3, "outcome_text": "Great block!"},
            "passing": {"score_change": 0, "outcome_text": "You tried to pass, but you don't have the ball!"},
            "shoot":   {"score_change": 0, "outcome_text": "Shooting isn't possible if you don't have the ball."}
        }
    ),
]

class GameLogic:
    """
    This class handles the main flow: current scenario, scoring, moving to next scenario.
    """

    @staticmethod
    def get_scenario(scenario_index: int) -> Scenario:
        """
        Returns the scenario at the given index, or None if out of range.
        """
        if 0 <= scenario_index < len(SCENARIOS):
            return SCENARIOS[scenario_index]
        return None

    @staticmethod
    def get_total_scenarios() -> int:
        return len(SCENARIOS)
