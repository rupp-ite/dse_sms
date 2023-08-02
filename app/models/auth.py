from app import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100), unique=True, nullable=False)
    sub_menu = db.relationship('SubMenu', backref='menu', lazy=True)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)

class SubMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    name_latin = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)