from flask_restx import Resource, Namespace

from dao.model.schemas import DirectorSchema
from implemented import director_service

director_ns = Namespace('director')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    # Возвращает подробную информацию о режиссере
    def get(self, director_id):
        director_by_id = director_service.get_one(director_id)

        if director_by_id is None:
            return {}, 404

        return director_schema.dump(director_by_id), 200


@director_ns.route('/')
class DirectorView(Resource):
    # Возвращает список всех режиссеров
    def get(self):
        directors = director_service.get_directors()

        return directors_schema.dump(directors), 200
