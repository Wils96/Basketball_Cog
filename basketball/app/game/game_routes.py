# game_routes.py

from flask import Blueprint, render_template, request, session, redirect, url_for
from .game_logic import GameLogic

game_bp = Blueprint("game_bp", __name__, template_folder="../templates/game")

@game_bp.route("/game/start", methods=["GET"])
def start_game():
    """
    Reset or initialize session data for a new game.
    """
    session["scenario_index"] = 0
    session["score"] = 0
    return render_template("game/start.html")

@game_bp.route("/game/next", methods=["GET"])
def show_scenario():
    """
    Display the current scenario to the user. If we're past the last scenario, show results.
    """
    scenario_index = session.get("scenario_index", 0)
    total_scenarios = GameLogic.get_total_scenarios()

    if scenario_index >= total_scenarios:
        # All scenarios completed; go to results
        return redirect(url_for("game_bp.show_results"))

    scenario = GameLogic.get_scenario(scenario_index)
    return render_template("game/scenario.html", scenario_index=scenario_index, scenario=scenario)

@game_bp.route("/game/choose_action", methods=["POST"])
def choose_action():
    """
    Handle user's chosen action for the current scenario.
    Update score and scenario index, then redirect to next scenario.
    """
    choice = request.form.get("choice")
    scenario_index = session.get("scenario_index", 0)
    score = session.get("score", 0)

    scenario = GameLogic.get_scenario(scenario_index)
    if scenario:
        # If the choice exists in the scenario
        if choice in scenario.choices:
            outcome = scenario.choices[choice]
            # Update score
            score += outcome["score_change"]
            session["score"] = score
        else:
            # Invalid choice; no score update
            pass

    # Move to the next scenario
    session["scenario_index"] = scenario_index + 1

    return redirect(url_for("game_bp.show_scenario"))

@game_bp.route("/game/results", methods=["GET"])
def show_results():
    """
    Display final results after all scenarios are completed.
    """
    final_score = session.get("score", 0)
    return render_template("game/results.html", final_score=final_score)
