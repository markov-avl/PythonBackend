from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    identifier = StringField(
        label='Логин/телефон',
        validators=[
            DataRequired(message='Обязательное поле')
        ]
    )
    password = PasswordField(
        label='Пароль',
        validators=[
            DataRequired(message='Обязательное поле')
        ]
    )
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
