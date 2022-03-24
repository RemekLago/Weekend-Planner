import os
from app import app
from flask import render_template, flash, redirect, url_for, send_from_directory
from app.forms import CityNames, LoginForm
from flask_login import current_user, login_user
from app.models import User, ActivitiesTable, WeatherTable, IconsTable, ImageTable, ChosenActivitiesTable, CityTable, ChosenActivitiesTableHistory
from flask_login import logout_user
from flask_login import login_required
from flask import request, flash
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from datetime import datetime, timedelta
from app.forms import EditProfileForm, AddActivity, EditActivity, AddImage, ChosenActivities
from werkzeug.utils import secure_filename
from sqlalchemy import cast,Date
from flask_mail import Mail, Message
from app import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
import urllib.request
import smtplib, ssl
from werkzeug.middleware.shared_data import SharedDataMiddleware
from keys import Mailkey
# from  weather import adding_data_for_all_cities as weather_input
from  weather_one_city import adding_data_for_all_cities as weather_one_city_input

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
@app.route('/propositions', methods=["GET", "POST"])
def propositions():
    form = ChosenActivities()
    tomorrow = datetime.now().date() + timedelta(days = 1)
    week = datetime.now().date() + timedelta(days = 7)
    today = datetime.now().date()
    user = User.query.filter(User.username==current_user.username).all()
    icons = IconsTable.query.all()
    
    weather = WeatherTable \
        .query\
        .filter(
            (WeatherTable.weather_location==User.location)
            & (WeatherTable.weather_date>(tomorrow))
        
        ).all()
    weather2 = WeatherTable \
        .query\
        .filter(
            (WeatherTable.weather_day_name=="Saturday")
            & (WeatherTable.weather_date>(tomorrow))
            # & (WeatherTable.weather_date<(week))
        & (WeatherTable.weather_location==current_user.location)
        ).all()
    weather3 = WeatherTable \
    .query\
    .filter(
        (WeatherTable.weather_day_name=="Sunday")
        & (WeatherTable.weather_date>(tomorrow))
        # & (WeatherTable.weather_date<(week))
        & (WeatherTable.weather_location==current_user.location)
    ).all()
    activities = ActivitiesTable\
        .query\
        .filter(
            (
            ActivitiesTable.activity_level1==User.activity_level1  
            | ActivitiesTable.activity_level2==User.activity_level2 
            | ActivitiesTable.activity_level3==User.activity_level3
            ) 
            & 
            (ActivitiesTable.activity_conditions_temp <= WeatherTable.weather_temperature)
            # & (
            # ActivitiesTable.activity_conditions_1_icon==weather2[0].weather_icon
            # | ActivitiesTable.activity_conditions_2_icon==weather2[0].weather_icon
            # | ActivitiesTable.activity_conditions_3_icon==weather2[0].weather_icon
            # | ActivitiesTable.activity_conditions_4_icon==weather2[0].weather_icon
            # | ActivitiesTable.activity_conditions_5_icon==weather2[0].weather_icon
            # | ActivitiesTable.activity_conditions_6_icon==weather2[0].weather_icon
            # | ActivitiesTable.activity_conditions_7_icon==weather2[0].weather_icon
            # | ActivitiesTable.activity_conditions_8_icon==weather2[0].weather_icon
            # | ActivitiesTable.activity_conditions_9_icon==weather2[0].weather_icon
            # )
        ).all()     
    # print(weather2[0].weather_icon)
    # for idx in activities:
    #     print(idx) 
    #     print(idx.activity_conditions_1_icon)
        
    if form.validate_on_submit():
        db.session.query(ChosenActivitiesTable).delete()
        db.session.commit()

        chosen_activity = ChosenActivitiesTable(
        chosen_activity_name = form.chosen_activity_name.data,    
        chosen_status = form.chosen_status.data,
        chosen_activity_timestamp = today,
        )
        chosen_activity2 = ChosenActivitiesTableHistory(
        chosen_activity_name = form.chosen_activity_name.data,    
        chosen_status = form.chosen_status.data,
        chosen_activity_timestamp = today,
        )

        db.session.add(chosen_activity)
        db.session.add(chosen_activity2)
        db.session.commit()
        flash('Congratulations, you have been added activities for the weekend!')
        return redirect(url_for('chosen_activities'))
    return render_template('propositions.html', title='Propositions', 
    activities=activities, weather=weather, weather2=weather2, weather3=weather3, 
    icons=icons, user=user, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
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
            next_page = url_for('user', username=current_user.username)
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
    # start = weather_input()
    user = User.query.filter_by(username=username).first_or_404()
    icons = IconsTable.query.all()
    activities = ActivitiesTable\
        .query\
            .filter(ActivitiesTable.activity_user_id==user.id).all()
    today = datetime.today()
    tomorrow = str(datetime.now().date() + timedelta(days = 1))
    weather = WeatherTable\
        .query\
            .filter(\
                (WeatherTable.weather_location==user.location)\
                &(WeatherTable.weather_date>today)).all()
    weather_today = WeatherTable\
        .query\
            .filter(\
                (WeatherTable.weather_location==user.location)\
                &(WeatherTable.weather_date<tomorrow)).all()
    return render_template('user.html', user=user, activities=activities, 
            weather=weather, icons=icons, weather_today=weather_today)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.location = form.location.data
        current_user.activity_level1 = form.activity_level1.data
        current_user.activity_level2 = form.activity_level2.data
        current_user.activity_level3 = form.activity_level3.data
        city = CityTable(
        city_name = form.location.data
        )
        if not CityTable.query.filter(CityTable.city_name==city.city_name).all():
            # db.session.query(CityTable).delete()
            db.session.add(city)
            db.session.commit()
            take_weather_date = weather_one_city_input(city.city_name)
            # pobieranie pogody w tle
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.location.data = current_user.location
        form.activity_level1.data = current_user.activity_level1
        form.activity_level2.data = current_user.activity_level2
        form.activity_level3.data = current_user.activity_level3
    return render_template('edit_profile.html', title='Edit Profile',
        form=form)


@app.route("/activities", methods=["GET", "POST"])
def activities():
    activities = ActivitiesTable.query.all()
    icons = IconsTable.query.all()
    return render_template("activities.html", activities=activities, icons=icons)


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    form = AddActivity()
    icons = IconsTable.query.all()
    today = datetime.today()
    if form.validate_on_submit():
        test_ativity_conditions = (form.activity_conditions_1.data or form.activity_conditions_2.data or form.activity_conditions_3.data
        or form.activity_conditions_4.data or form.activity_conditions_5.data or form.activity_conditions_6.data or 
        form.activity_conditions_7.data or form.activity_conditions_8.data or form.activity_conditions_9.data)
        if not test_ativity_conditions:
            flash("Error, please check a minimum of one weather condition")
            return redirect(url_for('add_activity'))
        test_user_activity = (form.activity_level1.data or form.activity_level2.data or form.activity_level3.data)    
        if not test_user_activity:
            flash("Error, please check a minimum of one option of level activity for the user")
            return redirect(url_for('add_activity'))
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
            activity_user_id = current_user.id,
            activity_conditions_1_icon = "01d",
            activity_conditions_2_icon = "02d",
            activity_conditions_3_icon = "03d",
            activity_conditions_4_icon = "04d",
            activity_conditions_5_icon = "09d",
            activity_conditions_6_icon = "10d",
            activity_conditions_7_icon = "11d",
            activity_conditions_8_icon = "13d",
            activity_conditions_9_icon = "50d",
            )

        db.session.add(activity)
        db.session.commit()
        flash('Congratulations, you have been added new activity!')
        return redirect(url_for('add_activity'))
    return render_template('add_activity.html', title='Add Activity', form=form, icons=icons)
    

@app.route('/edit_activity/<activity_id>', methods=['GET', 'POST'])
def edit_activity(activity_id):
    activity = ActivitiesTable.query.get_or_404(activity_id)
    form = EditActivity()
    icons = IconsTable.query.all()
    today = datetime.today()
    
    if form.validate_on_submit():
        test_ativity_conditions = (form.activity_conditions_1.data or form.activity_conditions_2.data or form.activity_conditions_3.data
        or form.activity_conditions_4.data or form.activity_conditions_5.data or form.activity_conditions_6.data or 
        form.activity_conditions_7.data or form.activity_conditions_8.data or form.activity_conditions_9.data)
        if not test_ativity_conditions:
            flash("Error, please check a minimum of one weather condition")
            return redirect(url_for('add_activity'))
        test_user_activity = (form.activity_level1.data or form.activity_level2.data or form.activity_level3.data)    
        if not test_user_activity:
            flash("Error, please check a minimum of one option of level activity for the user")
            return redirect(url_for('add_activity'))
        activity.activity_name = form.activity_name.data
        activity.activity_description = form.activity_description.data
        activity.activity_todo_list = form.activity_todo_list.data
        activity.activity_calories = form.activity_calories.data
        activity.activity_favourite = form.activity_favourite.data
        activity.activity_conditions_temp = form.activity_conditions_temp.data
        activity.activity_conditions_1 = form.activity_conditions_1.data
        activity.activity_conditions_2 = form.activity_conditions_2.data
        activity.activity_conditions_3 = form.activity_conditions_3.data
        activity.activity_conditions_4 = form.activity_conditions_4.data
        activity.activity_conditions_5 = form.activity_conditions_5.data
        activity.activity_conditions_6 = form.activity_conditions_6.data
        activity.activity_conditions_7 = form.activity_conditions_7.data
        activity.activity_conditions_8 = form.activity_conditions_8.data
        activity.activity_conditions_9 = form.activity_conditions_9.data
        activity.activity_level1 = form.activity_level1.data
        activity.activity_level2 = form.activity_level2.data
        activity.activity_level3 = form.activity_level3.data
        activity.activity_timestamp = today
        activity.activity_user_id = current_user.id
        activity.activity_conditions_1_icon = "01d"
        activity.activity_conditions_2_icon = "02d"
        activity.activity_conditions_3_icon = "03d"
        activity.activity_conditions_4_icon = "04d"
        activity.activity_conditions_5_icon = "09d"
        activity.activity_conditions_6_icon = "10d"
        activity.activity_conditions_7_icon = "11d"
        activity.activity_conditions_8_icon = "13d"
        activity.activity_conditions_9_icon = "50d"
        
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_activity', activity_id=activity.id))

    form.activity_name.data = activity.activity_name
    form.activity_description.data = activity.activity_description
    form.activity_todo_list.data = activity.activity_todo_list
    form.activity_calories.data = activity.activity_calories
    form.activity_favourite.data = activity.activity_favourite
    form.activity_user_id.data = activity.activity_user_id
    form.activity_conditions_temp.data = activity.activity_conditions_temp
    form.activity_conditions_1.data = activity.activity_conditions_1
    form.activity_conditions_2.data = activity.activity_conditions_2
    form.activity_conditions_3.data = activity.activity_conditions_3
    form.activity_conditions_4.data = activity.activity_conditions_4
    form.activity_conditions_5.data = activity.activity_conditions_5
    form.activity_conditions_6.data = activity.activity_conditions_6
    form.activity_conditions_7.data = activity.activity_conditions_7
    form.activity_conditions_8.data = activity.activity_conditions_8
    form.activity_conditions_9.data = activity.activity_conditions_9
    form.activity_level1.data = activity.activity_level1
    form.activity_level2.data = activity.activity_level2
    form.activity_level3.data = activity.activity_level3
    form.activity_conditions_1_icon.data = "01d"
    form.activity_conditions_2_icon.data = "02d"
    form.activity_conditions_3_icon.data = "03d"
    form.activity_conditions_4_icon.data = "04d"
    form.activity_conditions_5_icon.data = "09d"
    form.activity_conditions_6_icon.data = "10d"
    form.activity_conditions_7_icon.data = "11d"
    form.activity_conditions_8_icon.data = "13d"
    form.activity_conditions_9_icon.data = "50d"
    return render_template('edit_activity.html', title='Edit Activity', form=form, 
    icons=icons, activity=activity)


@app.route("/users_activities", methods=["GET", "POST"])
def users_activities():
    form = ActivitiesTable()
    user = User.query.all()
    icons = IconsTable.query.all()
    activities = ActivitiesTable.query.filter(ActivitiesTable.activity_user_id==current_user.id).all()
    return render_template("users_activities.html", title='Users activities', 
    activities=activities, icons=icons, user=user, form=form)


@app.route("/chosen_activities", methods=["GET", "POST"])
def chosen_activities():
    form = ActivitiesTable()
    user = User.query.all()
    chosen_activities = ChosenActivitiesTable.query.filter(ChosenActivitiesTable.chosen_status==True).all()
    return render_template("chosen_activities.html", title='Users activities', 
    chosen_activities=chosen_activities, user=user, form=form,)


@app.route("/email")
def email():
    
    chosen_activities = ChosenActivitiesTable.query.filter(ChosenActivitiesTable.chosen_status==True).all()
    port = 587  # For SSL
    smtp_server = "smtp.poczta.onet.pl"
    sender_email = "testowo12345@onet.pl"
    receiver_email = "jacekwacek123gmail.com"
    password = "Testowo12345"
    message = """
    This is the email with thing you should prepare for incomming weekend
    f"{chosen_activities}", list of thing to prepare: f"{activity_todo_list}"
    """
    
    context = ssl.create_default_context()
    # context = ssl._create_unverified_context()
    print(1)
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print(2)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.ehlo()  # Can be omitted
    #     print(1)
    #     server.starttls(context=context)
    #     print(2)
    #     server.ehlo()  # Can be omitted
    #     print(3)
    #     server.login(sender_email, password)
    #     print(4)
    #     server.sendmail(sender_email, receiver_email, message)

    return "Mail sent"


@app.route("/gallery")
def gallery():
    images = ImageTable.query.all()
    dir_path = os.path.dirname
    return render_template("gallery.html", images=images, dir_path=dir_path)


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_image')
def show_image():
	return render_template("upload_image.html")


@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    
    # if form.validate_on_submit():
    if request.method == 'POST':
        # if form.validate_on_submit():

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            
            images = ImageTable()
            form = AddImage()
            today = datetime.today()
            user = User.query.all()

            images.image_name=filename
            images.image_date=today
            images.image_user=current_user.username
            images.image_user_id=current_user.id
            images.image_description=form.image_description.data
            images.image_link=os.path.join(UPLOAD_FOLDER, filename)

            db.session.add(images)
            db.session.commit()
        
            flash('Image successfully uploaded')
            return render_template('upload_image.html', form=form, user=user)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)
    return render_template('upload_image.html', title='Upload Image', form=form)



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # return send_from_directory(UPLOAD_FOLDER, filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)