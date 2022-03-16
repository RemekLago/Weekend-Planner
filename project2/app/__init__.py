from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_moment import Moment
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)
# app.config.from_object(PyMongo)
# ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]
# # app.config["SECRET_KEY"] = "SECRET_KEY"
# app.config["UPLOAD_FOLDER"] = "app/static/uploads/"
# app.config["MONGO_DBNAME"] = "gallery"
# app.config["MONGO_URI"] = "mongodb://localhost:27017/gallery"
# mongo = PyMongo(app)



from app import routes, models