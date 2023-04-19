from flask import render_template, flash, redirect, url_for,request,g
from flask_login import current_user,login_required
from app import app,db

from functools import wraps

def login_required_patient(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated  or current_user.user_type=='professional':
            flash('You must be logged in to access this page')
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def login_required_professional(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated  or current_user.user_type=='patient':
            flash('You do not have permission for this action')
            return redirect(url_for('index', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')