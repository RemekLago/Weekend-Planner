import os
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User, ActivitiesTable, WeatherTable, IconsTable, ImageTable
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from datetime import datetime, timedelta
from app.forms import EditProfileForm, AddActivity, EditActivity, AddImage
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
from sqlalchemy import cast,Date
# from app import mongo


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
def index():
    weather = WeatherTable.query.all()
    return render_template('index.html', weather=weather)


@login_required
@app.route('/propositions')
def propositions():
    user = User.query.all()
    activities = ActivitiesTable.query.all()
    today = str(datetime.now().date() + timedelta(days = 1))
    # today = str(datetime.now().date())
    weather = WeatherTable.query.filter((WeatherTable.weather_location==User.location)&(WeatherTable.weather_date>(today))).all()
    icons = IconsTable.query.all()
    return render_template('propositions.html', title='Home',  activities=activities, weather=weather, icons=icons, user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # print(current_user.__dir__())
    if current_user.is_authenticated:
        return redirect(url_for('user', username=current_user.username))
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('propositions')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('propositions'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    # activities = ActivitiesTable.query.filter_by(username=username).first_or_404()
    activities = ActivitiesTable.query.all()
    # activities = ActivitiesTable.query.filter(ActivitiesTable.user_id==current_user.id)
    #weather = WeatherTable.query.get(1)
    # weather = WeatherTable.query.all()
    # today = str(datetime.now().date() + timedelta(days = 2))
    today = datetime.now().date()
    weather = WeatherTable.query.filter((WeatherTable.weather_location==user.location)&(WeatherTable.weather_date>=today)).all()
    weather_today = WeatherTable.query.filter((WeatherTable.weather_location==user.location)&(WeatherTable.weather_date==today)).all()
    # print(weather_today)
    # print(today)
    # print(WeatherTable.query(WeatherTable.weather_date).all())
    # weather = WeatherTable.query.filter(WeatherTable.weather_date>=today).all()
    icons = IconsTable.query.all()
    return render_template('user.html', user=user, activities=activities, weather=weather, icons=icons, weather_today=weather_today)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.location = form.location.data
        current_user.activity_level = form.activity_level.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.location.data = current_user.location
        form.activity_level.data = current_user.activity_level
    return render_template('edit_profile.html', title='Edit Profile',form=form)


@app.route("/activities", methods=["GET", "POST"])
def activities():
    activities = ActivitiesTable.query.all()
    icons = IconsTable.query.all()
    return render_template("activities.html", activities=activities, icons=icons)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html", gallery=mongo.db.gallery.find())

@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    form = AddActivity()
    icons = IconsTable.query.all()
    today = datetime.today()
    if form.validate_on_submit():
        activity = ActivitiesTable(
        activity_name = form.activity_name.data,
        activity_description = form.activity_description.data,
        activity_todo_list = form.activity_todo_list.data,
        activity_calories = form.activity_calories.data,
        activity_favourite = form.activity_favourite.data,
        activity_conditions_temp = form.activity_conditions_temp.data,
        activity_conditions_1 = form.activity_conditions_1.data,
        activity_conditions_2 = form.activity_conditions_2.data,
        activity_conditions_3 = form.activity_conditions_3.data,
        activity_conditions_4 = form.activity_conditions_4.data,
        activity_conditions_5 = form.activity_conditions_5.data,
        activity_conditions_6 = form.activity_conditions_6.data,
        activity_conditions_7 = form.activity_conditions_7.data,
        activity_conditions_8 = form.activity_conditions_8.data,
        activity_conditions_9 = form.activity_conditions_9.data,
        activity_level1 = form.activity_level1.data,
        activity_level2 = form.activity_level2.data,
        activity_level3 = form.activity_level3.data,
        activity_timestamp = today,
        activity_user_id = current_user.id
        )

        db.session.add(activity)
        db.session.commit()
        flash('Congratulations, you have been added new activity!')
        return redirect(url_for('add_activity'))
    return render_template('add_activity.html', title='Add Activity', form=form, icons=icons)
    

@app.route('/edit_activity', methods=['GET', 'POST'])
def edit_activity():
    form = EditActivity()
    icons = IconsTable()
    today = datetime.today()
    if form.validate_on_submit():
        activity_name = form.activity_name.data,
        activity_description = form.activity_description.data,
        activity_todo_list = form.activity_todo_list.data,
        activity_calories = form.activity_calories.data,
        activity_favourite = form.activity_favourite.data,
        activity_user_id = form.activity_user_id.data,
        activity_conditions_temp = form.activity_conditions_temp.data,
        activity_conditions_1 = form.activity_conditions_1.data,
        activity_conditions_2 = form.activity_conditions_2.data,
        activity_conditions_3 = form.activity_conditions_3.data,
        activity_conditions_4 = form.activity_conditions_4.data,
        activity_conditions_5 = form.activity_conditions_5.data,
        activity_conditions_6 = form.activity_conditions_6.data,
        activity_conditions_7 = form.activity_conditions_7.data,
        activity_conditions_8 = form.activity_conditions_8.data,
        activity_conditions_9 = form.activity_conditions_9.data,
        activity_level1 = form.activity_level1.data,
        activity_level2 = form.activity_level2.data,
        activity_level3 = form.activity_level3.data,
        activity_timestamp = today
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_activity'))

    elif request.method == 'GET':
            form.activity_name.data = activity_name
            form.activity_description.data = activity_description
            form.activity_todo_list.data = activity_todo_list
            form.activity_calories.data = activity_calories
            form.activity_favourite.data = activity_favourite
            form.activity_user_id.data = activity_user_id
            form.activity_conditions_temp.data = activity_conditions_temp
            form.activity_conditions_1.data = activity_conditions_1
            form.activity_conditions_2.data = activity_conditions_2
            form.activity_conditions_3.data = activity_conditions_3
            form.activity_conditions_4.data = activity_conditions_4
            form.activity_conditions_5.data = activity_conditions_5
            form.activity_conditions_6.data = activity_conditions_6
            form.activity_conditions_7.data = activity_conditions_7
            form.activity_conditions_8.data = activity_conditions_8
            form.activity_conditions_9.data = activity_conditions_9
            form.activity_level1.data = activity_level1
            form.activity_level2.data = activity_level2
            form.activity_level3.data = activity_level3
    return render_template('edit_activity.html', title='Edit Activity')


@app.route("/users_activities", methods=["GET", "POST"])
def users_activities():
    form = ActivitiesTable()
    user = User.query.all()
    activities = ActivitiesTable.query.filter(ActivitiesTable.activity_user_id==current_user.id).all()
    icons = IconsTable.query.all()
    return render_template("users_activities.html", title='Users activities',activities=activities, icons=icons, user=user, form=form)


@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():
    form = AddImage()
    if form.validate_on_submit():
        image = ImageTable(
        image_name=form.image_name.data,
        image_description=form.image_description.data,
        image_link=form.image_link.data
        )

        image_name = secure_filename(image.image_name)
        # image.save(os.path.join("app/static/uploads/", image_name))
        f=request.files
        print(f)



        db.session.add(image)
        db.session.commit()
        flash("Congratulations, you have been added new image")
        return redirect(url_for('/upload_image'))
    return render_template("upload_image.html")


    # if request.method == "POST":
    #     image = request.files["image"]
    #     description = request.form.get("description")
    #     if image and description and image.filename.split(".")[-1].lower() in ALLOWED_EXTENSIONS:
    #         filename = secure_filename(image.filename)
    #         image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    #         mongo.db.gallery.insert_one(
    #             {
    #             "filename": filename,
    #             "description": description.strip()
    #         })

    #         flash("Successfully uploaded image", "success")
    #         return redirect(url_for("upload_image"))
    #     else:
    #         flash("An error occurred while uploading the image!", "danger")
    #         return redirect(url_for("upload_image"))
    





