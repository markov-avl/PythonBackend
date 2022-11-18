from jinja2 import Template
import sqlite3
from library_model import get_reader, get_book_reader

if __name__ == '__main__':
    reader_id = 3

    conn = sqlite3.connect('../library.sqlite')
    df_reader = get_reader(conn)
    df_book_reader = get_book_reader(conn, reader_id)
    conn.close()

    with open('library_template.jinja2', 'r', encoding='utf-8-sig') as infile:
        template = Template(infile.read())

    library_html = template.render(
        reader_id=reader_id,
        combo_box=df_reader,
        book_reader=df_book_reader,
        len=len
    )

    with open('library.html', 'w', encoding='utf-8-sig') as outfile:
        outfile.write(library_html)
