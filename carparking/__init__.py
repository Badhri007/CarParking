from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='abcdefghijklmnop'
app.config['TEMPLATES_AUTO_RELOAD'] = True

from carparking import routes