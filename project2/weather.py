from pprint import pprint
import requests
from keys import APIkey
from datetime import datetime
from app import db
from app.models import WeatherTable

APIkey = "1fcc3b7ebb293bbe3db4de3086b4d39c"

"""https://openweathermap.org/forecast5"""
"""https://openweathermap.org/api/one-call-api"""
"""https://libraries.io/npm/weathericons"""
"""https://rapidapi.com/wettercom-wettercom-default/api/forecast9/"""

"""take geographic coordinates to find a city in the next step"""
city = "Warsaw"
limit = 1
coordinates_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={APIkey}"
coordinates_city_link = coordinates_city

coordinats_to_cityname = requests.get(coordinates_city_link)
lat = coordinats_to_cityname.json()[0].get("lat")
lon = coordinats_to_cityname.json()[0].get("lon")

"""take geographic coordinates to find a city and take parameters from the link"""
units = "metric"
part = "current,minutely,hourly,alerts"

weather_download = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={units}&exclude={part}&appid={APIkey}"
weather_download_link = weather_download
weather_data = (requests.get(weather_download_link)).json()
#print(weather_download_link)

"""taking: temperature, weather descriptions, level of clouds, level of wind, level of raining - for 7 day forecast"""
def create_dict_with_weather():
    list_with_weather_day_dict = []
    dict_weekday_name = {
        "0": "Sunday",
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday"
    }
    for idx in range (8):
        weather_day_dict = {}
        weather_day_dict["id"] = idx 
        timestamp = str(datetime.fromtimestamp(weather_data["daily"][idx]["dt"]))
        timestamp1 = datetime.fromtimestamp(weather_data["daily"][idx]["dt"])
        timestamp2 = timestamp.rsplit(" ")[0]
        weather_day_dict["weather_date"] = timestamp2
        weather_day_dict["weather_day"] = timestamp1.weekday()
        day_number = int(timestamp1.weekday())
        weather_day_dict["weather_day_name"] = dict_weekday_name.get(f"{day_number}")
        weather_day_dict["weather_temperature"] = weather_data["daily"][idx]["temp"]["day"]
        weather_day_dict["weather_wind"] = weather_data["daily"][idx]["wind_speed"]
        weather_day_dict["weather_cloud"] = weather_data["daily"][idx]["pop"]
        weather_day_dict["weather_description"] = weather_data["daily"][idx]["weather"][0]["description"]
        weather_day_dict["weather_icon"] = weather_data["daily"][idx]["weather"][0]["icon"]
        list_with_weather_day_dict.append(weather_day_dict)
    #pprint(list_with_weather_day_dict) 
    return list_with_weather_day_dict
    
create_dict_with_weather()

def adding_weather_to_base():
    input_data = create_dict_with_weather()
    db.session.query(WeatherTable).delete()
    db.session.commit()
    for idx in input_data:
        weather = WeatherTable(
            weather_date = idx["weather_date"],
            weather_day = idx["weather_day"],
            weather_day_name = idx["weather_day_name"],
            weather_temperature = idx["weather_temperature"],
            weather_wind = idx["weather_wind"],
            weather_cloud  = idx["weather_cloud"],
            weather_description = idx["weather_description"],
            weather_icon = idx["weather_icon"]
            )
        db.session.add(weather)  
        db.session.commit()
        # print(weather.weather_day_name)
adding_weather_to_base()