from flask import Blueprint

signup_bp = Blueprint('signup',__name__, template_folder='templates')

from app.signup import signup  #signup routes exposed here
