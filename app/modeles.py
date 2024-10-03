from app.extensions import db

class Film(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  titre = db.Column(db.String(100), nullable=False)
  genre = db.Column(db.String(50))
  annee_sortie = db.Column(db.Integer)
