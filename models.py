from . import db
from datetime import datetime

class Pushup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
