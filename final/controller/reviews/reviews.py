from flask import Blueprint, request, redirect, url_for

from .review_form import ReviewForm
from final.controller.method import Method
from final.model import ReviewService

blueprint = Blueprint('reviews', __name__)
review_service = ReviewService()


@blueprint.route('/reviews', methods=[Method.POST])
def create():
    review_form = ReviewForm(request.form)

    if review_form.validate_on_submit():
        review_service.create(review_form.reservation_id.data, review_form.rating.data, review_form.comment.data)

    return redirect(url_for('profile.index'))
