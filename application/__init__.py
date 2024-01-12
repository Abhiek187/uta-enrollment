from flask import Flask
from config import Config
from mongoengine import connect
from flask_restx import Api

api = Api()

app = Flask(__name__)
app.config.from_object(Config)

connect("UTA_Enrollment")
api.init_app(app)

from application import routes
