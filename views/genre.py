from flask_restx import Resource, Namespace
from dao.model.schemas import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genre')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    # Возвращает жанр по id
    def get(self, gid):
        genre_by_id = genre_service.get_one(gid)

        if genre_by_id is None:
            return {}, 404

        return genre_schema.dump(genre_by_id), 200


@genre_ns.route('/')
class GenreView(Resource):
    # Возвращает список всех жанров
    def get(self):
        genres = genre_service.get_genres()
        return genres_schema.dump(genres), 200

