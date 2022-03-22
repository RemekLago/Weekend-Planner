from app import app, db
from app.models import User, ActivitiesTable, WeatherTable, IconsTable
from keys import cloud_name, api_key, api_secret


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'ActivitiesTable': ActivitiesTable, 'WeatherTable': WeatherTable, 'IconsTable': IconsTable}
