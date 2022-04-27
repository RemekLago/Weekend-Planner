from app import app, db
from app.models import User, ActivitiesTable, WeatherTable, IconsTable
from management.weather import adding_data_for_all_cities

adding_data_for_all_cities()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'ActivitiesTable': ActivitiesTable, 'WeatherTable': WeatherTable, 'IconsTable': IconsTable}
