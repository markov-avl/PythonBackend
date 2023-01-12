from Lab6 import constants
from flask import render_template, Blueprint

blueprint = Blueprint('subject', __name__)


@blueprint.route('/subject/<sub>')
def index(sub):
    html = render_template(
        'subject.jinja2',
        sub=sub,
        description=constants.subject_dict[sub]
    )
    return html
