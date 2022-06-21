import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

#template_dir = os.path.abspath('templates')

app = Flask(__name__)#template_folder=template_dir

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://clientes:VQo4OLI1r1li04GS@localhost/cliente'
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
db = SQLAlchemy(app)