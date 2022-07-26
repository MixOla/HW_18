# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace

from dao.model.schemas import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movie')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
@movie_ns.param("director_id")
@movie_ns.param("genre_id")
@movie_ns.param("year")
class MoviesView(Resource):
    # Возвращает список всех фильмов
    def get(self):
        movies_query = movie_service.get_all()

        args = request.args

        # director_id = args.get('director_id')
        # if director_id is not None:
        #     movies_query = movies_query.filter(models.Movie.director_id == director_id)
        #
        # genre_id = args.get('genre_id')
        # if genre_id is not None:
        #     movies_query = movies_query.filter(models.Movie.genre_id == genre_id)

        movies = movies_query.all()

        return movies_schema.dump(movies), 200

    def post(self):
        reg_json = request.json
        movie_service.create(reg_json)

        return None, 201


@movie_ns.route('/<int:bid>/')
class MovieView(Resource):
    # Возвращает подробную информацию о фильме
    def get(self, bid: int):
        movie_by_id = movie_service.get_one(bid)

        if movie_by_id is None:
            return {}, 404

        return movie_schema.dump(movie_by_id), 200

    def put(self, mid: int):
        req_json = request.json
        req_json["id"] = mid
        updated_rows = movie_service.update(req_json)
        if updated_rows != 1:
            return None, 400

        return None, 204

    def patch(self, mid: int):
        req_json = request.json
        req_json["id"] = mid
        updated_rows = movie_service.update_partialy(req_json)
        if updated_rows != 1:
            return None, 400

        return None, 204

    def delete(self, mid: int):
        deleted_rows = movie_service.delete(mid)
        if deleted_rows != 1:
            return None, 400

        return None, 200
