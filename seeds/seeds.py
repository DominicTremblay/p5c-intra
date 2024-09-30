from flask_seeder import Seeder, Faker, generator
from app.modeles import Film  # Make sure the model is imported correctly
from app import db

class FilmSeeder(Seeder):

    def empty_database(self):
        """Supprime tous les enregistrements des tables de la base de données."""
        db.session.execute(db.delete(Film))
        db.session.commit()

    # Methode run appelee par Flask-Seeder
    def run(self):
        # First, clear the existing database entries
        self.empty_database()

        # Create a list of movies (popular films from 2023 and 2024)
        movies = [
            {"titre": "Barbie", "genre": "Comedie", "annee_sortie": 2023},
            {"titre": "Oppenheimer", "genre": "Drame", "annee_sortie": 2023},
            {"titre": "Mission: Impossible – Dead Reckoning Part One", "genre": "Action", "annee_sortie": 2023},
            {"titre": "Dune: Part Two", "genre": "Sci-Fi", "annee_sortie": 2024},
            {"titre": "Aquaman and the Lost Kingdom", "genre": "Action", "annee_sortie": 2024},
            {"titre": "Spider-Man: Across the Spider-Verse", "genre": "Animation", "annee_sortie": 2023},
            {"titre": "The Marvels", "genre": "Action", "annee_sortie": 2023},
            {"titre": "Guardians of the Galaxy Vol. 3", "genre": "Action", "annee_sortie": 2023},
            {"titre": "The Expendables 4", "genre": "Action", "annee_sortie": 2023},
            {"titre": "John Wick: Chapter 4", "genre": "Action", "annee_sortie": 2023},
        ]

        # Loop through the list and add each movie to the database
        for movie in movies:
            film = Film(titre=movie['titre'], genre=movie['genre'], annee_sortie=movie['annee_sortie'])
            print(f"Adding film: {movie['titre']}")
            self.db.session.add(film)

        # Commit the changes to the database
        self.db.session.commit()
