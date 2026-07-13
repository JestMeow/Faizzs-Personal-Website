from flask import Flask
from .home import home

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home)

    print("Static folder:", app.static_folder)
    print("Template folder:", app.template_folder)

    return app

app = create_app()
