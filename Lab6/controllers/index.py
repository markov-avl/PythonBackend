from Lab6 import constants
from flask import render_template, Blueprint, request

blueprint = Blueprint('index', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    if request.values.get('clear'):
        gender = None
        name = None
        program_id = None
        subject_id = []
        olimpiads_id = []
    else:
        gender = request.values.get('gender')
        name = request.values.get('username')
        program_id = request.values.get('program')
        subject_id = list(map(int, request.values.getlist('subject')))
        olimpiads_id = list(map(int, request.values.getlist('olimpiads')))

    subjects_selected = [constants.subjects[i] for i in subject_id]
    olimpiads_selected = [constants.olimpiads[i] for i in olimpiads_id]

    html = render_template(
        'index.jinja2',
        len=len,
        program_list=constants.programs,
        subject_list=constants.subjects,
        olimpiad_list=constants.olimpiads,
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)] if program_id else None,
        subjects_selected=subjects_selected,
        olimpiads_selected=olimpiads_selected,
        subject_selected_ids=subject_id,
        olimpiads_selected_ids=olimpiads_id
    )
    return html
