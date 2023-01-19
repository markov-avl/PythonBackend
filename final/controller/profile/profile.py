import datetime

from flask import render_template, Blueprint, session, redirect, url_for

from final.controller.method import Method
from final.model import UserService, ReservationService
from final.model.entity import ReservationDetailedInfo
from final.model.reservation_status import ReservationStatus

blueprint = Blueprint('profile', __name__)
user_service = UserService()
reservation_service = ReservationService()


@blueprint.route('/profile', methods=[Method.GET])
def index():
    if not (user := user_service.get_by_login(session.get('login', None))):
        return redirect(url_for('index.index'))

    reservations = reservation_service.get_detailed_info_by_user_id(user.id)
    now = datetime.datetime.now()

    return render_template(
        'page/profile.jinja2',
        user=user,
        current_reservations=list(filter(lambda r: is_current_reservation(r, now), reservations)),
        past_reservations=list(filter(lambda r: not is_current_reservation(r, now), reservations)),
        status=ReservationStatus
    )


def is_current_reservation(reservation: ReservationDetailedInfo, now: datetime.datetime) -> bool:
    return reservation.offer_ending_at > now and \
        reservation.status in (ReservationStatus.PAID, ReservationStatus.ACCEPTED)
