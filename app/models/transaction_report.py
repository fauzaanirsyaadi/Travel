from app import db 
from datetime import datetime

class Transaction_Report(db.Model):
    report_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    report_date = db.Column(db.Date, nullable=False)
    note = db.Column(db.String(500), nullable=False)
    Status =  db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    
    user_id = db.Column(db.Integer, foreign_key=True)
    reservation_id = db.Column(db.Integer, foreign_key=True)
    payment_id = db.Column(db.Integer, foreign_key=True)
