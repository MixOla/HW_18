from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        # Инициализируем сессию
        self.session = session

    def get_one(self, gid):
        # Получаем список всех фильмов по id
        return self.session.query(Genre).get(gid)

    def get_all(self):
        # Получаем список всех жанров
        return self.session.query(Genre).all()


