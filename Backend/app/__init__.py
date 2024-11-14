#(initializes Flask app and extensions)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

# Todo: Inialize the extensions
db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()

def create_app():
    #Todo: Initailize Flask app
    app = Flask(__name__)
    
    ##* Load configurations from environment variables or config files
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'myssecret')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'myjwtsecret')
    
    #Todo: Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    
    return app