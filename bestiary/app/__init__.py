from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sse import sse
from flask_graphql import GraphQLView
from flask_jwt import JWT
from flask_whooshee import Whooshee

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.register_blueprint(sse, url_prefix="/sse")

from bestiary.app.mixin import IdModel

db = SQLAlchemy(app, model_class=IdModel)
migrate = Migrate(app, db)
whooshee = Whooshee(app)

CORS(app)

from bestiary.app.models import *
from bestiary.app.auth import authenticate, identity

jwt = JWT(app, authenticate, identity)

from bestiary.app.schema import schema

whooshee.reindex()

app.add_url_rule('/', view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))

if __name__ == '__main__':
    app.run(debug=True)
