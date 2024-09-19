from flask import Flask, jsonify, request, render_template, Blueprint, current_user
from flask_sqlalchemy import SQLAlchemy
from models import User
from db import db


app = Flask(__name__)

dc = SQLAlchemy()

blueprint = Blueprint('api', __name__, url_prefix='/api')

@app.route('/')  
def homepage():
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