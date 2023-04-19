from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, SubmitField,SelectField,DateField
from wtforms.validators import InputRequired, Email

class ProfileEditForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    date_of_birth = DateField('Date of Birth', validators=[InputRequired()], format='%Y-%m-%d')
    submit = SubmitField('Register')