from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from sqlalchemy import create_engine, update, and_
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import flag_modified
from .models import User

app = Flask(__name__)

# Definir a URI de conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2404@localhost:5432/CNMD'

db_ = SQLAlchemy(app)  # Já inicializa o SQLAlchemy aqui, não precisa do init_app

# Crie o engine do SQLAlchemy manualmente se precisar de um para a sessão
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

blueprint = Blueprint('api', __name__, url_prefix='/api')

main = Blueprint('main', __name__)

@app.route('/')  
def homepage():
    users = User.query.all()
    return render_template('index.html', users=users)

    # for user in users:
    #     print(user.username)
    # return render_template("index.html")

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
    db_.session.add(new_user)
    db_.session.commit()

    return jsonify(message='Usuário '+username+' criado com sucesso!', created=1)

# Rota para deletar um usuário
@blueprint.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']
    if current_user.username == username:
        return jsonify(message='Voce não pode deletar o usuário atual', deleted=0)
    else:
        user = User.query.filter_by(username=username).first()
        
        db_.session.delete(user)
        db_.session.commit()

        return jsonify(message='Usuário '+username+' deletado com sucesso!', deleted=1)

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)