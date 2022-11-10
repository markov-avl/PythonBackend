import sqlite3
from jinja2 import Template
from library_model import *

if __name__ == '__main__':
    conn = sqlite3.connect('../library.sqlite')
    dataframes = [
        ('publisher', get_publisher(conn)),
        ('genre', get_genre(conn)),
        ('reader', get_reader(conn)),
        ('author', get_author(conn)),
        ('book_author', get_book_author(conn)),
        ('book', get_book(conn)),
        ('book_reader', get_book_reader(conn)),
    ]
    conn.close()

    with open('library_template.jinja2', 'r', encoding='utf-8-sig') as infile:
        template = Template(infile.read())

    library_html = template.render(
        dataframes=dataframes,
        len=len
    )

    with open('library.html', 'w', encoding='utf-8-sig') as outfile:
        outfile.write(library_html)
