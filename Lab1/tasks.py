import sqlite3

import pandas as pd


def task1(con: sqlite3.Connection) -> None:
    """
    Для каждого жанра посчитать, сколько различных книг этого жанра представлено в
    библиотеке, каково общее количество доступных экземпляров книг (имеющихся в наличии)
    и какой самый ранний год издания книг, относящихся к этому жанру. Информацию
    отсортировать по названию жанра в алфавитном порядке
    """
    print(pd.read_sql("""
        SELECT g.genre_name, COUNT(b.book_id) AS count, min(b.year_publication) AS year
        FROM book b
            JOIN genre g ON b.genre_id = g.genre_id
        GROUP BY b.genre_id
        ORDER BY g.genre_name
    """, con=con))


def task2(con: sqlite3.Connection, reader_name: str) -> None:
    """
    Вывести информацию о всех книгах, который сдал заданный читатель. Для каждой
    книги указать дату выдачи, дату сдачи и сколько дней книга была на руках. Информацию
    отсортировать по убыванию количества дней.
    """
    print(pd.read_sql("""
        SELECT
            b.title                                                            AS book,
            br.borrow_date,
            br.return_date,
            CAST(julianday(br.return_date) - julianday(br.borrow_date) AS INT) AS days
        FROM book_reader br
            JOIN book b ON br.book_id = b.book_id
            JOIN reader r ON br.reader_id = r.reader_id
        WHERE r.reader_name = :reader_name
          AND br.return_date IS NOT NULL
        ORDER BY days DESC
    """, con=con, params={'reader_name': reader_name}))


def task3(con: sqlite3.Connection) -> None:
    """
    Вывести самый популярный жанр (жанры). Самым популярным считается жанр,
    книги которого чаще всего брали читатели в библиотеке. Вывести название жанра (жанров) и
    сколько раз читатели брали книги этого жанра. Информацию отсортировать по названию
    жанров в алфавитном порядке.
    """
    print(pd.read_sql("""
        WITH most_popular AS (SELECT MAX(count) AS max
                              FROM (SELECT COUNT(b.book_id) AS count
                                    FROM genre g
                                        JOIN book b ON b.genre_id = g.genre_id
                                        JOIN book_reader br ON br.book_id = b.book_id
                                    GROUP BY g.genre_id))
        SELECT g.genre_name, COUNT(b.book_id) AS count
        FROM genre g, most_popular
            JOIN book b ON b.genre_id = g.genre_id
            JOIN book_reader br ON br.book_id = b.book_id
        GROUP BY g.genre_id
        HAVING count = most_popular.max
        ORDER BY g.genre_name
    """, con=con))


def task4(con: sqlite3.Connection) -> None:
    """
    Вывести книги, которые были взяты в библиотеке в октябре месяце. Указать
    фамилии читателей, которые их взяли, а также дату, когда их взяли. Столбцы назвать
    Название, Читатель, Дата соответственно. Информацию отсортировать сначала по
    возрастанию даты, потом в алфавитном порядке по фамилиям читателей, и, наконец, по
    названиям книг тоже в алфавитном порядке.
    """
    print(pd.read_sql("""
        SELECT b.title AS Название, r.reader_name AS Читатель, br.borrow_date AS Дата
        FROM book b
            JOIN book_reader br ON br.book_id = b.book_id
            JOIN reader r ON r.reader_id = br.reader_id = r.reader_id
        WHERE strftime('%m', br.borrow_date) = '10'
        ORDER BY br.borrow_date, r.reader_name, b.title
    """, con=con))


def task5(con: sqlite3.Connection) -> None:
    """
    Для каждой книги, изданной в заданном издательстве, вывести информацию о ее
    принадлежности к группе:
    - если книга издана раньше 2014 года, вывести "III";
    - если книга издана в период с 2014 года по 2017 год, вывести "II";
    - если книга издана позже 2017 года, вывести "I".
    """
    print(pd.read_sql("""
        SELECT b.title,
               CASE
                   WHEN b.year_publication < 2014 THEN 'III'
                   WHEN b.year_publication > 2017 THEN 'I'
                   ELSE 'II'
               END AS 'group'
        FROM book b
    """, con=con))


def task6(con: sqlite3.Connection) -> None:
    """
    Для каждой книги также указать ее жанр и год издания. Столбцы назвать
    Название, Жанр, Год, Группа. Информацию отсортировать сначала по группе в
    порядке убывания, потом возрастанию года издания и, наконец, по названию в алфавитном
    порядке.
    """
    print(pd.read_sql("""
        SELECT b.title                                       AS Название,
               g.genre_name                                  AS Жанр,
               b.year_publication                            AS Год,
               CASE
                   WHEN b.year_publication < 2014 THEN 'III'
                   WHEN b.year_publication > 2017 THEN 'I'
                   ELSE 'II'
               END                                           AS Группа
        FROM book b
            JOIN genre g ON g.genre_id = b.genre_id
        ORDER BY Группа DESC, Год, Название                                                          
    """, con=con))


def task7(con: sqlite3.Connection) -> None:
    """
    Для каждой книги вывести количество экземпляров, которые есть в наличии
    (available_numbers) в библиотеке, а также сколько раз экземпляры книги брали
    читатели. Если книгу читатели не брали - вывести 0. Столбцы назвать Название,
    Количество, Количество_выдачи. Информацию отсортировать сначала по убыванию
    количества выданных экземпляров, а потом по названию книги в алфавитном порядке и,
    наконец, по возрастанию доступного количества.
    """
    print(pd.read_sql("""
        SELECT b.title             AS Название,
               b.available_numbers AS Количество,
               COUNT(br.book_id)   AS Количество_выдачи
        FROM book b
            LEFT JOIN book_reader br ON br.book_id = b.book_id
        GROUP BY b.book_id
        ORDER BY Количество_выдачи DESC, Название, Количество
    """, con=con))


def main() -> None:
    con = sqlite3.connect("../library.sqlite")
    tasks = [
        lambda connection: task1(connection),
        lambda connection: task2(connection, 'Петров Ф.С.'),
        lambda connection: task3(connection),
        lambda connection: task4(connection),
        lambda connection: task5(connection),
        lambda connection: task6(connection),
        lambda connection: task7(connection)
    ]
    for i, task in enumerate(tasks):
        print('-' * 50 + f' Task {i + 1} ' + '-' * 50)
        task(con)
    con.close()


if __name__ == '__main__':
    main()
