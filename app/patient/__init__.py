from flask import Blueprint

patient_bp = Blueprint('patient',__name__, template_folder='templates')

from app.patient import patient  #auth routes exposed here
