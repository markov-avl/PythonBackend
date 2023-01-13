from .service import Service


class ReaderService(Service):
    def get_readers(self):
        sql = '''
            SELECT * FROM reader
        '''
        return self._fetchall(sql)

    def get_reader_books(self, reader_id: int):
        sql = '''
            with authors (book_id, name) AS (SELECT ba.book_id,
                                                    GROUP_CONCAT(a.author_name)
                                             FROM author a
                                                      JOIN book_author ba on ba.author_id = a.author_id
                                             GROUP BY ba.book_id)
            SELECT b.title           AS Название,
                   a.name            AS Авторы,
                   br.borrow_date    AS Дата_выдачи,
                   br.return_date    AS Дата_возврата,
                   br.book_reader_id
            FROM reader r
                     JOIN book_reader br on br.reader_id = r.reader_id
                     JOIN book b on b.book_id = br.book_id
                     JOIN authors a on a.book_id = b.book_id
            WHERE r.reader_id = ?
            ORDER BY br.borrow_date
        '''
        return self._fetchall(sql, (reader_id,))

    def add_reader(self, reader_name: str) -> int:
        sql = '''
            INSERT INTO reader (reader_name) VALUES (?)
        '''
        return self._insert(sql, (reader_name,))

    def borrow_book(self, book_id: int, reader_id: int) -> None:
        sql = '''
            INSERT INTO book_reader (book_id, reader_id, borrow_date)
            VALUES (?, ?, DATE('now'))
        '''
        self._insert(sql, (book_id, reader_id))
        self._dec_available_numbers(book_id)

    def return_book(self, book_reader_id: int) -> None:
        sql = '''
            SELECT book_id
            FROM book_reader
            WHERE book_reader_id = ?
        '''
        book_id = self._fetchone(sql, (book_reader_id,))[0][0]
        self._inc_available_numbers(book_id)

        sql = '''
            UPDATE book_reader
            SET return_date = DATE('now')
            WHERE book_reader_id = ?
        '''
        self._update(sql, (book_reader_id,))

    def _inc_available_numbers(self, book_id: int) -> None:
        sql = '''
            UPDATE book
            SET available_numbers = available_numbers + 1
            WHERE book_id = ?
        '''
        self._update(sql, (book_id,))

    def _dec_available_numbers(self, book_id: int) -> None:
        sql = '''
            UPDATE book
            SET available_numbers = available_numbers - 1
            WHERE book_id = ?
        '''
        self._update(sql, (book_id,))
