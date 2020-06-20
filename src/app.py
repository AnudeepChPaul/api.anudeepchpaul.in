from flask import Flask, Blueprint
from flask_cors import CORS
import src.controllers as controllers

app = Flask(__name__)

CORS(app)

controllers.initiate_routes(app)
