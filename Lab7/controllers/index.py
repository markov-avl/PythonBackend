from flask import render_template, request, session, Blueprint

from Lab7.models import ReaderService

from .method import Method

blueprint = Blueprint('index', __name__)
reader_service = ReaderService()


@blueprint.route('/', methods=[Method.GET])
def index():
    if request.values.get('reader'):
        reader_id = int(request.values.get('reader'))
        session['reader_id'] = reader_id
    elif request.values.get('new_reader'):
        new_reader = request.values.get('new_reader')
        session['reader_id'] = reader_service.add_reader(new_reader)
    elif request.values.get('return'):
        book_reader_id = int(request.values.get('return'))
        reader_service.return_book(book_reader_id)
    elif request.values.get('book'):
        book_id = int(request.values.get('book'))
        reader_service.borrow_book(book_id, session['reader_id'])
    else:
        session['reader_id'] = 1

    df_reader = reader_service.get_readers()
    df_book_reader = reader_service.get_reader_books(session['reader_id'])

    # выводим форму
    html = render_template(
        'index.jinja2',
        reader_id=session['reader_id'],
        combo_box=df_reader,
        book_reader=df_book_reader,
        len=len
    )
    return html
