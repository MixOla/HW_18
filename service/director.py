from dao.director import DirectorDAO
from typing import List

from dao.model.director import Director


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> List[Director]:
        return self.director_dao.get_all()

    def get_one(self, director_id) -> List[Director]:
        return self.director_dao.get_one(director_id)