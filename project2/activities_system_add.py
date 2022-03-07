from pprint import pprint
from app import db
from app.models import ActivityDescription

def open_file():
    temporary_list = []
    list_descriptions = []
    with open("activities_description.txt", "r") as file:
        for row in file:
            if row.strip() != "":
                temporary_list.append(row.strip())
            else:    
                list_descriptions.append(temporary_list)
                temporary_list = []
    return list_descriptions

def create_dict_with_descriptions():
    data = open_file()
    dict_with_descriptions = {}
    list_with_dict_description = []
    for idx in data:
        dict_with_descriptions["activite_name"] = idx[0]
        dict_with_descriptions["activite_description"] = idx[1]
        dict_with_descriptions["activite_todo_list"] = idx[2]
        dict_with_descriptions["activite_conditions"] = idx[3]
        dict_with_descriptions["activite_calories"] = idx[4]
        dict_with_descriptions["activite_favorite"] = idx[5]
        list_with_dict_description.append(dict_with_descriptions)
    # pprint(list_with_dict_description)
    return list_with_dict_description

def adding_activities_to_base():
    input_data = create_dict_with_descriptions()
    # pprint(input_data)
    for idx in input_data:
        activity = ActivityDescription(
            activity_name = idx["activite_name"],
            activity_description = idx["activite_description"],
            activity_todo_list = idx["activite_todo_list"],
            activity_conditions = idx["activite_conditions"],
            activity_calories = idx["activite_calories"],
            activity_favorite = idx["activite_favorite"]
            )
        print(activity.activity_name)
        # db.session.add(activity)  
        # db.session.commit()
    
adding_activities_to_base()
