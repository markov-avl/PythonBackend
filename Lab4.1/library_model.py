import pandas as pd

LIMIT = 11


def get_publisher(conn, limit=LIMIT):
    return pd.read_sql(f'SELECT * FROM publisher LIMIT {limit}', conn)


def get_genre(conn, limit=LIMIT):
    return pd.read_sql(f'SELECT * FROM genre LIMIT {limit}', conn)


def get_reader(conn, limit=LIMIT):
    return pd.read_sql(f'SELECT * FROM reader LIMIT {limit}', conn)


def get_author(conn, limit=LIMIT):
    return pd.read_sql(f'SELECT * FROM author LIMIT {limit}', conn)


def get_book_author(conn, limit=LIMIT):
    return pd.read_sql(f'SELECT * FROM book_author LIMIT {limit}', conn)


def get_book(conn, limit=LIMIT):
    return pd.read_sql(f'SELECT * FROM book LIMIT {limit}', conn)


def get_book_reader(conn, limit=LIMIT):
    return pd.read_sql(f'SELECT * FROM book_reader LIMIT {limit}', conn)
