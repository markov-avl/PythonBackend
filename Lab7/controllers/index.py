from app import app
from flask import render_template, request, session
from connection import get_db_connection
from models.index_model import get_reader, get_book_reader, get_new_reader, borrow_book, return_book


@app.route('/', methods=['get'])
def index():
    conn = get_db_connection()

    if request.values.get('reader'):
        reader_id = int(request.values.get('reader'))
        session['reader_id'] = reader_id
    elif request.values.get('new_reader'):
        new_reader = request.values.get('new_reader')
        session['reader_id'] = get_new_reader(conn, new_reader)
    elif request.values.get('return'):
        book_reader_id = int(request.values.get('return'))
        return_book(conn, book_reader_id)
    elif request.values.get('book'):
        book_id = int(request.values.get('book'))
        borrow_book(conn, book_id, session['reader_id'])
    else:
        session['reader_id'] = 1

    df_reader = get_reader(conn)
    df_book_reader = get_book_reader(conn, session['reader_id'])

    # выводим форму
    html = render_template(
        'index.jinja2',
        reader_id=session['reader_id'],
        combo_box=df_reader,
        book_reader=df_book_reader,
        len=len
    )
    return html
