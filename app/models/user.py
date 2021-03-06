from app import db 
from datetime import datetime
# from werkzeug import generate_password_hash, check_password_hash

class Users(db.Model):
    user_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(250), nullable=False)
    user_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)# index untuk pencarian berdasarkan email, seperti login
    password = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(50), unique=False, nullable=True)
    address = db.Column(db.String(500), unique=False, nullable=True)
    category = db.Column(db.String(10), unique=False, nullable=True)
    
    gender = db.Column(db.String(10), unique=False, nullable=True)
    age = db.Column(db.String(4), unique=False, nullable=True)
    month = db.Column(db.String(10), unique=False, nullable=True)
    day = db.Column(db.String(40), unique=False, nullable=True)
    year = db.Column(db.String(10), unique=False, nullable=True)
    date = db.Column(db.String(40), unique=False, nullable=True)

    Status =  db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    
    
    
    # def set_password(self, raw_password):
    #     self.password_hash = generate_password_hash(raw_password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

