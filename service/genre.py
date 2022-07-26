from dao.genre import GenreDAO
from typing import List

from dao.model.genre import Genre


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self) -> List[Genre]:
        return self.genre_dao.get_all()

    def get_one(self, genre_id) -> List[Genre]:
        return self.genre_dao.get_one(genre_id)
