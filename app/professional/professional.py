from app import db
from app.models import Professional,Appointment
from app.professional import professional_bp
from app.professional.forms import AppointmentForm
from app.routes import login_required_professional,login_required_patient,login_required
from app.professional.forms import ProfileEditForm
from flask import render_template,redirect,url_for,flash,request
from flask_login import current_user,login_required
import datetime

@professional_bp.route('/profile')
@login_required_professional
def profile():
    professional=current_user
    return render_template('/professional_profile.html',professional=professional)

@professional_bp.route('/profile/<user_id>')
def profile_public(user_id):
    professional=Professional.query.filter_by(id=user_id).first_or_404()
    return render_template('/professional_profile_public.html',professional=professional)

@professional_bp.route('/profile/edit',methods=['POST','GET'])
@login_required_professional
def edit_profile():
    user=current_user
    form=ProfileEditForm()
    if form.validate_on_submit():
        user.first_name=form.first_name.data
        user.last_name = form.last_name.data
        user.address=form.address.data
        user.bio=form.bio.data
        user.speciality=form.speciality.data
        # user.modified=datetime.datetime.utcnow
        db.session.commit()
        flash('Profile edited successfully!')
        return redirect(url_for('professional.profile'))
    form.first_name.data=user.first_name
    form.last_name.data=user.last_name
    form.address.data=user.address
    form.bio.data=user.bio
    form.speciality.data=user.speciality
    return render_template('/edit_professional_profile.html',form=form)

@professional_bp.route('/appointments/<user_id>')
@login_required
def professional_appointments(user_id):
    professional=Professional.query.filter_by(id=user_id).first_or_404()
    return render_template('/professional_appointments.html',professional=professional)

@professional_bp.route('/appointments/create/<user_id>',methods=['POST','GET'])
@login_required_professional
def create_appointment(user_id):
    professional = Professional.query.filter_by(id=user_id).first_or_404()
    if current_user != professional:
        flash('You do not have permission for this action')
        return redirect(url_for('professional.profile'))
    form= AppointmentForm()
    professional = current_user
    if form.validate_on_submit():
        appointment= Appointment()
        appointment.timestamp=form.timestamp.data
        professional.appointments.add(appointment)
        db.session.commit()
        flash('Appointment added successfully')
        return redirect(url_for('professional.professional_appointments',user_id=user_id))
    return render_template('create_appointment.html',professional=professional,form=form)

