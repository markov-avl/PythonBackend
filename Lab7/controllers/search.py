from flask import render_template, request, Blueprint

from Lab7.models import SearchService

from .method import Method

blueprint = Blueprint('search', __name__)
search_service = SearchService()


@blueprint.route('/search', methods=[Method.GET, Method.POST])
def index():
    df_authors = search_service.get_authors()
    df_publishers = search_service.get_publishers()
    df_genres = search_service.get_genres()

    if request.form.get('clear'):
        genres = []
        publishers = []
        authors = []
    else:
        genres = list(map(int, request.form.getlist('genre_id')))
        publishers = list(map(int, request.form.getlist('publisher_id')))
        authors = list(map(int, request.form.getlist('author_id')))

    df_card = search_service.card(publishers, genres, authors)

    html = render_template(
        'search.jinja2',
        authors=df_authors,
        publishers=df_publishers,
        genres=df_genres,
        card=df_card,
        sel_authors=authors,
        sel_publishers=publishers,
        sel_genres=genres,
        len=len
    )
    return html
