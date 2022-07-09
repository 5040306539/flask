# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from config import Development
#
# app = Flask(__name__)
#
# app.config.from_object(Development)
# db = SQLAlchemy(app)
#
#
# @app.route("/")
# def index():
#     print(app.config)
#     return "hello"
# ____________________________________________________________________________
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Blog home"