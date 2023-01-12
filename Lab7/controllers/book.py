from flask import render_template, Blueprint

from .method import Method

blueprint = Blueprint('book', __name__)


@blueprint.route('/book', methods=[Method.GET])
def index():
    html = render_template('book.jinja2')
    return html
