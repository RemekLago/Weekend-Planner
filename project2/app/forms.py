from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, WeatherTable, IconsTable, ActivitiesTable, ChosenActivitiesTable
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=500)])
    location = TextAreaField('Location', validators=[Length(min=0, max=100)])
    activity_level1 = BooleanField('activity_lavel1')
    activity_level2 = BooleanField('activity_lavel2')
    activity_level3 = BooleanField('activity_lavel3')
    submit = SubmitField('Submit')

class AddActivity(FlaskForm):
    activity_name = TextAreaField('activity_name', validators=[Length(min=0, max=140)])
    activity_description = TextAreaField('activity_description', validators=[Length(min=0, max=500)])
    activity_todo_list = TextAreaField('activity_todo_list', validators=[Length(min=0, max=500)])
    activity_calories = TextAreaField('activity_calories', validators=[Length(min=0, max=140)])
    activity_favourite = BooleanField('activity_favourite')
    activity_user_id = TextAreaField('activity_user_id')
    activity_level1 = BooleanField('activity_lavel1')
    activity_level2 = BooleanField('activity_lavel2')
    activity_level3 = BooleanField('activity_lavel3')
    activity_conditions_temp = TextAreaField('activity_conditions_temp', validators=[Length(min=0, max=10)])
    activity_conditions_1 = BooleanField('activity_conditions_1')
    activity_conditions_2 = BooleanField('activity_conditions_2')
    activity_conditions_3 = BooleanField('activity_conditions_3')
    activity_conditions_4 = BooleanField('activity_conditions_4')
    activity_conditions_5 = BooleanField('activity_conditions_5')
    activity_conditions_6 = BooleanField('activity_conditions_6')
    activity_conditions_7 = BooleanField('activity_conditions_7')
    activity_conditions_8 = BooleanField('activity_conditions_8')
    activity_conditions_9 = BooleanField('activity_conditions_9')
    activity_conditions_1_icon = TextAreaField('activity_conditions_1_icon', validators=[Length(min=0, max=100)])
    activity_conditions_2_icon = TextAreaField('activity_conditions_2_icon', validators=[Length(min=0, max=100)])
    activity_conditions_3_icon = TextAreaField('activity_conditions_3_icon', validators=[Length(min=0, max=100)])
    activity_conditions_4_icon = TextAreaField('activity_conditions_4_icon', validators=[Length(min=0, max=100)])
    activity_conditions_5_icon = TextAreaField('activity_conditions_5_icon', validators=[Length(min=0, max=100)])
    activity_conditions_6_icon = TextAreaField('activity_conditions_6_icon', validators=[Length(min=0, max=100)])
    activity_conditions_7_icon = TextAreaField('activity_conditions_7_icon', validators=[Length(min=0, max=100)])
    activity_conditions_8_icon = TextAreaField('activity_conditions_8_icon', validators=[Length(min=0, max=100)])
    activity_conditions_9_icon = TextAreaField('activity_conditions_9_icon', validators=[Length(min=0, max=100)])
    chosen_status= BooleanField('chosen_status')
    submit = SubmitField('Submit')

class EditActivity(FlaskForm):
    activity_name = TextAreaField('activity_name', validators=[Length(min=0, max=140)])
    activity_description = TextAreaField('activity_description', validators=[Length(min=0, max=500)])
    activity_todo_list = TextAreaField('activity_todo_list', validators=[Length(min=0, max=500)])
    activity_calories = TextAreaField('activity_calories', validators=[Length(min=0, max=140)])
    activity_favourite = BooleanField('activity_favourite')
    activity_user_id = TextAreaField('activity_user_id')
    activity_level1 = BooleanField('activity_lavel1')
    activity_level2 = BooleanField('activity_lavel2')
    activity_level3 = BooleanField('activity_lavel3')
    activity_conditions_temp = TextAreaField('activity_conditions_temp', validators=[Length(min=0, max=10)])
    activity_conditions_1 = BooleanField('activity_conditions_1')
    activity_conditions_2 = BooleanField('activity_conditions_2')
    activity_conditions_3 = BooleanField('activity_conditions_3')
    activity_conditions_4 = BooleanField('activity_conditions_4')
    activity_conditions_5 = BooleanField('activity_conditions_5')
    activity_conditions_6 = BooleanField('activity_conditions_6')
    activity_conditions_7 = BooleanField('activity_conditions_7')
    activity_conditions_8 = BooleanField('activity_conditions_8')
    activity_conditions_9 = BooleanField('activity_conditions_9')
    activity_conditions_1_icon = TextAreaField('activity_conditions_1_icon', validators=[Length(min=0, max=100)])
    activity_conditions_2_icon = TextAreaField('activity_conditions_2_icon', validators=[Length(min=0, max=100)])
    activity_conditions_3_icon = TextAreaField('activity_conditions_3_icon', validators=[Length(min=0, max=100)])
    activity_conditions_4_icon = TextAreaField('activity_conditions_4_icon', validators=[Length(min=0, max=100)])
    activity_conditions_5_icon = TextAreaField('activity_conditions_5_icon', validators=[Length(min=0, max=100)])
    activity_conditions_6_icon = TextAreaField('activity_conditions_6_icon', validators=[Length(min=0, max=100)])
    activity_conditions_7_icon = TextAreaField('activity_conditions_7_icon', validators=[Length(min=0, max=100)])
    activity_conditions_8_icon = TextAreaField('activity_conditions_8_icon', validators=[Length(min=0, max=100)])
    activity_conditions_9_icon = TextAreaField('activity_conditions_9_icon', validators=[Length(min=0, max=100)])
    chosen_status= BooleanField('chosen_status')
    submit = SubmitField('Submit')


class AddImage(FlaskForm):
    image_name = TextAreaField('image_name', validators=[Length(min=0, max=100)])
    image_user = TextAreaField('image_user', validators=[Length(min=0, max=100)])
    image_description = TextAreaField('image_description', validators=[Length(min=0, max=500)])
    image_link = TextAreaField('image_link', validators=[Length(min=0, max=500)])
    submit = SubmitField('Submit')


class ChosenActivities(FlaskForm):
    chosen_activity_name = TextAreaField('activity_name', validators=[Length(min=0, max=140)])
    chosen_status = BooleanField('chosen_atatus')
    submit = SubmitField('Submit')
