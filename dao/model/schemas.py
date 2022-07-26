
from marshmallow import Schema, fields

# Cериализация модели Director
class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

# Cериализация модели Genre
class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

# Cериализация модели Movie
class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)