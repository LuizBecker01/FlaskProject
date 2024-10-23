from flask import Flask, jsonify, request, render_template, Blueprint, session, redirect, url_for
from app import db
from app.models import User

main = Blueprint('main', __name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')

# Rota principal
@main.route('/')  
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

# Rota para login
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
         # Configurando a sessão do usuário
            session['user_id'] = user.id
            session['logged_in'] = True

            # Redireciona para a página principal
            return redirect(url_for('main.home'))
        else:
            return jsonify(message='Credenciais inválidas!', logged=0)
    return render_template('login.html')

#Rota para Sobre
@main.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para criar um novo usuário
@main.route('/create_user', methods=['POST'])
def create_user():
    # username = request.form['username']
    # email = request.form['email']
    # password = request.form['password']

    # # Verifica se o usuário já existe
    # user = User.query.filter_by(username=username).first()
    # if user:
    #     return jsonify(message='Usuário já existe!', created=0)
    
    if request.method == 'POST':
        username = request.form['username']
        email= request.form['email']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
         # Configurando a sessão do usuário
            session['user_id'] = user.id
            session['email'] = user.email
            session['logged_in'] = True

            # Redireciona para a página principal
            return redirect(url_for('main.home'))
        else:
            return jsonify(message='Credenciais inválidas!', logged=0)

    new_user = User(username=username, email=email, password=password)
    
    # Adiciona o novo usuário ao banco de dados
    db.session.add(new_user)
    db.session.commit()

    return render_template('singup.html')

# Registra os blueprints
def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(blueprint)