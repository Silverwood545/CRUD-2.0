from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(150))
    projectname = db.Column(db.String(150))
    manager = db.Column(db.String(150))
    startdate = db.Column(db.String)
    enddate = db.Column(db.String)
    
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectname = db.Column(db.String(150))
    membername = db.Column(db.String(150))
    role = db.Column(db.String(150))
    startdate = db.Column(db.String)
    enddate = db.Column(db.String)





