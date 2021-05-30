from app import db 
from datetime import datetime

class Reservations(db.Model):
    reservation_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    number_of_seat = db.Column(db.Integer, nullable=False)
    fare_amount = db.Column(db.String(500), unique=False, nullable=True)
    departure_time = db.Column(db.Date, nullable=False)
    destination = db.Column(db.String(500), unique=False, nullable=True)
    reservation_date = db.Column(db.Date, nullable=False)

    status = db.Column(db.Integer, nullable=False)
    bus_id = db.Column(db.Integer, foreign_key=True, unique=True)
    user_id = db.Column(db.Integer, foreign_key=True, nullable=True)
    schedule_id = db.Column(db.Integer, foreign_key=True, nullable=True)
    