from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, WeatherTable, IconsTable
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
    activity_level = StringField('Activity level', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddActivity(FlaskForm):
    activity_name = TextAreaField('activity_name ', validators=[Length(min=0, max=140)])
    activity_description = TextAreaField('activity_description', validators=[Length(min=0, max=500)])
    activity_todo_list = TextAreaField('activity_todo_list', validators=[Length(min=0, max=500)])
    activity_calories = TextAreaField('activity_calories', validators=[Length(min=0, max=140)])
    activity_favourite = TextAreaField('activity_favourite')
    activity_user_id = TextAreaField('activity_user_id')
    activity_level1 = TextAreaField('activity_lavel1', validators=[Length(min=0, max=10)])
    activity_level2 = TextAreaField('activity_lavel2', validators=[Length(min=0, max=10)])
    activity_level3 = TextAreaField('activity_lavel3', validators=[Length(min=0, max=10)])
    activity_conditions_temp = TextAreaField('activity_conditions_temp', validators=[Length(min=0, max=10)])
    activity_conditions_1 = TextAreaField('activity_conditions_1', validators=[Length(min=0, max=10)])
    activity_conditions_2 = TextAreaField('activity_conditions_2', validators=[Length(min=0, max=10)])
    activity_conditions_3 = TextAreaField('activity_conditions_3', validators=[Length(min=0, max=10)])
    activity_conditions_4 = TextAreaField('activity_conditions_4', validators=[Length(min=0, max=10)])
    activity_conditions_5 = TextAreaField('activity_conditions_5', validators=[Length(min=0, max=10)])
    activity_conditions_6 = TextAreaField('activity_conditions_6', validators=[Length(min=0, max=10)])
    activity_conditions_7 = TextAreaField('activity_conditions_7', validators=[Length(min=0, max=10)])
    activity_conditions_8 = TextAreaField('activity_conditions_8', validators=[Length(min=0, max=10)])
    activity_conditions_9 = TextAreaField('activity_conditions_9', validators=[Length(min=0, max=10)])
    submit = SubmitField('Submit')

class EditActivity(FlaskForm):
    activity_name = TextAreaField('activity_name', validators=[Length(min=0, max=140)])
    activity_description = TextAreaField('activity_description', validators=[Length(min=0, max=140)])
    activity_todo_list = TextAreaField('activity_todo_list', validators=[Length(min=0, max=140)])
    activity_conditions = TextAreaField('activity_conditions', validators=[Length(min=0, max=140)])
    activity_calories = TextAreaField('activity_calories', validators=[Length(min=0, max=140)])
    activity_favourite = TextAreaField('activity_favourite', validators=[Length(min=0, max=140)])
    activity_user_id = TextAreaField('activity_user_id' , validators=[Length(min=0, max=140)])
    activity_level1 = TextAreaField('activity_lavel1', validators=[Length(min=0, max=10)])
    activity_level2 = TextAreaField('activity_lavel2', validators=[Length(min=0, max=10)])
    activity_level3 = TextAreaField('activity_lavel3', validators=[Length(min=0, max=10)])
    activity_conditions_temp = TextAreaField('activity_conditions_temp', validators=[Length(min=0, max=10)])
    activity_conditions_1 = TextAreaField('activity_conditions_1', validators=[Length(min=0, max=10)])
    activity_conditions_2 = TextAreaField('activity_conditions_2', validators=[Length(min=0, max=10)])
    activity_conditions_3 = TextAreaField('activity_conditions_3', validators=[Length(min=0, max=10)])
    activity_conditions_4 = TextAreaField('activity_conditions_4', validators=[Length(min=0, max=10)])
    activity_conditions_5 = TextAreaField('activity_conditions_5', validators=[Length(min=0, max=10)])
    activity_conditions_6 = TextAreaField('activity_conditions_6', validators=[Length(min=0, max=10)])
    activity_conditions_7 = TextAreaField('activity_conditions_7', validators=[Length(min=0, max=10)])
    activity_conditions_8 = TextAreaField('activity_conditions_8', validators=[Length(min=0, max=10)])
    activity_conditions_9 = TextAreaField('activity_conditions_9', validators=[Length(min=0, max=10)])
    submit = SubmitField('Submit')