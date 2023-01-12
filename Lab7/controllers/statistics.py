from flask import render_template, Blueprint

from .method import Method

blueprint = Blueprint('statistics', __name__)


@blueprint.route('/statistics', methods=[Method.GET])
def index():
    html = render_template('statistics.jinja2')
    return html
