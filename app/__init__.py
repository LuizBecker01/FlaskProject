from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configs do app
    app.config.from_object('config.config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2404@localhost:5432/CNMD'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o SQLAlchemy com app
    db.init_app(app)

    # Importa e registra o Blueprints

    from app.main import main as main_blueprint
    from app.main import blueprint as api_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)

    return app