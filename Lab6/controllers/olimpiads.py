import constants
from main import app
from flask import render_template, request


@app.route('/olimpiads/<olim>')
def olimpiads(olim):
    html = render_template(
        'olimpiads.jinja2',
        olim=olim,
        description=constants.olimpiads_dict[olim]
    )
    return html
