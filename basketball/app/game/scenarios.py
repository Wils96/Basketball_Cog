class Scenario:
    def __init__(self, id, trigger_zone, choices):
        # choices: dict of { action_name: { score_change, outcome_text, key_hint } }
        self.choices = choices
        # …
choices = {
  "pass": {"score_change":2, "outcome":"…", "key_hint":"A"},
  "shoot":{…,"key_hint":"S"},
  "drive":{…,"key_hint":"D"}
}
