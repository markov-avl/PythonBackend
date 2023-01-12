import pandas


def get_reader(conn):
    return pandas.read_sql('''
        SELECT * FROM reader
    ''', conn)


def get_book_reader(conn, reader_id):
    return pandas.read_sql('''
        with get_authors(book_id, authors_name) AS (SELECT book_id, GROUP_CONCAT(author_name)
                                                    FROM author
                                                             JOIN book_author USING (author_id)
                                                    GROUP BY book_id)
        SELECT title          AS Название,
               authors_name   AS Авторы,
               borrow_date    AS Дата_выдачи,
               return_date    AS Дата_возврата,
               book_reader_id
        FROM reader
                 JOIN book_reader USING (reader_id)
                 JOIN book USING (book_id)
                 JOIN get_authors USING (book_id)
        WHERE reader.reader_id = :id
        ORDER BY borrow_date
    ''', conn, params={"id": reader_id})


def get_new_reader(conn, new_reader):
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO reader(reader_name) VALUES (:new_reader)
    ''', {"new_reader": new_reader})

    conn.commit()

    return cur.lastrowid


def borrow_book(conn, book_id, reader_id) -> None:
    cur = conn.cursor()

    cur.executescript(f'''
        INSERT INTO book_reader(book_id, reader_id, borrow_date)
            VALUES ({book_id}, {reader_id}, DATE('now'));
        UPDATE book
            SET available_numbers = available_numbers - 1
        WHERE book_id = {book_id}
    ''')

    return conn.commit()


def return_book(conn, book_reader_id) -> None:
    cur = conn.cursor()

    book_id = pandas.read_sql(f'''
        SELECT book_id
        FROM book_reader
        WHERE book_reader_id = :book_reader_id
    ''', conn, params=dict(book_reader_id=book_reader_id)).values[0][0]

    cur.executescript(f'''
        UPDATE book
        SET available_numbers = available_numbers + 1
        WHERE book_id = {book_id};
        
        UPDATE book_reader
        SET return_date = DATE('now')
        WHERE book_reader_id = {book_reader_id}
    ''')

    return conn.commit()
