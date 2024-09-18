from flask import Flask, make_response, jasonify, request
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')  
def homepage():     
    return render_template ("index.html")


if __name__ == "__main__":
    app.run()