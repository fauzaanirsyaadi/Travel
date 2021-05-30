from app import db 
from datetime import datetime

class Drivers(db.Model):
    driver_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    driver_name = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(50), unique=False, nullable=True)
    
    bus_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    Status =  db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    
    def __repr__(self):
        return f'Quotes<{self.driver_name}>'
        
