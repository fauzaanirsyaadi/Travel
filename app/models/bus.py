from app import db
from datetime import datetime
from app.models.user import Users
from app.models.driver import Drivers

class Buses(db.Model):
    bus_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    bus_name = db.Column(db.String(50), unique=False, nullable=True)
    bus_number = db.Column(db.BigInteger, unique=False, nullable=True)
    plate_number = db.Column(db.BigInteger, unique=False, nullable=True)
    type = db.Column(db.String(10), unique=False, nullable=True)
    capacity = db.Column(db.BigInteger, unique=False, nullable=True)
    
    Status =  db.Column(db.Integer, nullable=False)

    # user_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # driver_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # kurang jelas

    user_id = db.Column(db.Integer, db.ForeignKey(Users.user_id))
    driver_id = db.Column(db.Integer, db.ForeignKey(Drivers.driver_id))
    # lebih
    
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    
    
        
