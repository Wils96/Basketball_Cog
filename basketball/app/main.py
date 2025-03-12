# main.py

from flask import Flask
from admin.admin_routes import admin_bp
from game.game_routes import game_bp

def create_app():
    app = Flask(__name__)

    # Set a secret key for sessions
    app.secret_key = "some-secret-key-string"

    # Register the blueprints
    app.register_blueprint(admin_bp)
    app.register_blueprint(game_bp)

    @app.route('/')
    def index():
        return "Welcome to the Wheelchair Basketball Decision Game (Admin & Game Routes Available)"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
