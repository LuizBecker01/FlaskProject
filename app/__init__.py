from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.config')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2404@localhost:5432/CNMD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importa e registra o Blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
