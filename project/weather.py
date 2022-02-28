from pprint import pprint
import requests
from keys import APIkey

"""https://openweathermap.org/forecast5"""

"""take geographic coordinates to find a city in the next step"""
city = "Warsaw"
limit = 1
coordinates_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={APIkey}"

coordinats_to_cityname = requests.get(coordinates_city)
lat = coordinats_to_cityname.json()[0].get("lat")
lon = coordinats_to_cityname.json()[0].get("lon")

"""take geographic coordinates to find a city and take parameters from the link"""
cnt = 8
units = "metric"
weather_download = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&cnt={cnt}&appid={APIkey}"
weather_city = requests.get(weather_download)


"""taking: temperature, weather descriptions, level of clouds, level of wind, level of raining"""
weather_data = weather_city.json().get("list")
"""1 day, data from 6am i 12am - it is the 5th sample from day """
weather_day = weather_data[4].get("dt_txt")
weather_temperature_min = weather_data[2].get("main").get("temp_min")
weather_temperature_max = weather_data[4].get("main").get("temp_max")
weather_description = weather_data[4].get("weather")[0].get("description")
weather_icon = weather_data[4].get("weather")[0].get("icon")
pprint(weather_day)
print(weather_temperature_max)
print(weather_temperature_min)
print(weather_description)
print(weather_icon)
