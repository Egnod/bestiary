from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sse import sse

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.register_blueprint(sse, url_prefix="/sse")

from app.mixin import IdModel

db = SQLAlchemy(app, model_class=IdModel)
migrate = Migrate(app, db)

CORS(app)

from app.models import *

if __name__ == '__main__':
    app.run()
