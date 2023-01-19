from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField


class ReservationForm(FlaskForm):
    class Meta:
        csrf = False

    offer_id = IntegerField(
        name='offerId'
    )
    available_reservations = IntegerField(
        label='Количество мест',
        name='availableReservations'
    )
    submit = SubmitField('Забронировать')
