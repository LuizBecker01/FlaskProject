from flask import Flask, jsonify, request, render_template, Blueprint 
from app import db
from app.models import User

main = Blueprint('main', __name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')

# Rota principal
@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

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

    new_user = User(username=username, email=email, password=password)

    # Adiciona o novo usuário ao banco de dados
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='Usuário criado com sucesso!', created=1)

# Rota para deletar um usuário (opcional, comentada por enquanto)

# Registra os blueprints
def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(blueprint)

# if __name__ == "__main__": 
#      app.run(host="0.0.0.0", port=8001 ,debug=True)