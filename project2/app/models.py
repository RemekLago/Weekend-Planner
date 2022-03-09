from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(100))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class ActivitiesTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(500), nullable=False)
    activity_description = db.Column(db.String(500), nullable=False)
    activity_todo_list = db.Column(db.String(500), nullable=False)
    activity_conditions = db.Column(db.String, nullable=False)
    activity_calories = db.Column(db.String(100))
    activity_favorite = db.Column(db.String(100))
    activity_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    activity_user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return '<activities {}>'.format(self.activity_name)

class WeatherTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_date = db.Column(db.DateTime)
    weather_day = db.Column(db.String(100))
    weather_temperature = db.Column(db.Integer)
    weather_wind = db.Column(db.Integer)
    weather_cloud = db.Column(db.Integer)
    weather_description = db.Column(db.String(500))
    weather_icon = db.Column(db.String(100))

    def __repr__(self):
        return '<wetaher {}>'.format(self.weather)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))