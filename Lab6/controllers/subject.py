import constants
from main import app
from flask import render_template


@app.route('/subject/<sub>')
def subject(sub):
    html = render_template(
        'subject.jinja2',
        sub=sub,
        description=constants.subject_dict[sub]
    )
    return html
