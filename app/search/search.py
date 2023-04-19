from app import db
from app.models import Professional
from app.search import search_bp
from app.routes import login_required_professional,login_required_patient
from flask import render_template,redirect,url_for,flash,request
from flask_login import current_user

@search_bp.route('/professionals',methods=['GET','POST'])
def search_professionals():
    results=Professional.query.all()
    return render_template('search_professionals.html',results=results)