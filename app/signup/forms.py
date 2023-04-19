from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,DateTimeLocalField
from wtforms.validators import ValidationError, InputRequired, Email, EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    password2 = PasswordField(
    'Repeat Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
        raise ValidationError('Please use a different username.')

def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
        raise ValidationError('Please use a different email address.')

class RegistrationFormInmate(RegistrationForm):
    institution = SelectField('Institution', coerce=int)

# class RegistrationFormProfessional(RegistrationForm):




