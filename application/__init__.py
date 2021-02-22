from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.ProductionConfig")

    Bootstrap(app)

    db.init_app(app)
    

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create database tables for our data models
        
        migrate = Migrate(app, db)
        
        return app
