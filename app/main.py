from flask import Flask, jsonify, request, render_template, Blueprint
from flask_login import current_user
from sqlalchemy import create_engine, update, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import flag_modified
from flask_sqlalchemy import SQLAlchemy
from models import User

db = SQLAlchemy()

db_string = "postgresql://postgres:2404@localhost:5432/CNMD"
db_ = create_engine(db_string)
Base = declarative_base()
Session = sessionmaker(db_)
session = Session()
Base.metadata.create_all(db_)

app = Flask(__name__)

db.init_app(app)

blueprint = Blueprint('api', __name__, url_prefix='/api')

@app.route('/')  
def homepage():
    users = User.query.all()
    for user in users:
        print(user.username)
    return render_template ("index.html")

# Rota para criar um novo usuário
@blueprint.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Verifica se o usuário já existe
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(message='Usuário já existe!', created=0)

    new_user = User(username=username, password=password)
    
    # Adiciona o novo usuário ao banco de dados
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='Usuário '+username+' criado com sucesso!', created=1)

# Rota para deletar um usuário
@blueprint.route('/delte_user', methods=['POST'])
def delete_user():
    username = request.form['username']
    if current_user.username == username:
        return jsonify(message='Voce não pode deletar o usuário atual', deleted=0)
    else:
        user = User.query.filter_by(username=username).first()
        
        db.session.delete(user)
        db.session.commit()

        return jsonify(message='Usuário '+username+' deletado com sucesso!', deleted=1)

if __name__ == "__main__":
    app.run(debug=True)