import pandas as pd


def get_genre(conn):
    return pd.read_sql(f'SELECT g.genre_name AS name, COUNT(b.book_id) AS count '
                       f'FROM genre g '
                       f'JOIN book b ON g.genre_id = b.genre_id '
                       f'GROUP BY g.genre_id',
                       conn)


def get_author(conn):
    return pd.read_sql(f'SELECT a.author_name AS name, COUNT(b.book_id) AS count '
                       f'FROM author a '
                       f'JOIN book_author ba ON a.author_id = ba.author_id '
                       f'JOIN book b on b.book_id = ba.book_id '
                       f'GROUP BY a.author_id',
                       conn)


def get_publisher(conn):
    return pd.read_sql(f'SELECT p.publisher_name AS name, COUNT(b.book_id) AS count '
                       f'FROM publisher p '
                       f'JOIN book b on p.publisher_id = b.publisher_id '
                       f'GROUP BY p.publisher_id',
                       conn)


def get_cards(conn, genres: list[str], authors: list[str], publishers: list[str]):
    where = []
    if genres:
        where.append(f'''g.genre_name IN ('{"', '".join(genres)}')''')
    if authors:
        where.append(f'''a.author_name IN ('{"', '".join(authors)}')''')
    if publishers:
        where.append(f'''p.publisher_name IN ('{"', '".join(publishers)}')''')

    filters = f'WHERE {" AND ".join(where)} ' if where else ''

    return pd.read_sql(f'SELECT b.title AS Название,'
                       f'       GROUP_CONCAT(a.author_name, ", ") AS Авторы,'
                       f'       g.genre_name AS Жанр,'
                       f'       p.publisher_name AS Издательство,'
                       f'       b.year_publication AS Год_издания, '
                       f'       b.available_numbers AS Количество '
                       f'FROM book b '
                       f'    JOIN book_author ba on b.book_id = ba.book_id '
                       f'    JOIN author a on a.author_id = ba.author_id '
                       f'    JOIN publisher p on p.publisher_id = b.publisher_id '
                       f'    JOIN genre g on g.genre_id = b.genre_id '
                       f'{filters}'
                       f'GROUP BY b.book_id',
                       conn)
