from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField


class ReservationForm(FlaskForm):
    available_reservations = IntegerField(
        label='Количество мест',
        name='availableReservations'
    )
    submin = SubmitField('Забронировать')
