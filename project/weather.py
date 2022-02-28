from pprint import pprint
import requests
import keys

"""https://openweathermap.org/forecast5"""

APIkey = keys.APIkey
cnt = 16
city = "Warsaw"
country_code = "48"
limit = 1
units = "metric"

coordinats_to_cityname = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&limit={limit}&appid={APIkey}")
pprint(coordinats_to_cityname.json())

city_name = coordinats_to_cityname("name")
lat = coordinats_to_cityname("lat")
lon = coordinats_to_cityname("lon")
cnt = 2
weather_download = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&cnt={cnt}&appid={APIkey}")

pprint(weather_download.json())

weather_data = weather_download("list")
# weather_temperature = weather_data[0]("main")
# weather_description = weather_data("weather")
# weather_clouds = weather_data("clouds")
# weather_wind = weather_data("wind")
# weather_rain = weather_data("rain")
