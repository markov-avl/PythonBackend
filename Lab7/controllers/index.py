from flask import render_template, request, session, Blueprint

from Lab7 import database
from Lab7.models import index_service

from .method import Method

blueprint = Blueprint('index', __name__)


@blueprint.route('/', methods=[Method.GET])
def index():
    conn = database.get_connection()

    if request.values.get('reader'):
        reader_id = int(request.values.get('reader'))
        session['reader_id'] = reader_id
    elif request.values.get('new_reader'):
        new_reader = request.values.get('new_reader')
        session['reader_id'] = index_service.get_new_reader(conn, new_reader)
    elif request.values.get('return'):
        book_reader_id = int(request.values.get('return'))
        index_service.return_book(conn, book_reader_id)
    elif request.values.get('book'):
        book_id = int(request.values.get('book'))
        index_service.borrow_book(conn, book_id, session['reader_id'])
    else:
        session['reader_id'] = 1

    df_reader = index_service.get_reader(conn)
    df_book_reader = index_service.get_book_reader(conn, session['reader_id'])

    # выводим форму
    html = render_template(
        'index.jinja2',
        reader_id=session['reader_id'],
        combo_box=df_reader,
        book_reader=df_book_reader,
        len=len
    )
    return html
