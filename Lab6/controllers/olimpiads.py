from Lab6 import constants
from flask import render_template, Blueprint

blueprint = Blueprint('olimpiads', __name__)


@blueprint.route('/olimpiads/<olim>')
def index(olim):
    html = render_template(
        'olimpiads.jinja2',
        olim=olim,
        description=constants.olimpiads_dict[olim]
    )
    return html
