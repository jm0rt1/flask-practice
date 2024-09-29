# fmt: off

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
# Construct the absolute path for the database file in the instance folder
basedir = os.path.abspath(os.path.dirname(__file__))
instance_dir = os.path.join(basedir, 'instance')
if not os.path.exists(instance_dir):
    os.makedirs(instance_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(instance_dir, "site.db")}'

db = SQLAlchemy(app)

from flask_app_1.routes import main
app.register_blueprint(main)
migrate = Migrate(app, db)
from flask_app_1 import models