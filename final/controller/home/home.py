from flask import render_template, Blueprint, request

from .filter_form import FilterForm
from final.controller.method import Method
from final.model import TagService, DifficultyService, OfferService

blueprint = Blueprint('index', __name__)
tag_service = TagService()
difficulty_service = DifficultyService()
offer_service = OfferService()


@blueprint.route('/', methods=[Method.GET])
def index():
    filter_form = FilterForm(request.args)

    tags = tag_service.get_all_with_count()
    difficulties = difficulty_service.get_all_with_count_ordered_by_rating()

    offers = offer_service.get_all_previews()
    offer_prices = [offer.price for offer in offers]
    offer_available_reservations = [offer.available_reservations for offer in offers]

    offers = offer_service.get_all_previews(filter_form.search.data,
                                            filter_form.tags.data,
                                            filter_form.difficulties.data,
                                            filter_form.min_rating.data,
                                            filter_form.max_price.data,
                                            filter_form.min_available_reservations.data)

    return render_template(
        'page/index.jinja2',
        filter_form=filter_form,
        tags=tags,
        difficulties=difficulties,
        offers=offers,
        min_price=min(offer_prices) if offer_prices else None,
        max_price=max(offer_prices) if offer_prices else None,
        min_available_reservations=min(offer_available_reservations) if offer_available_reservations else None,
        max_available_reservations=max(offer_available_reservations) if offer_available_reservations else None
    )
