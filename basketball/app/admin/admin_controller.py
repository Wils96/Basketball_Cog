# admin_controller.py

class AdminController:
    """
    This class encapsulates the business logic for administrator actions.
    For instance, starting/stopping the game, fetching results, etc.
    """

    def __init__(self):
        # If you need to track game state in-memory, do it here,
        # or connect to a database if needed.
        self.game_active = False
        self.results = []

    def start_game(self):
        """Mark the game as active and initialize any necessary data."""
        self.game_active = True
        # You could reset results or other counters here.
        print("Game started")

    def stop_game(self):
        """End the current game session."""
        self.game_active = False
        print("Game stopped")

    def record_result(self, result_data):
        """
        Store result data from players.
        In a real app, you'd insert into a DB or a file.
        """
        self.results.append(result_data)

    def get_results(self):
        """
        Return whatever results you've collected.
        In a real app, retrieve from DB or file.
        """
        return self.results

    def is_game_active(self):
        """Helper method to check if a game is currently active."""
        return self.game_active
