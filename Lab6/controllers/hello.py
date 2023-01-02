import constants
from main import app
from flask import render_template, request


@app.route('/hello', methods=['GET'])
def hello():
    gender = request.values.get('gender')
    name = request.values.get('username')
    program_id = request.values.get('program')
    subject_id = request.values.getlist('subject[]')
    olimpiads_id = request.values.getlist('olimpiads[]')
    olimpiads_select = list(map(lambda i: constants.olimpiads[int(i)], olimpiads_id))
    olimpiads_select = [constants.olimpiads[int(i)] for i in olimpiads_id]
    subjects_select = [constants.subjects[int(i)] for i in subject_id]

    html = render_template(
        'hello.jinja2',
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)],
        subjects_select=subjects_select,
        subject_list=constants.subjects,
        olimpiads_select=olimpiads_select
    )
    return html
