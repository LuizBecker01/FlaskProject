from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from sqlalchemy import create_engine, update, and_
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import flag_modified

db = SQLAlchemy()

# Crie o engine do SQLAlchemy manualmente se precisar de um para a sessão
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()

# Base.metadata.create_all(engine)

def create_app():
    app = Flask(__name__)

    # Configurações do app
    app.config.from_object('config.config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2404@localhost:5432/CNMD'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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