import datetime

from flask import render_template, Blueprint, abort

from final.controller.method import Method
from final.controller.reservations import ReservationForm
from final.model import OfferService, DifficultyService, ReviewService

blueprint = Blueprint('offers', __name__)
difficulty_service = DifficultyService()
review_service = ReviewService()
offer_service = OfferService()


@blueprint.route('/offers/<int:id_>', methods=[Method.GET])
def offer_by_id(id_: int):
    offer = offer_service.get_detailed_info_by_id(id_)

    if not offer:
        abort(404)

    form = ReservationForm()
    difficulties = difficulty_service.get_all()
    reviews = review_service.get_by_offer_id_ordered_by_created_at_desc(id_)

    difficulty_ratings = [difficulty.rating for difficulty in difficulties]

    return render_template(
        'page/offer.jinja2',
        form=form,
        offer=offer,
        reviews=reviews,
        max_difficulty_rating=max(difficulty_ratings) if difficulty_ratings else None,
        now=datetime.datetime.now()
    )
