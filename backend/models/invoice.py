from backend import db
from backend.models.user import User

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_details = db.Column(db.JSON, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    pdf_path = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Invoice {self.id} for User {self.user_id}>'