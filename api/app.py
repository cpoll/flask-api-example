from flask import Flask
from flask_restful import Api

from api.api.IndexAPI import IndexAPI

def configure_app(app):
    api = Api(app)
    api.add_resource(IndexAPI, '/')


APP = Flask(__name__)
configure_app(APP)
