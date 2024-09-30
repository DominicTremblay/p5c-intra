from flask import Flask
from app.extensions import db, migrate, seeder
from app.api import api_bp

def create_app():
    app = Flask(__name__)

    # Load the configuration from config.py or environment variables
    app.config.from_object('config.Config')

    # Initialize the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)  # Initialize seeder with app and db

    from app.modeles import Film 

    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
