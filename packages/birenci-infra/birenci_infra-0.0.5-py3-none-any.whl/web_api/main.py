from flask import Flask
from flask_cors import CORS

from .config import Conf
from .exception import register_error_handler
from .models.JenkinsResult import db as mongo
from .routers import register_router

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["JSON_AS_ASCII"] = False


app.config.update(Conf.mongo_engine)
mongo.init_app(app)
register_router(app)
register_error_handler(app)
