from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

# Initialize the extensions here
db = SQLAlchemy()      # Initialize SQLAlchemy
migrate = Migrate()    # Initialize Flask-Migrate
seeder = FlaskSeeder() # Initialize Flask-Seeder (but to be connected to app later)
