from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models import User
from db import db


app = Flask(__name__)

dc = SQLAlchemy()

blueprint = Blueprint('api', __name__, url_prefix='/api')

@app.route('/')  
def homepage():
    return render_template ("index.html")

@blueprint.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Verifica se o usuário já existe
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(message='Usuário já existe!', created=0)

    # Cria um novo usuário
    new_user = User(username=username, password=password)
    
    # Adiciona o novo usuário ao banco de dados
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='Usuário '+username+' criado com sucesso!', created=1)

if __name__ == "__main__":
    app.run(debug=True)