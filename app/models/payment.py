from app import db 
from datetime import datetime
from app.models.user import Users
from app.models.reservation import Reservations

class Payments(db.Model):
    payment_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow())
    amount_paid = db.Column(db.String(40), unique=False, nullable=True)
    
    # user_id = db.Column(db.BigInteger, foreign_key=True, autoincrement=True)
    # reservation_id = db.Column(db.BigInteger, foreign_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.user_id))
    reservation_id = db.Column(db.BigInteger, db.ForeignKey(Reservations.reservation_id))
        
