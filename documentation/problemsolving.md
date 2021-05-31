error message
  Can't validate argument 'foreign_key'; can't locate any SQLAlchemy dialect named 'foreign'
  ..
  ..
  [flask_migrate] Error: Can't locate revision identified by '51475b665d81'
solution
  change from this :
  user_id = db.Column(db.Integer, foreign_key=True, nullable=False)
  to this :
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
another solution 
  from app.models.driver import Drivers
  ...
  ...
  driver_id = db.Column(db.Integer, db.ForeignKey(Drivers.driver_id), nullable=False)

error message
  ERROR [flask_migrate] Error: Can't locate revision identified by '51475b665d81'
solution
  delete from alembic_version;
  (in sql shell)