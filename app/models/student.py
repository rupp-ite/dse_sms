from app import db

class Student(db.Model):
    __tablename__='student'
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(100),nullable = False)
    last_name = db.Column(db.String(100),nullable = False)
    gender_id = db.Column(db.Integer,db.ForeignKey('gender.id'),nullable = False)
    student_card = db.relationship('StudentCard',backref='student',lazy=True,uselist=False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    age = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    def __repr__(self):
        return f'Student ({self.id},{self.first_name},{self.last_name},{self.email},{self.age})'

class Gender(db.Model):
    __tablename__='gender'
    id = db.Column(db.Integer, primary_key = True)
    name_latin = db.Column(db.String(10),nullable = False)
    acronym = db.Column(db.String(4),nullable = False)
    student = db.relationship('Student',backref='gender',lazy=True)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    def __repr__(self):
        return f'Gender ({self.id},{self.name_latin},{self.acronym})'

class StudentCard(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    card_number = db.Column(db.String(20),unique = True,nullable=False)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'),nullable=False)
    issued_date = db.Column(db.Date,nullable = False)
    expired_date = db.Column(db.Date,nullable = False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    def __repr__(self):
        return f'StudentCard ({self.id},{self.card_number},{self.issued_date},{self.expired_date})'