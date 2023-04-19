from app import app, db
from app.models import Institute,User,Inmate,Professional,Appointment

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Institute':Institute, 'User':User,'Inmate':Inmate,'Professsional':Professional,'Appointment':Appointment}