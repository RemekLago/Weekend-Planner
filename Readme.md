Application operation:
1. the user enters the home page index.html, where there is a description of the application functioning
2. Then the user can register on the register.html website (gives login / email, password), data are saved in the User table.
3. After registration, the user enters the login.html page, where he must log in
4. after logging in, he can go to the user.html website, where he has information about his profile. Here he can edit his profile (complete his location, add information about himself, define his activity level), he can add his new activity or edit it (if he has previously created it), he can also add a photo to the gallery (visible to everyone).
Without editing the profile and specifying his location, he will not see the current weather and the weather forecast for the next week for his location. This information appears on the profile page, if the user has not provided this data, there is a request to edit his profile.
5. Editing the profile is done on the edit_profile.html page
6. adding a new activity is done on the add_activity.html page
The 7th edition of the activity takes place on the edit_activity.html page
8. Adding photos to the gallery on the upload_image.html website, then the images are visible in the gallery on galery.html
9. Then the user can go to the activity page at activity.html, here he has a list of activities with their description. Each activity has: name, description, Todo list, i.e. a list of things necessary to perform the activity, the minimum temperature at which it can be performed, the estimated number of kcalories that is burned for 1 hour of a given activity, in the form of checkboxes, the types of user activity levels and icons are marked symbolizing the weather in which the activity is possible
10. the user can go to the website propositions.html where activities for the next weekend will be proposed, divided into Saturday and Sunday. The user can select the activities he or she is interested in using checkboxes.
The proposed activities are filtered based on the weather forecast for the user's location, the type of user activity and parameters of the activity's characteristics, such as the minimum temperature, icons, symbols / weather icons for which it is possible to perform. After selecting the activity, the user is transferred to the summary page.
11. On the website chosen_activities.html, the user has the activities presented, which he has chosen, after clicking send an email, the system sends an e-mail to the user's address with the name of the activity and a list of things to be prepared (Todo list)


Apps files:

planner.py - main file

weather_icon_add.py - file for loading names and descriptions of weather icons / symbols, saving to icons_table table

weather.py - file for loading weather for cities already in the database, should be run every day at midnight, saving data to the weather_table and weather_table_histrory tables. The weather_table is cleared daily, but the historical data is in weather_table_histrory.

weather_one_city.py - a file for loading weather, but only for one city, it is launched only when the user adds his location or changes it (this is done in the profile edition)

activities_system_add.py - file for loading basic and system activities, saving to activities_table

activities_description.txt - file for loading basic activities into the system (description of activities and their parameters)

city_names.txt - file for loading city names, used only at the beginning as test input

routes.py - file with paths to all subpages

models.py - classes for creating data in the database / tables

forms.py - file with classes for form data verification