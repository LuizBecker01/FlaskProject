from flask import Flask, make_response
from flask import render_template
# from models import User

app = Flask(__name__)

@app.route('/')  
def homepage():
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(debug=True)