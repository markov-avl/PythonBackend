from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class ReviewForm(FlaskForm):
    class Meta:
        csrf = False

    reservation_id = IntegerField(
        label='Комментарий',
        name='reservationId'
    )
    comment = StringField(
        label='Комментарий'
    )
    rating = IntegerField(
        label='Оценка'
    )
    submit = SubmitField('Отправить')
