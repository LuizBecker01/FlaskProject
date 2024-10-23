from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações do app
    app.config.from_object('config.config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:luiz@localhost:5432/CNMD' #Trocar a senha

    # Inicializa o SQLAlchemy com app
    db.init_app(app)

    # Importa e registra os Blueprints
    from app.main import main as main_blueprint
    from app.main import blueprint as api_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)

    # Criação das tabelas no banco de dados
    with app.app_context():
        db.create_all()

    return app