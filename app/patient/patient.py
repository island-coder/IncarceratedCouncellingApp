from app import db
from app.models import Inmate,Appointment
from app.patient import patient_bp
from app.routes import login_required_patient
from app.patient.forms import ProfileEditForm
from flask import render_template,redirect,url_for,flash,request
from flask_login import current_user,login_required


@patient_bp.route('/profile')
@login_required_patient
def profile():
    patient=current_user
    return render_template('profile.html',patient=patient)

@patient_bp.route('/profile/edit',methods=['POST','GET'])
@login_required_patient
def edit_profile():
    user=current_user
    form=ProfileEditForm()
    if form.validate_on_submit():
        user.first_name=form.first_name.data
        user.last_name = form.last_name.data
        user.date_of_birth=form.date_of_birth.data
        db.session.commit()
        flash('Profile edited successfully!')
        return redirect(url_for('patient.profile'))
    form.first_name.data=user.first_name
    form.last_name.data=user.last_name
    form.date_of_birth.data=user.date_of_birth
    return render_template('edit_profile.html',form=form)

@patient_bp.route('/appointments/<user_id>')
@login_required_patient
def patient_appointments(user_id):
    if current_user != Inmate.query.filter_by(id=user_id).first():
        flash('You do not have permission for this action')
        return redirect(url_for('patient.profile'))
    patient=current_user
    return render_template('/patient_appointments.html',patient=patient)

@patient_bp.route('/appointments/book/<user_id>/<appointment_id>')
@login_required_patient
def book_patient_appointment(user_id,appointment_id):
    if current_user != Inmate.query.filter_by(id=user_id).first():
        flash('You do not have permission for this action')
        return redirect(url_for('patient.profile'))
    patient=current_user
    appointment=Appointment.query.filter_by(id=appointment_id).first()
    patient.appointments.add(appointment)
    db.session.commit()
    flash('Appointment added successfully')
    return redirect(url_for('patient.patient_appointments',user_id=user_id))