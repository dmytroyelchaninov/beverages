from backend import db, bcrypt
from backend.models.user import User
from flask_mail import Message
from backend import mail
from security.auth import generate_confirmation_token

def create_user(data):
    user = User(
        name=data['name'],
        email=data['email'],
        phone_number=data['phone_number'],
        address=data['address'],
        user_level=data.get('user_level', 'non_verified')
    )
    
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def update_user(user, data):
    user.phone_number = data.get('phone_number', user.phone_number)
    user.address = data.get('address', user.address)
    db.session.commit()
    return user

def check_password(user, password):
    return bcrypt.check_password_hash(user.password_hash, password)

def send_confirmation_email(user):
    token = generate_confirmation_token(user.email)
    confirm_url = f'http://localhost:5000/api/users/confirm/{token}'
    
    msg = Message('Confirm your email', sender = 'dmytroyelchaninov@gmail.com', recipients = [user.email])
    msg.body = f'Click the link to confirm your email: {confirm_url}'
    mail.send(msg)
    