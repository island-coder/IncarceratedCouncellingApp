from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class Institute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(64), index=True, nullable=False,unique=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.utcnow)
    inmates = db.relationship('Inmate', backref='parent_institute', lazy='dynamic')

    def __repr__(self):
        return '<Institute {}>'.format(self.title)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False,unique=True)
    email = db.Column(db.String(100), index=True, nullable=False,unique=True)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.utcnow)

    __mapper_args__ = {
        'polymorphic_on': user_type,
        'polymorphic_identity': 'user'
    }

    def __repr__(self):
        return f"<User {self.id}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Inmate(User):
    __tablename__ = 'inmate'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    institute = db.Column(db.Integer, db.ForeignKey('institute.id'))
    date_of_birth=db.Column(db.DateTime)
    medical_history=db.Column(db.String(500))
    appointments = db.relationship('Appointment', backref='consulting_patient', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'inmate'
    }

    def __repr__(self):
        return f"<Inmate {self.id}>"


class Professional(User):
    __tablename__ = 'professional'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    bio = db.Column(db.String(150))
    address = db.Column(db.String(150))
    speciality = db.Column(db.String(64))
    reviews= db.relationship('Review',backref='reviewed_professional',lazy='dynamic')
    appointments=db.relationship('Appointment',backref='consulting_professional',lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'professional'
    }

    def __repr__(self):
        return f"<Professional {self.id}>"

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content= db.Column(db.String(200),nullable=False)
    reviewer= db.Column(db.String(50))
    professional=db.Column(db.Integer,db.ForeignKey('professional.id'))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    professional=db.Column(db.Integer,db.ForeignKey('professional.id'))
    patient = db.Column(db.Integer, db.ForeignKey('inmate.id'))
    is_available=db.Column(db.String(10),default='True')