from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '59ced78434ad9766bd66ecdfb966f992'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #/// => specifies a relative path for the current file
# represent database structure as classes(models)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
