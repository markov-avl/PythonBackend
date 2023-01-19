from flask import Blueprint, abort, redirect, url_for, request, session, render_template

from .reservation_form import ReservationForm
from final.controller.method import Method
from final.model import ReservationService
from final.model.reservation_status import ReservationStatus

blueprint = Blueprint('reservations', __name__)
reservation_service = ReservationService()


@blueprint.route('/reservations', methods=[Method.POST])
def create():
    form = ReservationForm(request.form)

    if session.get('id', None) and form.validate_on_submit():
        reservation_service.create(form.offer_id.data, int(session['id']), form.available_reservations.data)

    return redirect(url_for('profile.index'))


@blueprint.route('/reservations/pending', methods=[Method.GET])
def pending():
    if not session.get('is_admin', None):
        abort(404)

    pending_reservations = reservation_service.get_pending()

    return render_template(
        'page/pending.jinja2',
        reservations=pending_reservations,
        status=ReservationStatus
    )


@blueprint.route('/reservations/<int:id_>', methods=[Method.POST])
def change_status(id_: int):
    reservation_service.update_status(id_, ReservationStatus.from_id(int(request.form.get('status'))))
    return redirect(request.values.get('redirect', url_for('index.index')))
