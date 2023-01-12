from flask import render_template, request, Blueprint

from Lab7 import database
from Lab7.models import search_service

from .method import Method

blueprint = Blueprint('search', __name__)


@blueprint.route('/search', methods=[Method.GET, Method.POST])
def index():
    conn = database.get_connection()
    df_author = search_service.get_author(conn)
    df_publisher = search_service.get_publisher(conn)
    df_genre = search_service.get_genre(conn)

    if request.form.get('clear'):
        genres = []
        publishers = []
        authors = []
    else:
        genres = [int(item) for item in request.form.getlist('genre_id')]
        publishers = [int(item) for item in request.form.getlist('publisher_id')]
        authors = [int(item) for item in request.form.getlist('author_id')]

    df_card = search_service.card(conn, publishers, genres, authors)

    html = render_template(
        'search.jinja2',
        authors=df_author,
        publishers=df_publisher,
        genres=df_genre,
        card=df_card,
        sel_authors=authors,
        sel_publishers=publishers,
        sel_genres=genres,
        len=len
    )
    return html
