import sqlite3


def main():
    # создаем базу данных и устанавливаем соединение с ней
    con = sqlite3.connect("library.sqlite")
    # открываем файл с дампом базой двнных
    f_dump = open('library.db', 'r', encoding='utf-8-sig')
    # читаем данные из файла
    dump = f_dump.read()
    # закрываем файл с дампом
    f_dump.close()
    # запускаем запросы
    con.executescript(dump)
    # сохраняем информацию в базе данных
    con.commit()
    # закрываем соединение с базой
    con.close()


if __name__ == '__main__':
    main()
