from flask import (
    Blueprint, render_template, url_for
)

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@home.route('/')
def create_home():
    return render_template('index.html')

