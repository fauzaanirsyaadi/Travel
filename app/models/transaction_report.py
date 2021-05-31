from app import db 
from datetime import datetime
from app.models.user import Users
from app.models.reservation import Reservations
from app.models.payment import Payments

class Transaction_Reports(db.Model):
    report_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    report_date = db.Column(db.Date, nullable=False)
    note = db.Column(db.String(500), nullable=False)
    Status =  db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    
    user_id = db.Column(db.Integer, db.ForeignKey(Users.user_id))
    reservation_id = db.Column(db.Integer, db.ForeignKey(Reservations.reservation_id))
    payment_id = db.Column(db.Integer, db.ForeignKey(Payments.payment_id))
    # user_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # reservation_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # payment_id = db.Column(db.Integer, foreign_key=True, nullable=False)
