from app import db 
from datetime import datetime

class Schedules(db.Model):
    schedule_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    destination = db.Column(db.String(500), unique=False, nullable=True)
    starting_point = db.Column(db.String(500), unique=False, nullable=True)
    departure_time = db.Column(db.Date, nullable=False)
    estimated_arrival_time = db.Column(db.Date, nullable=False)
    schedule_date = db.Column(db.Date, nullable=False)
    remarks = db.Column(db.String(500), unique=False, nullable=True)#catatan
    fare_amount = db.Column(db.String(25), unique=False, nullable=True)#total
    
    user_id = db.Column(db.Integer, foreign_key=True, nullable=True)
    driver_id = db.Column(db.Integer, foreign_key=True, nullable=True)
    bus_id = db.Column(db.Integer, foreign_key=True, nullable=True)
    