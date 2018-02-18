from flask import Flask,render_template
from jobplus.config import configs
from jobplus.models import db

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)


    return app
