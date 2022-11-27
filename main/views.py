from flask import Blueprint, render_template

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')