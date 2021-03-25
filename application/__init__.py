from flask import Flask

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.TestingConfig")

    with app.app_context():
        from . import routes  # Import routes
        
        return app
