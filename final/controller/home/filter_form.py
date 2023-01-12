from flask_wtf import FlaskForm
from wtforms import SearchField, SelectMultipleField, IntegerField, FloatField


class FilterForm(FlaskForm):
    class Meta:
        csrf = False

    search = SearchField(
        label='Поиск'
    )
    tags = SelectMultipleField(
        label='Тэги',
        coerce=int
    )
    difficulties = SelectMultipleField(
        label='Сложности',
        coerce=int
    )
    min_rating = IntegerField(
        label='Минимальная оценка',
        name='minRating'
    )
    max_price = FloatField(
        label='Максимальная цена',
        name='maxPrice'
    )
    min_available_reservations = IntegerField(
        label='Количество свободных мест',
        name='minAvailableReservations'
    )
