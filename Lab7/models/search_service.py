from .service import Service


class SearchService(Service):
    def get_publishers(self):
        sql = '''
            SELECT publisher_id, publisher_name, COUNT(book.book_id)
            FROM publisher
                     JOIN book USING (publisher_id)
            GROUP BY publisher_name
        '''
        return self._fetchall(sql)

    def get_genres(self):
        sql = '''
            SELECT genre_id,
                   genre_name,
                   COUNT(book.book_id)
            FROM genre
                     JOIN book USING (genre_id)
            GROUP BY genre_name
        '''
        return self._fetchall(sql)

    def get_authors(self):
        sql = '''
            SELECT author_id,
                   author_name,
                   COUNT(book.book_id)
            FROM author
                     JOIN book_author USING (author_id)
                     JOIN book USING (book_id)
            GROUP BY author_name
        '''
        return self._fetchall(sql)

    def card(self, publishers: list[int], genres: list[int], authors: list[int]):
        publishers = self.__convert(publishers)
        authors = self.__convert(authors)
        genres = self.__convert(genres)

        sql = f'''
            SELECT title AS Название,
                   group_concat(DISTINCT author_name) AS Авторы,
                   genre_name AS Жанр,
                   publisher_name AS Издательство,
                   year_publication AS Год_издания,
                   available_numbers AS Количество,
                   book_id AS ID
            FROM book
                     JOIN genre USING(genre_id)
                     JOIN publisher USING(publisher_id)
                     JOIN book_author USING(book_id)
                     JOIN author USING(author_id)
            GROUP BY book_id
            HAVING (genre_id IN ({genres}) OR ({not genres}))
               AND (publisher_id IN ({publishers}) OR ({not publishers}))
               AND (author_id IN ({authors}) OR ({not authors}))
            ORDER BY title, available_numbers DESC, genre_name, year_publication DESC 
        '''
        return self._fetchall(sql)

    @staticmethod
    def __convert(l: list[int]):
        return ', '.join(map(str, l))
