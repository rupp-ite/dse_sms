from app import db

class Student(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(100),nullable = False)
    last_name = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    age = db.Column(db.Integer, nullable = False)
    create_at = db.Column(db.DateTime)
    create_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)