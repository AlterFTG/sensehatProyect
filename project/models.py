from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # Las primary keys son obligatorias en SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
class draws(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Las primary keys son obligatorias en SQLAlchemy
    code = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
