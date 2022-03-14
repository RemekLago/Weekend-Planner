from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User, ActivitiesTable, WeatherTable, IconsTable
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from datetime import datetime, timedelta
from app.forms import EditProfileForm, AddActivity, EditActivity


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
    today = str(datetime.now().date())
    weather = WeatherTable.query.filter((WeatherTable.weather_location==user.location)&(WeatherTable.weather_date>=today)).all()
    weather_today = WeatherTable.query.filter((WeatherTable.weather_location==user.location)&(WeatherTable.weather_date==today)).all()
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
    return render_template("gallery.html")

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
        activity_conditions = form.activity_conditions,
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
        )

        db.session.add(activity)
        db.session.commit()
        flash('Congratulations, you have been added new activity!')
        return redirect(url_for('user'))
    return render_template('add_activity.html', title='Add Activity', form=form, activities=activities, icons=icons)
    

@app.route('/edit_activity', methods=['GET', 'POST'])
def edit_activity():
    form = EditActivity()
    icons = IconsTable()

    if form.validate_on_submit():
        current_activity_name = form.activity_name.data
        current_activity_description = form.activity_description.data
        current_activity_todo_list = form.activity_todo_list.data
        current_activity_conditions = form.activity_conditions.data
        current_activity_calories = form.activity_calories.data
        current_activity_favourite = form.activity_favourite.data
        current_activity_user_id = form.activity_user_id.data

        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_activity'))
    elif request.method == 'GET':
        form.activity_name.data = current_activity_name
        form.activity_description.data = current_activity_description
        form.activity_todo_list.data = current_activity_todo_list
        form.activity_conditions.data = current_activity_conditions
        form.activity_calories.data = current_activity_calories
        form.activity_favourite.data = current_activity_favourite
        form.activity_user_id.data = current_activity_user_id
    return render_template('edit_activity.html', title='Edit Activity', form=form, icons=icons)







