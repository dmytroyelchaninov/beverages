from backend import db

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    subcategories = db.relationship('Subcategory', backref='category', lazy=True)

class Subcategory(db.Model):
    __tablename__ = 'subcategories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('subcategories.id'), nullable=True)
    children = db.relationship('Subcategory', lazy='joined', join_depth=3, backref=db.backref('parent', remote_side=[id]))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)