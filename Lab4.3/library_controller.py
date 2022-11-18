import sqlite3
from jinja2 import Template
from library_model import *

GENRES = ['Детектив', 'Приключения', 'Роман']
AUTHORS = ['Агата Кристи', 'Жюль Верн', 'Ильф И.А.', 'Петров Е.П.']
PUBLISHERS = ['ПИТЕР']

if __name__ == '__main__':
    conn = sqlite3.connect('../library.sqlite')
    form_groups = [
        ('Жанр', get_genre(conn), GENRES),
        ('Автор', get_author(conn), AUTHORS),
        ('Издательство', get_publisher(conn), PUBLISHERS)
    ]
    cards = get_cards(conn, GENRES, AUTHORS, PUBLISHERS)
    conn.close()

    with open('library_template.jinja2', 'r', encoding='utf-8-sig') as infile:
        template = Template(infile.read())

    library_html = template.render(
        form_groups=form_groups,
        cards=cards,
        has_filters=any(form_group[2] for form_group in form_groups),
        join=lambda l: ', '.join(l),
        len=len
    )

    with open('library.html', 'w', encoding='utf-8-sig') as outfile:
        outfile.write(library_html)
