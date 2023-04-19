from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, SubmitField,SelectField,DateField,TextAreaField,DateTimeLocalField
from wtforms.validators import InputRequired, Email

class ProfileEditForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    address=StringField('Address', validators=[InputRequired()])
    bio = TextAreaField('Bio', validators=[InputRequired()])
    speciality = StringField('Speciality', validators=[InputRequired()])
    submit = SubmitField('Register')

class AppointmentForm(FlaskForm):
    timestamp=DateTimeLocalField('Appointment Date and Time',validators=[InputRequired()],format='%Y-%m-%dT%H:%M')