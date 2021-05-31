#ini adalah file pertama yang akan dibaca
from flask import Flask
from config import Config
# from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate# MigrateCommand

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'super secret string' 


db = SQLAlchemy(app)
migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)

from app.routes.user_route import user
app.register_blueprint(user, url_prefix='/user')

# models
# from app.models.bus import Buses
# from app.models.driver import Drivers
# from app.models.payment import Payments
# from app.models.reservation import Reservations
# from app.models.schedule import Schedules
# from app.models.transaction_report import Transaction_Reports
# from app.models.user import Users

from app.models import bus, driver, payment, reservation, schedule, transaction_report, user 

if __name__=='__main__':
  app.run(debug=True)
