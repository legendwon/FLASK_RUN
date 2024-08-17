from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app) # SQLALchemy 초기화.
    migrate.init_app(app,db)
    from . import models

    #블루 프린트
    from .views import main_views , question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    
    return app

