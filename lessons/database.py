import sqlite3
# sqlite - .db, .sqlite


def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        done BOOLEAN
    )
    """) # SQL
    # primary key - первичный ключ

def add_todo(conn, name_param, description_param, done_param):
    print(name_param, description_param, done_param)
    conn.execute("""
    INSERT INTO todos (name, description, done)
    VALUES (?, ?, ?)
    """, (name_param, description_param, done_param)
    )
    conn.commit()


def get_all_todos(conn):
    # result = conn.execute("SELECT * FROM todos")
    result = conn.execute("SELECT id, done, name FROM todos")
    # to_return = result.fetchall() # все записи
    # to_return = result.fetchone()
    to_return = result.fetchmany(3)
    return to_return

def delete_todo(conn, todo_id):
    conn.execute("""
    DELETE FROM todos WHERE id = ?
    """, (todo_id,)
    )
    conn.commit()

if __name__ == '__main__':
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


    delete_todo(connection, 2)

    connection.close()