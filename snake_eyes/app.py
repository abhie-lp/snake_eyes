"""Main application file"""

from flask import Flask


def create_app() -> Flask:
    """Create Flask application using the app factory pattern"""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    @app.route("/")
    def index():
        """Simple Hello, World! response"""
        return "Hello World!"

    return app
