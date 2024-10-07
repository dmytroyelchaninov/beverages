from backend import db, bcrypt
from flask_login import UserMixin
from backend.models.invoice import Invoice
import enum

class UserLevel(enum.Enum):
    non_verified = 'non-verified'
    verified = 'verified'
    admin = 'admin'

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    is_confirmed = db.Column(db.Boolean, default=False)
    user_level = db.Column(db.Enum(UserLevel), nullable=False, default=UserLevel.non_verified)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    additional_info = db.Column(db.Text)
    license = db.Column(db.String(255), nullable=True)


    invoices = db.relationship('Invoice', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.id} - {self.name} - {self.email}>'