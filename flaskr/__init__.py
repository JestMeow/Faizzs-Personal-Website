from flask import Flask
from .home import app

print("Static folder:", app.static_folder)
print("Template folder:", app.template_folder)


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(app)

    return flask_app
