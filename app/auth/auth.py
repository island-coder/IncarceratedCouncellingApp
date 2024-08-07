from app.auth import auth_bp
from flask import render_template,redirect,url_for,flash,request
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from app.auth.forms import LoginForm
from app.models import User


# auth bp routes are defined
#routes accessed as auth.routename
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form= LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=login_form.remember.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',title='Sign In',form=login_form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))