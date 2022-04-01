from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_moment import Moment
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from keys import Mailkey
from .celery_maker import make_celery

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery_obj = make_celery(app)



# app.config['MAIL_SERVER']="smtp.gmail.com"
# app.config['MAIL_PORT'] = 587
# # app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USE_TLS'] = True
# # app.config['MAIL_USE_SSL'] = True
# # app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USERNAME'] = "jacekwacek@gmail.com"
# app.config['MAIL_PASSWORD'] = f"{Mailkey}"
# app.config['MAIL_DEFAULT_SENDER'] = "jacekwacek@gmail.com"
# mail = Mail(app)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# UPLOAD_FOLDER = 'app/static/uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# app.secret_key = "secret key"

UPLOAD_FOLDER = 'app/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
secret_key = "secret key"


from app import routes, models