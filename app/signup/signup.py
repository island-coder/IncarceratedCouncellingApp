from app.signup import signup_bp
from app.signup.forms import RegistrationForm,RegistrationFormInmate
from flask import render_template,redirect,url_for,flash,request
from flask_login import current_user, login_user,logout_user,login_required
from app import db
from app.models import Inmate,Professional,Institute

@signup_bp.route('/join')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('signup.html')

@signup_bp.route('/join/patient',methods=['GET','POST'])
def signup_inmate():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationFormInmate()
    institute_list = [(i.id, i.title) for i in Institute.query.all()]
    form.institution.choices=institute_list
    if form.validate_on_submit():
        user = Inmate(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        institute=Institute.query.filter_by(id=form.institution.data).first()
        user.parent_institute=institute
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('signup_inmate.html', title='Join Us', form=form)

@signup_bp.route('/join/professional',methods=['GET','POST'])
def signup_professional():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Professional(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered service provider!')
        return redirect(url_for('auth.login'))
    return render_template('signup_professional.html', title='Join Us', form=form)
