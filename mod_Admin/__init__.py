from flask import Blueprint

Admin = Blueprint('Admin', __name__,url_prefix='/Admin/')

@Admin.route("/")
def Admin_index():
    return "hello bluprint"
