from pprint import pprint
from app import db
from app.models import IconsTable

def adding_icon_weather_to_base():
    dict_input_data = {
        "icon_01d": ["http://openweathermap.org/img/wn/01d@2x.png", "01d"],
        "icon_02d": ["http://openweathermap.org/img/wn/02d@2x.png", "02d"],
        "icon_03d": ["http://openweathermap.org/img/wn/03d@2x.png", "03d"],
        "icon_04d": ["http://openweathermap.org/img/wn/04d@2x.png", "04d"],
        "icon_09d": ["http://openweathermap.org/img/wn/09d@2x.png", "09d"],
        "icon_10d": ["http://openweathermap.org/img/wn/10d@2x.png","10d"],
        "icon_11d": ["http://openweathermap.org/img/wn/12d@2x.png","11d"],
        "icon_13d": ["http://openweathermap.org/img/wn/13d@2x.png","13d"],
        "icon_50d": ["http://openweathermap.org/img/wn/50d@2x.png","50d"]
        }
    for idx, idy in dict_input_data.items():
        icons = IconsTable(
            icon_name = idx,
            icon_value = idy[1],
            icon_link = idy[0],
        )
          
        #pprint(icons.icon_value) 
        db.session.add(icons)  
        db.session.commit()

adding_icon_weather_to_base()