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
    # pprint(list_descriptions)
    return list_descriptions


def create_dict_with_descriptions():
    data = open_file()

    dict_with_descriptions = {}
    list_with_dict_description = []
    for idx in data:
        dict_with_descriptions["activite_name"] = idx[0]
        dict_with_descriptions["activite_description"] = idx[1]
        dict_with_descriptions["activite_todo_list"] = idx[2]
        dict_with_descriptions["activite_calories"] = idx[4]
        dict_with_descriptions["activity_conditions_temp"] = int(idx[5])
        dict_with_descriptions["activity_conditions_1"] = 1 if idx[6].strip() == "True" else 0
        dict_with_descriptions["activity_conditions_2"] = 1 if idx[7].strip() == "True" else 0
        dict_with_descriptions["activity_conditions_3"] = 1 if idx[8].strip() == "True" else 0
        dict_with_descriptions["activity_conditions_4"] = 1 if idx[9].strip() == "True" else 0
        dict_with_descriptions["activity_conditions_5"] = 1 if idx[10].strip() == "True" else 0
        dict_with_descriptions["activity_conditions_6"] = 1 if idx[11].strip() == "True" else 0
        dict_with_descriptions["activity_conditions_7"] = 1 if idx[12].strip() == "True" else 0
        dict_with_descriptions["activity_conditions_8"] = 1 if idx[13].strip() == "True" else 0
        dict_with_descriptions["activity_conditions_9"] = 1 if idx[14].strip() == "True" else 0
        dict_with_descriptions["activity_user_id"] = (idx[16])
        dict_with_descriptions["activity_level1"] = 1 if idx[17].strip() == "True" else 0
        dict_with_descriptions["activity_level2"] = 1 if idx[18].strip() == "True" else 0
        dict_with_descriptions["activity_level3"] = 1 if idx[19].strip() == "True" else 0
        dict_with_descriptions["activity_favourite"] = False
        dict_with_descriptions["activity_conditions_1_icon"] = idx[20] if dict_with_descriptions["activity_conditions_1"] == 1 else 0
        dict_with_descriptions["activity_conditions_2_icon"] = idx[21] if dict_with_descriptions["activity_conditions_2"] == 1 else 0
        dict_with_descriptions["activity_conditions_3_icon"] = idx[22] if dict_with_descriptions["activity_conditions_3"] == 1 else 0
        dict_with_descriptions["activity_conditions_4_icon"] = idx[23] if dict_with_descriptions["activity_conditions_4"] == 1 else 0
        dict_with_descriptions["activity_conditions_5_icon"] = idx[24] if dict_with_descriptions["activity_conditions_5"] == 1 else 0
        dict_with_descriptions["activity_conditions_6_icon"] = idx[25] if dict_with_descriptions["activity_conditions_6"] == 1 else 0
        dict_with_descriptions["activity_conditions_7_icon"] = idx[26] if dict_with_descriptions["activity_conditions_7"] == 1 else 0
        dict_with_descriptions["activity_conditions_8_icon"] = idx[27] if dict_with_descriptions["activity_conditions_8"] == 1 else 0
        dict_with_descriptions["activity_conditions_9_icon"] = idx[28] if dict_with_descriptions["activity_conditions_9"] == 1 else 0
        list_with_dict_description.append(dict_with_descriptions)
        dict_with_descriptions = {}
    # pprint(list_with_dict_description)
    return list_with_dict_description

def adding_activities_to_base():
    input_data = create_dict_with_descriptions()
    today = datetime.today()
    db.session.query(ActivitiesTable).delete()
    db.session.commit()
    for idx in input_data:
        activity = ActivitiesTable(
            activity_name = idx["activite_name"],
            activity_description = idx["activite_description"],
            activity_todo_list = idx["activite_todo_list"],
            # activity_conditions = idx["activite_conditions"],
            activity_calories = idx["activite_calories"],
            activity_conditions_temp = idx["activity_conditions_temp"],
            activity_conditions_1 = bool(idx["activity_conditions_1"]),
            activity_conditions_2 = idx["activity_conditions_2"],
            activity_conditions_3 = idx["activity_conditions_3"],
            activity_conditions_4 = idx["activity_conditions_4"],
            activity_conditions_5 = idx["activity_conditions_5"],
            activity_conditions_6 = idx["activity_conditions_6"],
            activity_conditions_7 = idx["activity_conditions_7"],
            activity_conditions_8 = idx["activity_conditions_8"],
            activity_conditions_9 = idx["activity_conditions_9"],
            activity_user_id = idx["activity_user_id"],
            activity_favourite = idx["activity_favourite"],
            activity_level1 = idx["activity_level1"],
            activity_level2 = idx["activity_level2"],
            activity_level3 = idx["activity_level3"],
            activity_timestamp = today,
            activity_conditions_1_icon = idx["activity_conditions_1_icon"],
            activity_conditions_2_icon = idx["activity_conditions_2_icon"],
            activity_conditions_3_icon = idx["activity_conditions_3_icon"],
            activity_conditions_4_icon = idx["activity_conditions_4_icon"],
            activity_conditions_5_icon = idx["activity_conditions_5_icon"],
            activity_conditions_6_icon = idx["activity_conditions_6_icon"],
            activity_conditions_7_icon = idx["activity_conditions_7_icon"],
            activity_conditions_8_icon = idx["activity_conditions_8_icon"],
            activity_conditions_9_icon = idx["activity_conditions_9_icon"],
            # **idx
            )
        
        # print(activity.activity_conditions_temp)
        db.session.add(activity)  
        db.session.commit()
 
adding_activities_to_base()
