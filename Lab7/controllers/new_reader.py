from flask import render_template, Blueprint

from .method import Method

blueprint = Blueprint('new_reader', __name__)


@blueprint.route('/new_reader', methods=[Method.GET])
def index():
    html = render_template('new_reader.jinja2')
    return html
