from flask import Flask
from sqlalchemy import schema
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = schema(app)


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    views = db.Column(db.Integer)
    name = db.Column(db.String(120), unique=True)
    size = db.Column(db.Integer)

    def __init__(self, views, name, size, pub_date=None):
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.views = views
        self.name = name
        self.size = size

    def __repr__(self):
        return '<User %r>' % self.name
