from pprint import pprint
from app.models import User, ActivitiesTable, WeatherTable, IconsTable, ImageTable, ChosenActivitiesTable, CityTable, ChosenActivitiesTableHistory, WeatherTableHistory

def weather_table_dict():
    weather_table_dict = {}
    weather_history = WeatherTable.query.all()
    for idx in weather_history:
        weather_table_dict.update({
            idx.weather_date.strftime("%Y:%m:%d"): { 
                'weather_id': idx.id,
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
    return weather_table_dict


def weather_table_history_dict():
    weather_table_history_dict = {}
    weather_history = WeatherTableHistory.query.all()
    for idx in weather_history:
        weather_table_history_dict.update({
            idx.weather_date.strftime("%Y:%m:%d"): { 
                'weather_id': idx.id,
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
    return weather_table_history_dict
    
    
def activities_table_dict():
    activities_table_dict = {}
    activities = ActivitiesTable.query.all()
    for idx in activities:
        activities_table_dict.update({
            idx.activity_name: { 
                'activity_id': idx.id,
                'activity_description': idx.activity_description,
                'activity_todo_list': idx.activity_todo_list,
                'activity_conditions_temp': idx.activity_conditions_temp,
                'activity_conditions_1': idx.activity_conditions_1,
                'activity_conditions_2': idx.activity_conditions_2,
                'activity_conditions_3': idx.activity_conditions_3,
                'activity_conditions_4': idx.activity_conditions_4,'activity_conditions_5': idx.activity_conditions_5,
                'activity_conditions_6': idx.activity_conditions_6,
                'activity_conditions_7': idx.activity_conditions_7,
                'activity_conditions_8': idx.activity_conditions_8,
                'activity_conditions_9': idx.activity_conditions_9,
                'activity_calories': idx.activity_calories,
                'activity_level1': idx.activity_level1,
                'activity_level2': idx.activity_level2,
                'activity_level3': idx.activity_level3,
                'activity_timestamp': idx.activity_timestamp,
                'activity_user_id': idx.activity_user_id,
                'activity_conditions_1_icon': idx.activity_conditions_1_icon,'activity_conditions_2_icon': idx.activity_conditions_2_icon,
                'activity_conditions_3_icon': idx.activity_conditions_3_icon,
                'activity_conditions_4_icon': idx.activity_conditions_4_icon,
                'activity_conditions_5_icon': idx.activity_conditions_5_icon,
                'activity_conditions_6_icon': idx.activity_conditions_6_icon,
                'activity_conditions_7_icon': idx.activity_conditions_7_icon,
                'activity_conditions_8_icon': idx.activity_conditions_8_icon,
                'activity_conditions_9_icon': idx.activity_conditions_9_icon,
                'activity_chosen_status': idx.chosen_status,
                }
        }) 
    return activities_table_dict
    

def image_table_dict():
    image_table_dict = {}
    images = ImageTable.query.all()
    for idx in images:
        image_table_dict.update({
            idx.image_user: { 
                'image_id': idx.id,
                'image_user': idx.image_user,
                'image_user_id': idx.image_user_id,
                'image_date': idx.image_date,
                'image_name': idx.image_name,
                'image_description': idx.image_description,
                'image_link': idx.image_link,
                }
        })
    return image_table_dict

def icons_table_dict():
    icons_table_dict = {}
    icons = IconsTable.query.all()
    for idx in icons:
        icons_table_dict.update({
            idx.icon_name: { 
                'icon_id': idx.id,
                'icon_name': idx.icon_name,
                'icon_value': idx.icon_value,
                'icon_link': idx.icon_link,
                }
        })
    return icons_table_dict

def city_table_dict():
    city_table_dict = {}
    cities = CityTable.query.all()
    for idx in cities:
        city_table_dict.update({
            idx.city_name: { 
                'city_id': idx.id,
                'city_name': idx.city_name,
                'city_timestamp': idx.city_timestamp,
                }
        })
    return city_table_dict


def chosen_activities_table_history_dict():
    chosen_activities_table_history_dict = {}
    activities = ChosenActivitiesTableHistory.query.all()
    for idx in activities:
        chosen_activities_table_history_dict.update({
            idx.id: { 
                'chosen_activity_id': idx.id,
                'chosen_activity_name': idx.chosen_activity_name,
                'chosen__activity_status': idx.chosen_status,
                'chosen_activity_timestamp': idx.chosen_activity_timestamp
                }
        })
    return chosen_activities_table_history_dict


def chosen_activities_table_dict():
    chosen_activities_table_dict = {}
    activities = ChosenActivitiesTable.query.all()
    for idx in activities:
        chosen_activities_table_dict.update({
            idx.id: { 
                'chosen_activity_id': idx.id,
                'chosen_activity_name': idx.chosen_activity_name,
                'chosen__activity_status': idx.chosen_status,
                'chosen_activity_timestamp': idx.chosen_activity_timestamp
                }
        })
    return chosen_activities_table_dict
