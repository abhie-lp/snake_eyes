"""Main application file"""

from flask import Flask


def create_app() -> Flask:
    """Create Flask application using the app factory pattern"""
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def index():
        """Simple Hello, World! response"""
        return "Hello, World!"

    return app
