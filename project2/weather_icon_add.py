from pprint import pprint
from app import db
from app.models import IconsTable

def adding_icon_weather_to_base():
    icons = IconsTable(
        icon_01d = "http://openweathermap.org/img/wn/01d@2x.png",
        icon_02d = "http://openweathermap.org/img/wn/02d@2x.png",
        icon_03d = "http://openweathermap.org/img/wn/03d@2x.png",
        icon_04d = "http://openweathermap.org/img/wn/04d@2x.png",
        icon_09d = "http://openweathermap.org/img/wn/09d@2x.png",
        icon_10d = "http://openweathermap.org/img/wn/10d@2x.png",
        icon_11d = "http://openweathermap.org/img/wn/12d@2x.png",
        icon_13d = "http://openweathermap.org/img/wn/13d@2x.png",
        icon_50d = "http://openweathermap.org/img/wn/50d@2x.png"
        )
    db.session.add(icons)  
    db.session.commit()

adding_icon_weather_to_base()