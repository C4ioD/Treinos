from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

caminho_banco_de_dados = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'comunidade.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + caminho_banco_de_dados
app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view =  'login'
login_manager.login_message_category = 'alert-info'

from projetoweb import routes
