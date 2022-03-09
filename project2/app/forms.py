from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
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
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    location = TextAreaField('Location', validators=[Length(min=0, max=100)])
    submit = SubmitField('Submit')

class AddActivity(FlaskForm):
    activity_name = TextAreaField('activity_name ', validators=[Length(min=0, max=140)])
    activity_description = TextAreaField('activity_description', validators=[Length(min=0, max=500)])
    activity_todo_list = TextAreaField('activity_todo_list', validators=[Length(min=0, max=500)])
    activity_conditions = "list of weather conditions"
    activity_calories = TextAreaField('activity_calories', validators=[Length(min=0, max=140)])
    activity_favorite = TextAreaField('activity_favorite')
    activity_user_id = TextAreaField('activity_user_id')
    submit = SubmitField('Submit')

class EditActivity(FlaskForm):
    activity_name = TextAreaField('activity_name', validators=[Length(min=0, max=140)])
    activity_description = TextAreaField('activity_description', validators=[Length(min=0, max=140)])
    activity_todo_list = TextAreaField('activity_todo_list', validators=[Length(min=0, max=140)])
    activity_conditions = TextAreaField('activity_conditions', validators=[Length(min=0, max=140)])
    activity_calories = TextAreaField('activity_calories', validators=[Length(min=0, max=140)])
    activity_favorite = TextAreaField('activity_favorite', validators=[Length(min=0, max=140)])
    activity_favorite = TextAreaField('activity_favorite', validators=[Length(min=0, max=140)])
    activity_user_id = TextAreaField('activity_user_id' , validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')