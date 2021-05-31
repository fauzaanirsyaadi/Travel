from app import db 
from datetime import datetime
from app.models.user import Users
from app.models.bus import Buses
from app.models.driver import Drivers

class Schedules(db.Model):
    schedule_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    destination = db.Column(db.String(500), unique=False, nullable=True)
    starting_point = db.Column(db.String(500), unique=False, nullable=True)
    departure_time = db.Column(db.Date, nullable=False)
    estimated_arrival_time = db.Column(db.Date, nullable=False)
    schedule_date = db.Column(db.Date, nullable=False)
    remarks = db.Column(db.String(500), unique=False, nullable=True)#catatan
    fare_amount = db.Column(db.String(25), unique=False, nullable=True)#total
    
    user_id = db.Column(db.Integer, db.ForeignKey(Users.user_id))
    driver_id = db.Column(db.Integer, db.ForeignKey(Drivers.driver_id))
    bus_id = db.Column(db.Integer, db.ForeignKey(Buses.bus_id))
    # user_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # driver_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # bus_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    