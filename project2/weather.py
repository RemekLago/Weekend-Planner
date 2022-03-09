from genericpath import exists
from pprint import pprint
from sys import api_version
import requests
from keys import APIkey

APIkey = "1fcc3b7ebb293bbe3db4de3086b4d39c"

"""https://openweathermap.org/forecast5"""
"""https://libraries.io/npm/weathericons"""
"""https://rapidapi.com/wettercom-wettercom-default/api/forecast9/"""

"""take geographic coordinates to find a city in the next step"""
city = "Warsaw"
limit = 1
# coordinates_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=1fcc3b7ebb293bbe3db4de3086b4d39c"
coordinates_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={APIkey}"
coordinates_city_link = coordinates_city

coordinats_to_cityname = requests.get(coordinates_city_link)
# lat = coordinats_to_cityname.json()[0].get("lat")
# lon = coordinats_to_cityname.json()[0].get("lon")
lat= 52.2319581
lon= 21.0067249

"""take geographic coordinates to find a city and take parameters from the link"""
cnt = 8
units = "metric"
part = "current,minutely,hourly,alerts"
# weather_download = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&cnt={cnt}&appid={APIkey}"
weather_download = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units{units}&exclude={part}&appid={APIkey}"
weather_download_link = weather_download
# pprint(weather_download_link)
weather_data = (requests.get(weather_download_link)).json()
# pprint(weather_data)
# print(len(weather_data))
"""taking: temperature, weather descriptions, level of clouds, level of wind, level of raining - for 7 day forecast"""

def create_dict_with_weather():
    list_with_weather_day_dict = []
    for idx in range (8):
        weather_day_dict = {}
        weather_day_dict["id"] = idx 
        weather_day_dict["weather_date"] = weather_data["daily"][idx]["dt"]
        weather_day_dict["weather_day"] = idx
        weather_day_dict["weather_temperature"] = weather_data["daily"][idx]["temp"]["day"]
        weather_day_dict["weather_wind"] = weather_data["daily"][idx]["wind_speed"]
        weather_day_dict["weather_cloud"] = weather_data["daily"][idx]["clouds"]
        weather_day_dict["weather_cloud"] = weather_data["daily"][idx]["pop"]
        weather_day_dict["weather_description"] = weather_data["daily"][idx]["weather"][0]["description"]
        weather_day_dict["weather_icon"] = weather_data["daily"][idx]["weather"][0]["icon"]
        list_with_weather_day_dict.append(weather_day_dict)
    return list_with_weather_day_dict

a = create_dict_with_weather()

pprint(a)
