from app import app
from flask import render_template


@app.route('/statistics', methods=['get'])
def statistics():
    html = render_template(
        'statistics.jinja2',
    )
    return html
