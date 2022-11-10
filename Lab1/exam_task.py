import sqlite3

import pandas as pd


def task(con: sqlite3.Connection) -> None:
    """
    Каждому пользователю библиотеки определить его рейтинг:
    - Если у него все книжки сданы, и он держал их не более 14 дней, то ему начисислить 5 баллов за каждую книжку.
    - Если он всё сдал, но держал более 14 дней хотя бы одну книгу, то ему начислить 3 балла за каждую книгу.
    - Если у него есть несданные книги, то поставить ему один балл.
    """
    print(pd.read_sql("""
        SELECT
            r.reader_name AS Читатель,
            CASE
                WHEN NOT EXISTS(SELECT *
                                FROM book_reader br1
                                WHERE br1.reader_id = r.reader_id
                                  AND br1.return_date IS NOT NULL
                                  AND CAST(julianday(br1.return_date) - julianday(br1.borrow_date) AS INT) <= 14)
                     THEN COUNT(br.book_reader_id) * 5
                WHEN NOT EXISTS(SELECT *
                                FROM book_reader br1
                                WHERE br1.reader_id = r.reader_id
                                  AND br1.return_date IS NULL)
                     THEN COUNT(br.book_reader_id) * 3
                ELSE 1
            END           AS Рейтинг
        FROM reader r
            LEFT JOIN book_reader br ON br.reader_id = r.reader_id
        GROUP BY r.reader_id
    """, con=con))


def main() -> None:
    con = sqlite3.connect("../library.sqlite")
    task(con)
    con.close()


if __name__ == '__main__':
    main()
