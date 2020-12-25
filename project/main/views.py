from flask import Blueprint


main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/')
def main():
    return "main page"
