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
    about_me = db.Column(db.String(500))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(100))
    activity_level1 = db.Column(db.Boolean)
    activity_level2 = db.Column(db.Boolean)
    activity_level3 = db.Column(db.Boolean)

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
    activity_conditions_temp = db.Column(db.Integer, nullable=False)
    activity_conditions_1 = db.Column(db.Boolean)
    activity_conditions_2 = db.Column(db.Boolean)
    activity_conditions_3 = db.Column(db.Boolean)
    activity_conditions_4 = db.Column(db.Boolean)
    activity_conditions_5 = db.Column(db.Boolean)
    activity_conditions_6 = db.Column(db.Boolean)
    activity_conditions_7 = db.Column(db.Boolean)
    activity_conditions_8 = db.Column(db.Boolean)
    activity_conditions_9 = db.Column(db.Boolean)
    activity_calories = db.Column(db.String(100))
    activity_favourite = db.Column(db.Boolean)
    activity_level1 = db.Column(db.Boolean)
    activity_level2 = db.Column(db.Boolean)
    activity_level3 = db.Column(db.Boolean)
    activity_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    activity_user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    activity_conditions_1_icon = db.Column(db.String(100))
    activity_conditions_2_icon = db.Column(db.String(100))
    activity_conditions_3_icon = db.Column(db.String(100))
    activity_conditions_4_icon = db.Column(db.String(100))
    activity_conditions_5_icon = db.Column(db.String(100))
    activity_conditions_6_icon = db.Column(db.String(100))
    activity_conditions_7_icon = db.Column(db.String(100))
    activity_conditions_8_icon = db.Column(db.String(100))
    activity_conditions_9_icon = db.Column(db.String(100))
    chosen_status = db.Column(db.Boolean)

    def __repr__(self):
        return '<ActivitiesTable {}>'.format(self.activity_name)

class WeatherTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_date = db.Column(db.DateTime)
    weather_day = db.Column(db.String(100))
    weather_location = db.Column(db.String(100))
    weather_day_name = db.Column(db.String(100))
    weather_temperature = db.Column(db.Integer)
    weather_wind = db.Column(db.Integer)
    weather_cloud = db.Column(db.Integer)
    weather_description = db.Column(db.String(500))
    weather_icon = db.Column(db.String(100))
    weather_main = db.Column(db.String(300))
    weather_user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return '<WeatherTable {}>'.format(self.weather_icon)

class WeatherTableHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_date = db.Column(db.DateTime)
    weather_day = db.Column(db.String(100))
    weather_location = db.Column(db.String(100))
    weather_day_name = db.Column(db.String(100))
    weather_temperature = db.Column(db.Integer)
    weather_wind = db.Column(db.Integer)
    weather_cloud = db.Column(db.Integer)
    weather_description = db.Column(db.String(500))
    weather_icon = db.Column(db.String(100))
    weather_user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    weather_main = db.Column(db.String(300))

    def __repr__(self):
        return '<WeatherTable {}>'.format(self.weather_icon)        


class IconsTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    icon_name = db.Column(db.String(10))
    icon_value = db.Column(db.String(10))
    icon_link = db.Column(db.String(100))
    icon_value2 = db.Column(db.Boolean)
    icon_id = db.Column(db.Integer, db.ForeignKey("weather_table.weather_icon"))

    def __repr__(self):
        return '<IconsTable {}>'.format(self.icon_name)


class ImageTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_user = db.Column(db.String(100))
    image_user_id = db.Column(db.String(100))
    image_date = db.Column(db.DateTime)
    image_name = db.Column(db.String(100))
    image_description = db.Column(db.String(500))
    image_link = db.Column(db.String(200))

    def __repr__(self):
        return '<ImageTable {}>'.format(self.image_name)

class ChosenActivitiesTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chosen_activity_name = db.Column(db.String(500), nullable=False)
    chosen_status = db.Column(db.Boolean)
    chosen_activity_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<ChosenActivitiesTable {}>'.format(self.chosen_status)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class CityTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(500), nullable=False)
    city_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<CityTable {}>'.format(self.city_name)