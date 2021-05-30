from app import db 
from datetime import datetime

class Buses(db.Model):
    bus_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    bus_name = db.Column(db.String(50), unique=False, nullable=True)
    bus_number = db.Column(db.BigInteger, unique=False, nullable=True)
    plate_number = db.Column(db.BigInteger, unique=False, nullable=True)
    type = db.Column(db.String(10), unique=False, nullable=True)
    capacity = db.Column(db.BigInteger, unique=False, nullable=True)
    
    Status =  db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    driver_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    
    def __repr__(self):
        return f'Quotes<{self.bus_name}>'
        
