
from setup_db import db

class Genre(db.Model):
    # Создаем модель для жанра
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))