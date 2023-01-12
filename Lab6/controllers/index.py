from Lab6 import constants
from flask import render_template, Blueprint

blueprint = Blueprint('index', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    html = render_template(
        'index.jinja2',
        len=len,
        program_list=constants.programs,
        subject_list=constants.subjects,
        olimpiad_list=constants.olimpiads
    )
    return html
