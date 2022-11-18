import pandas as pd


def get_reader(conn):
    return pd.read_sql(f'SELECT * FROM reader', conn)


def get_book_reader(conn, reader_id: int):
    return pd.read_sql(f'SELECT b.title AS Названия,'
                       f'       p.publisher_name AS Авторы,'
                       f'       br.borrow_date AS Дата_выдачи,'
                       f'       br.return_date AS Дата_сдачи '
                       f'FROM book_reader br '
                       f'    JOIN book b ON b.book_id = br.book_id '
                       f'    JOIN publisher p on p.publisher_id = b.publisher_id '
                       f'WHERE reader_id = :reader_id',
                       conn,
                       params=dict(reader_id=reader_id))
