import sqlite3
# sqlite - .db, .sqlite: вся база SQLite хранится в одном файле, отдельный сервер не нужен.


def create_tables(conn):
    # IF NOT EXISTS - создать таблицу, только если её ещё нет:
    # повторный запуск скрипта не упадёт с ошибкой, что таблица уже существует.
    conn.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        done BOOLEAN
    )
    """) # SQL
    # primary key - первичный ключ: уникальный номер строки, по нему удобно
    # находить, изменять и удалять запись; если id не указать, SQLite назначит его сама.
    # Типа BOOLEAN в SQLite нет: False хранится как 0, True - как 1.

def add_todo(conn, name_param, description_param, done_param):
    print(name_param, description_param, done_param)
    # conn.execute() выполняет SQL-запрос. Знаки ? - места подстановки:
    # вместо них подставляются значения из кортежа, переданного ниже.
    # Данные идут отдельно от текста запроса - это защита от SQL-инъекций.
    conn.execute("""
    INSERT INTO todos (name, description, done)
    VALUES (?, ?, ?)
    """, (name_param, description_param, done_param)
    )
    # commit() сохраняет изменения в файле базы;
    # без него изменения не попадут в файл и пропадут при закрытии соединения.
    conn.commit()


def get_all_todos(conn):
    # result = conn.execute("SELECT * FROM todos")
    # Колонки в кортежах результата идут в порядке из SELECT, а не в порядке таблицы.
    result = conn.execute("SELECT id, done, name FROM todos")
    # to_return = result.fetchall() # все записи
    # to_return = result.fetchone()
    # fetchall() - все строки, fetchone() - первая (или None, если строк нет),
    # fetchmany(3) - не больше 3 строк.
    to_return = result.fetchmany(3)
    return to_return

def delete_todo(conn, todo_id):
    # Без WHERE DELETE удалил бы все строки таблицы.
    # (todo_id,) - кортеж из одного элемента, запятая внутри обязательна.
    conn.execute("""
    DELETE FROM todos WHERE id = ?
    """, (todo_id,)
    )
    conn.commit()

if __name__ == '__main__':
    # connect() открывает базу; если файла database.db ещё нет, он будет создан.
    connection = sqlite3.connect('database.db')
    create_tables(connection)
    # добавление данных
    add_todo(connection, 'магазин', 'сходить в магазин', False)
    add_todo(connection, 'уборка', 'убраться в комнате', False)
    add_todo(connection, 'ДЗ', 'сделать ДЗ', False)

    # получение данных
    all_todos = get_all_todos(connection)
    # print(all_todos)
    for t in all_todos:
        print(t)

    # удаление по id
    delete_todo(connection, 2)

    # Закрываем соединение: к этому моменту все изменения уже сохранены commit().
    connection.close()
