import sqlite3

import pandas as pd


def query1(con: sqlite3.Connection) -> None:
    """
    Вывести названия туров и их сложность в порядке возрастания сложности, кроме сложности с id, равному 1.
    """
    print(pd.read_sql("""
        SELECT t.name AS 'Название тура', d.name AS Сложность
        FROM tour t 
            INNER JOIN difficulty d ON d.id = t.difficulty_id
        WHERE d.id != 1
        ORDER BY d.rating
    """, con=con))


def query2(con: sqlite3.Connection) -> None:
    """
    Вывести названия туров, имеющих хотя бы одну наихудшую оценку, в порядке убывания цены.
    """
    print(pd.read_sql("""
        SELECT t.name AS 'Название тура', o.price AS 'Цена тура'
        FROM tour t
            INNER JOIN offer o ON t.id = o.tour_id
            INNER JOIN reservation r ON o.id = r.offer_id
            INNER JOIN review r2 ON r.id = r2.reservation_id AND r2.rating = 1
        ORDER BY o.price DESC
    """, con=con))


def query3(con: sqlite3.Connection) -> None:
    """
    Вывести средние оценки за каждый тур.
    """
    print(pd.read_sql("""
        SELECT t.name AS 'Название тура', AVG(r2.rating) AS 'Средняя оценка'
        FROM tour t
            LEFT JOIN offer o on t.id = o.tour_id
            LEFT JOIN reservation r on o.id = r.offer_id
            LEFT JOIN review r2 on r.id = r2.reservation_id
        GROUP BY t.id
    """, con=con))


def query4(con: sqlite3.Connection) -> None:
    """
    Вывести количество "ночных" туров.
    """
    print(pd.read_sql("""
        SELECT COUNT(DISTINCT t.id) AS Количество
        FROM tour t 
            LEFT JOIN tour_tag tt on t.id = tt.tour_id
            LEFT JOIN tag t2 on t2.id = tt.tag_id
        WHERE t2.name = 'Ночные'
        GROUP BY tt.tag_id
    """, con=con))


def query5(con: sqlite3.Connection) -> None:
    """
    Вывести самые высокие горы.
    """
    print(pd.read_sql("""
        SELECT m.name AS 'Название горы', m.height AS 'Высота'
        FROM mountain m
        WHERE m.height = (SELECT MAX(m2.height)
                          FROM mountain m2)
    """, con=con))


def query6(con: sqlite3.Connection) -> None:
    """
    Вывести горы, для которых туров ещё не создано, в порядке возрастания высоты горы.
    """
    print(pd.read_sql("""
        SELECT m.name AS 'Название горы', m.height AS Высота
        FROM mountain m
        WHERE (SELECT COUNT(*)
               FROM tour t
               WHERE t.mountain_id = m.id) = 0
        ORDER BY m.height
    """, con=con))


def query7(con: sqlite3.Connection) -> None:
    """
    Удалить горы, для которых ещё не создано туров.
    """
    con.execute("""
        DELETE FROM mountain
        WHERE (SELECT COUNT(*)
               FROM tour t
               WHERE t.mountain_id = mountain.id) = 0
    """)


def query8(con: sqlite3.Connection) -> None:
    """
    Уменьшить все цены на предложения на 1000 рублей.
    """
    con.execute("""
        UPDATE offer
        SET offer.price = offer.price - 1000
    """)


def main() -> None:
    con = sqlite3.connect("../final/climbing-club.sqlite")
    queries = [
        query1,
        query2,
        query3,
        query4,
        query5,
        query6,
        query7,
        query8
    ]
    for i, query in enumerate(queries):
        print(f'{i + 1}. {query.__doc__.strip()}')
        query(con)
        print()
    con.close()


if __name__ == '__main__':
    main()
