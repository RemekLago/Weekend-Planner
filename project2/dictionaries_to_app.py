from pprint import pprint
from app.models import User, ActivitiesTable, WeatherTable, IconsTable, ImageTable, ChosenActivitiesTable, CityTable, ChosenActivitiesTableHistory, WeatherTableHistory

weather_table_dict = {}
weather = WeatherTableHistory.query.all()
for idx in weather:
    weather_table_dict.update({
        idx.id: { 
            'weather_date': idx.weather_date.strftime("%Y:%m:%d"),
            'weather_day': idx.weather_day,
            'weather_laction': idx.weather_location,
            'weather_day_name': idx.weather_day_name,
            'weather_temperature': idx.weather_temperature,
            'weather_wind': idx.weather_wind,
            'weather_cloud': idx.weather_cloud,
            'weather_description': idx.weather_description,
            'weather_icon': idx.weather_icon,
            'weather_main': idx.weather_main,
            }
    })
pprint(weather_table_dict)
