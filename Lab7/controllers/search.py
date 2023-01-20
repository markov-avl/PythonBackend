from flask import render_template, request, Blueprint

from Lab7.models import SearchService

from .method import Method

blueprint = Blueprint('search', __name__)
search_service = SearchService()


@blueprint.route('/search', methods=[Method.GET, Method.POST])
def index():
    authors = search_service.get_authors()
    publishers = search_service.get_publishers()
    genres = search_service.get_genres()

    if request.form.get('clear'):
        selected_genres = []
        selected_publishers = []
        selected_authors = []
    else:
        selected_genres = list(map(int, request.form.getlist('genre_id')))
        selected_publishers = list(map(int, request.form.getlist('publisher_id')))
        selected_authors = list(map(int, request.form.getlist('author_id')))

    cards = search_service.get_cards(selected_genres, selected_publishers, selected_authors)

    html = render_template(
        'search.jinja2',
        authors=authors,
        publishers=publishers,
        genres=genres,
        cards=cards,
        selected_authors=selected_authors,
        selected_publishers=selected_publishers,
        selected_genres=selected_genres,
        len=len
    )
    return html
