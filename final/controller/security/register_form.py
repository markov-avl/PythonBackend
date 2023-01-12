from flask_wtf import FlaskForm
from wtforms import StringField, TelField, PasswordField, SubmitField, Form, Field
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, ValidationError


class RegisterForm(FlaskForm):
    name = StringField(
        label='Имя*',
        validators=[
            DataRequired(message='Обязательное поле'),
            Regexp(r'[А-ЯЁа-яё]+', message='Имя должно содержать только кириллические буквы')
        ],
        render_kw={
            'placeholder': 'Иван'
        }
    )
    surname = StringField(
        label='Фамилия*',
        validators=[
            DataRequired(message='Обязательное поле'),
            Regexp(r'[А-ЯЁа-яё]+', message='Фамилия должна содержать только кириллические буквы')
        ],
        render_kw={
            'placeholder': 'Иванов'
        }
    )
    patronymic = StringField(
        label='Отчество',
        validators=[
            Regexp(r'[А-ЯЁа-яё]*', message='Отчество должно содержать только кириллические буквы')
        ],
        render_kw={
            'placeholder': 'Иванович'
        }
    )
    phone = TelField(
        label='Телефон* (российский номер)',
        validators=[
            DataRequired(message='Обязательное поле')
        ],
        render_kw={
            'placeholder': '+7 (999) 999-99-99'
        }
    )
    login = StringField(
        label='Логин*',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 30, message='Логин должен содержать %(min)d-%(max)d символов'),
            Regexp(r'[A-Za-z0-9]+', message='Логин должен содержать только латинские буквы и цифры')
        ],
        render_kw={
            'placeholder': 'username'
        }
    )
    password = PasswordField(
        label='Пароль*',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(8, 60, message='Пароль должен содержать %(min)d-%(max)d символов')
        ]
    )
    password_confirm = PasswordField(
        label='Подтвердите пароль*',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(8, 60, message='Пароль должен содержать %(min)d-%(max)d символов'),
            EqualTo('password', message='Пароли должны совпадать')
        ]
    )
    submit = SubmitField('Зарегистрироваться')

    @staticmethod
    def validate_phone(form: Form, field: Field) -> None:
        phone = ''.join(s for s in field.data if s.isdigit())
        if len(phone) < 11:
            raise ValidationError('Номер должен содержать 11 цифр')
        if not phone.startswith(('7', '8')):
            raise ValidationError('Телефон должен начинаться с 7 или 8')
