from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Carregango configuraçõess do config.py
app.config.from_object('config.config')

# Definindo a URI do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:2404@localhost:5432/CNMD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importa as rotas e modelos
from . import main
from . import models
