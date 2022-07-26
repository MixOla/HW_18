# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from dao.model.movie import Movie
from dao.movie import MovieDAO
from typing import List

class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> List[Movie]:
        return self.movie_dao.get_all()

    def get_one(self, movie_id) -> List[Movie]:
        return self.movie_dao.get_one(movie_id)

    def create(self, data):
        return self.movie_dao.create(data)

    def get_movie_by(self, director_id=None, genre_id=None, year=None):

        if director_id is not None:
            return self.movie_dao.get_movie_by_director(director_id)

        elif genre_id is not None:
            return self.movie_dao.get_movie_by_genre(genre_id)

        elif year is not None:
            return self.movie_dao.get_movie_by_year(year)

        else:
            return []

    def add_movie(self, data) -> None:
        self.movie_dao.create(**data)

    def update_movie(self, data) -> None:
        self.movie_dao.update(**data)
        3
    def delete_movie(self, id) -> None:
        self.movie_dao.delete(id)