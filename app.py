# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение


from flask import Flask
from flask_restx import Api

from config import Config
#from create_db import create_database
from setup_db import db
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


# функция создания основного объекта application
def create_app(config_object: Config):  # Привязываем конфиги
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()  # Применяем конфигурацию во все будущие компоненты
    return application


# функция конфигурации приложения
def register_extensions(application):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)

# create_database()

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    register_extensions(app)
    app.run(host="localhost", port=10001)
