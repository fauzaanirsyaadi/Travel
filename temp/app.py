from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/travel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'fauzaan'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Users(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), unique=False, nullable=True)
    lastname = db.Column(db.String(50), unique=False, nullable=True)
    email = db.Column(db.String(50), unique=False, nullable=True)
    phone = db.Column(db.String(50), unique=False, nullable=True)
    password = db.Column(db.String(50), unique=False, nullable=True)
    month = db.Column(db.String(10), unique=False, nullable=True)
    day = db.Column(db.String(40), unique=False, nullable=True)
    gender = db.Column(db.String(4), unique=False, nullable=True)
    year = db.Column(db.String(10), unique=False, nullable=True)
    date = db.Column(db.String(40), unique=False, nullable=True)
    admin = db.Column(db.LargeBinary, unique=False, nullable=True)


class Busesdata(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    busname = db.Column(db.String(50), unique=False, nullable=True)
    seats = db.Column(db.String(50), unique=False, nullable=True)
    ticket_per_seat = db.Column(db.String(50), unique=False, nullable=True)
    date = db.Column(db.String(50), unique=False, nullable=True)
    city = db.Column(db.String(50), unique=False, nullable=True)
    driver_name = db.Column(db.String(50), unique=False, nullable=True)
    driver_contact = db.Column(db.String(50), unique=False, nullable=True)
    type = db.Column(db.String(10), unique=False, nullable=True)
    day = db.Column(db.String(20), nullable=True)
    monday = db.Column(db.String(20), nullable=True)
    tuesday = db.Column(db.String(20), nullable=True)
    wednesday = db.Column(db.String(20), nullable=True)
    thursday = db.Column(db.String(20), nullable=True)
    friday = db.Column(db.String(20), nullable=True)
    saturday = db.Column(db.String(20), nullable=True)
    admin = db.Column(db.LargeBinary)
