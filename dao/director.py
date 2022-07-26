# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным


from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        # Инициализируем сессию
        self.session = session

    def get_one(self, did):
        # Получаем информацию о режиссере по id
        return self.session.query(Director).get(did)

    def get_all(self):
        # Получаем информацию о всех режиссерах
        return self.session.query(Director).all()






