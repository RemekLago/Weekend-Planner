from pprint import pprint
from app import db
from app.models import ActivitiesTable
from datetime import datetime

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
    pprint(list_descriptions)
    return list_descriptions


def create_dict_with_descriptions():
    data = open_file()

    dict_with_descriptions = {}
    list_with_dict_description = []
    for idx in data:
        dict_with_descriptions["activite_name"] = idx[0]
        dict_with_descriptions["activite_description"] = idx[1]
        dict_with_descriptions["activite_todo_list"] = idx[2]
        # dict_with_descriptions["activite_conditions"] = idx[3]
        dict_with_descriptions["activite_calories"] = idx[4]
        dict_with_descriptions["activity_conditions_temp"] = idx[5]
        dict_with_descriptions["activity_conditions_1"] = idx[6]
        dict_with_descriptions["activity_conditions_2"] = idx[7]
        dict_with_descriptions["activity_conditions_3"] = idx[8]
        dict_with_descriptions["activity_conditions_4"] = idx[9]
        dict_with_descriptions["activity_conditions_5"] = idx[10]
        dict_with_descriptions["activity_conditions_6"] = idx[11]
        dict_with_descriptions["activity_conditions_7"] = idx[12]
        dict_with_descriptions["activity_conditions_8"] = idx[13]
        dict_with_descriptions["activity_conditions_9"] = idx[14]
        dict_with_descriptions["activity_user_id"] = idx[15]
        dict_with_descriptions["activity_favorite"] = False
        list_with_dict_description.append(dict_with_descriptions)
        dict_with_descriptions = {}
    pprint(list_with_dict_description)
    return list_with_dict_description

def adding_activities_to_base():
    input_data = create_dict_with_descriptions()
    today = datetime.today()
    # db.session.query(ActivitiesTable).delete()
    # db.session.commit()
    for idx in input_data:
        activity = ActivitiesTable(
            activity_name = idx["activite_name"],
            activity_description = idx["activite_description"],
            activity_todo_list = idx["activite_todo_list"],
            # activity_conditions = idx["activite_conditions"],
            activity_calories = idx["activite_calories"],
            activity_conditions_temp = idx["activity_conditions_temp"],
            activity_conditions_1 = idx["activity_conditions_1"],
            activity_conditions_2 = idx["activity_conditions_2"],
            activity_conditions_3 = idx["activity_conditions_3"],
            activity_conditions_4 = idx["activity_conditions_4"],
            activity_conditions_5 = idx["activity_conditions_5"],
            activity_conditions_6 = idx["activity_conditions_6"],
            activity_conditions_7 = idx["activity_conditions_7"],
            activity_conditions_8 = idx["activity_conditions_8"],
            activity_conditions_9 = idx["activity_conditions_9"],
            activity_user_id = idx["activity_user_id"],
            activity_favorite = idx["activity_favorite"],
            activity_timestamp = today
            )
        
        # print(activity.activity_conditions_4)
        db.session.add(activity)  
        db.session.commit()

    
adding_activities_to_base()
