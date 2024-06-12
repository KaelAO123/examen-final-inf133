from werkzeug.security import generate_password_hash
from app.database import db
import json
from flask_login import UserMixin
class User(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(40),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    phone = db.Column(db.String(50),nullable = False)
    role = db.Column(db.String(50),nullable = False)

    def __init__(self,name,email,password,phone,role=[]):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone
        self.role = json.dumps(role)
    
    @staticmethod
    def find_user(email):
        return User.query.filter_by(email=email).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()