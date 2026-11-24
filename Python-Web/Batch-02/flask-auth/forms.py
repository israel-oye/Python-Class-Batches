from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, ValidationError

from models import User


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name')
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField(
        'Password', 
        validators=[
            DataRequired(), 
            Length(min=8, message='Password must be at least 8 characters')
        ]
    )

    def validate_email(self, field: EmailField):
        email = field.data
        print("Validate email....", User.query.filter_by(email=email).first())
        if User.query.filter_by(email=email).first():
            raise ValidationError("Email is registered")
