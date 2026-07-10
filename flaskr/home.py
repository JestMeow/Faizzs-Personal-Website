from flask import (
    Blueprint, render_template, url_for
)

app = Blueprint(
    'app',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@app.route('/')
def home():
    return render_template('index.html')

