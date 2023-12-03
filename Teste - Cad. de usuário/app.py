from flask import Flask
from rotas import ConfigRotas, db

app = Flask(__name__)

@app.route("/")

def index():
    return "index"

ConfigRotas(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)