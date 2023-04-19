from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import LoginManager
from flask import Blueprint
# from flask_admin import Admin

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}



app = Flask(__name__)
app.config.from_object(Config)
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app,metadata=metadata)
migrate = Migrate(app, db, render_as_batch=True)


login = LoginManager(app)
login.login_view ='auth.login'

from app.auth import auth_bp  #registering flask blueprint for login
app.register_blueprint(auth_bp)

from app.signup import signup_bp
app.register_blueprint(signup_bp) #registering flask blueprint for auth

from app.patient import patient_bp
app.register_blueprint(patient_bp,url_prefix='/patient') #registering flask blueprint for auth

from app.professional import professional_bp
app.register_blueprint(professional_bp,url_prefix='/professional') #registering flask blueprint for professional

from app.search import search_bp
app.register_blueprint(search_bp) #registering flask blueprint for search


# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
# admin = Admin(app, name='admin_app', template_mode='bootstrap4')

from app import routes,models