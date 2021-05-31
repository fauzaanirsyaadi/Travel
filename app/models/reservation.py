from app import db 
from datetime import datetime
from app.models.user import Users
from app.models.bus import Buses
from app.models.schedule import Schedules
class Reservations(db.Model):
    reservation_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    number_of_seat = db.Column(db.Integer, nullable=False)
    fare_amount = db.Column(db.String(500), unique=False, nullable=True)
    departure_time = db.Column(db.Date, nullable=False)
    destination = db.Column(db.String(500), unique=False, nullable=True)
    reservation_date = db.Column(db.Date, nullable=False)

    status = db.Column(db.Integer, nullable=False)
    # bus_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # user_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # schedule_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.user_id))
    bus_id = db.Column(db.Integer, db.ForeignKey(Buses.bus_id))
    schedule_id = db.Column(db.Integer, db.ForeignKey(Schedules.schedule_id))
    