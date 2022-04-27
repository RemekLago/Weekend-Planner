from pprint import pprint
import requests
from management.keys import APIkey
from datetime import datetime
from app import db
from app.models import WeatherTable, WeatherTableHistory, CityTable

"""links to weather API and libray with icons:
https://openweathermap.org/forecast5
https://openweathermap.org/api/one-call-api
https://libraries.io/npm/weathericons
https://rapidapi.com/wettercom-wettercom-default/api/forecast9/"""

def take_city_name(one_city):
    """ taking a city name from table, this city name was added by user in prosess of updating profile"""
    city_list = []
    # """take city name from list of city names"""
    # with open ("city_names.txt") as file:
    #     for row in file:
    #         city_list.append(row.strip())
    # cities = CityTable.query.all()
    # for city in cities:
    city_list.append(one_city)
    return city_list

def take_coordinates_of_city(city):
    """take geographic coordinates to find a city name"""
    limit = 1
    coordinates_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={APIkey}"
    coordinates_city_link = coordinates_city
    city = city
    coordinats_to_cityname = requests.get(coordinates_city_link)
    lat = coordinats_to_cityname.json()[0].get("lat")
    lon = coordinats_to_cityname.json()[0].get("lon")

    return lat,lon, city


def take_forecast_for_city(city):
    """take geographic coordinates to find a city and take parameters from the link"""
    coordinates = take_coordinates_of_city(city)
    lat = coordinates[0]
    lon = coordinates[1]
    city = coordinates[2]
    units = "metric"
    part = "current,minutely,hourly,alerts"

    weather_download = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={units}&exclude={part}&appid={APIkey}"
    weather_download_link = weather_download
    weather_data = (requests.get(weather_download_link)).json()

    return weather_data, city


def create_dict_with_weather(city):
    """create dictionary with weather conditions for futer export to base, taking: temperature, weather descriptions, level of clouds, level of wind, level of raining - for 8 day forecast"""
    weather_data = take_forecast_for_city(city)[0]
    city = take_forecast_for_city(city)[1]
    list_with_weather_day_dict = []
    dict_weekday_name = {
        "0": "Monday",
        "1": "Tuesday",
        "2": "Wednesday",
        "3": "Thursday",
        "4": "Friday",
        "5": "Saturday",
        "6": "Sunday"
        }
    for idx in range (8):
        weather_day_dict = {}
        weather_day_dict["id"] = idx 
        timestamp1 = datetime.fromtimestamp(weather_data["daily"][idx]["dt"])
        weather_day_dict["weather_date"] = datetime.fromtimestamp(weather_data["daily"][idx]["dt"])
        weather_day_dict["weather_day"] = timestamp1.weekday()
        day_number = int(timestamp1.weekday())
        weather_day_dict["weather_day_name"] = dict_weekday_name.get(f"{day_number}")
        weather_day_dict["weather_temperature"] = weather_data["daily"][idx]["temp"]["day"]
        weather_day_dict["weather_wind"] = weather_data["daily"][idx]["wind_speed"]
        weather_day_dict["weather_cloud"] = weather_data["daily"][idx]["pop"]
        weather_day_dict["weather_description"] = weather_data["daily"][idx]["weather"][0]["description"]
        weather_day_dict["weather_icon"] = weather_data["daily"][idx]["weather"][0]["icon"]
        weather_day_dict["weather_location"] = city
        weather_day_dict["weather_main"] = weather_data["daily"][idx]["weather"][0]["main"]
        list_with_weather_day_dict.append(weather_day_dict)
    
    return list_with_weather_day_dict
    

def adding_weather_to_base(city):
    """take list with parameters and add to data base"""
    input_data = create_dict_with_weather(city)
    
    for idx in input_data:
        weather = WeatherTable(
            weather_date = idx["weather_date"],
            weather_day = idx["weather_day"],
            weather_day_name = idx["weather_day_name"],
            weather_temperature = idx["weather_temperature"],
            weather_wind = idx["weather_wind"],
            weather_cloud  = idx["weather_cloud"],
            weather_description = idx["weather_description"],
            weather_icon = idx["weather_icon"],
            weather_location = idx["weather_location"],
            weather_main = idx["weather_main"]
            )
        db.session.add(weather)  
        db.session.commit()

def adding_weather_to_base_history(city):
    """take list with parameters and add to data base"""
    input_data = create_dict_with_weather(city)
    
    for idx in input_data:
        if idx["weather_date"] != WeatherTableHistory.weather_date:
            weather = WeatherTableHistory(
                weather_date = idx["weather_date"],
                weather_day = idx["weather_day"],
                weather_day_name = idx["weather_day_name"],
                weather_temperature = idx["weather_temperature"],
                weather_wind = idx["weather_wind"],
                weather_cloud  = idx["weather_cloud"],
                weather_description = idx["weather_description"],
                weather_icon = idx["weather_icon"],
                weather_location = idx["weather_location"],
                weather_main = idx["weather_main"]
                )
            db.session.add(weather)  
            db.session.commit()

def adding_data_for_all_cities(one_city):
    """take list of cieties and add to data base """
    # db.session.query(WeatherTable).delete()
    # db.session.commit()
    cities = take_city_name(one_city)
    for idx in cities:
        take_coordinates_of_city(idx)
        adding_weather_to_base(idx)
        adding_weather_to_base_history(idx)
