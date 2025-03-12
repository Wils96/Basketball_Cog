# admin_routes.py

from flask import Blueprint, request, jsonify
from .admin_controller import AdminController

admin_bp = Blueprint('admin_bp', __name__)
admin_controller = AdminController()

@admin_bp.route('/admin/start', methods=['POST'])
def start_game():
    """
    Start the game session.
    We call the 'start_game' logic in our AdminController.
    """
    admin_controller.start_game()
    return jsonify({"message": "Game started"}), 200

@admin_bp.route('/admin/stop', methods=['POST'])
def stop_game():
    """
    Stop the current game session.
    """
    admin_controller.stop_game()
    return jsonify({"message": "Game stopped"}), 200

@admin_bp.route('/admin/results', methods=['GET'])
def view_results():
    """
    View all collected results from the current/previous game session(s).
    """
    results = admin_controller.get_results()
    return jsonify({"results": results}), 200

@admin_bp.route('/admin/status', methods=['GET'])
def game_status():
    """
    Check if the game is active or not.
    """
    status = {
        "game_active": admin_controller.is_game_active()
    }
    return jsonify(status), 200
