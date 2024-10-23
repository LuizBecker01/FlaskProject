from flask import Flask, jsonify, request, render_template, Blueprint 
from app import db
from app.models import User

main = Blueprint('main', __name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')


# Rota principal
@main.route('/')

app = Flask(__name__)

# Define a URI de conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2404@localhost:5432/CNMD'

db_ = SQLAlchemy(app)

# Crie o engine do SQLAlchemy manualmente se precisar de um para a sessão
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

@app.route('/')  
>>>>>>> Stashed changes
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

# Rota para login
@blueprint.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return jsonify(message='Login bem-sucedido!', logged=1)
    else:
        return jsonify(message='Credenciais inválidas!', logged=0)

# Rota para criar um novo usuário
@blueprint.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
<<<<<<< Updated upstream

=======
    
    
    
>>>>>>> Stashed changes
    # Verifica se o usuário já existe
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(message='Usuário já existe!', created=0)

    new_user = User(username=username, email=email, password=password)

    # Adiciona o novo usuário ao banco de dados
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='Usuário criado com sucesso!', created=1)

# Registra os blueprints
def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(blueprint)