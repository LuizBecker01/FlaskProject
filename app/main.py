from flask import Flask, make_response, jasonify, request
from flask import render_template
from flask import url_for

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  #não ordenar as chaves do em ordem alfabetica

@app.route('/')  
def homepage():     
    return render_template ("index.html")

# @app.route('/filmes', methods=['GET'])
# def get_filmes():
#      return make_response(
#          jasonify(filmes)
#      )

@app.route('/login', methods=['POST'])
def create_login():
    login = request.json
    return make_response(
        jasonify(login)
    ) 

if __name__ == "__main__":
    app.run()