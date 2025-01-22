import psycopg2


def test_database_connection():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )
    assert conn is not None

def test_data_insertion():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE users
    (
        id INT primary key,
        name VARCHAR
    )
    """)
    conn.commit()
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result[1] == 'John'

def test_data_update():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE users
        SET name = 'Poll' 
        WHERE id = 1
    """)
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE id=1")
    conn.commit()
    result = cursor.fetchone()
    assert result[1] == 'Poll'

def test_data_select():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    conn.commit()
    cursor.execute("SELECT name FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result[0] == 'Poll'


def test_data_delete():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=1")
    conn.commit()
    cursor.execute("SELECT name FROM users WHERE id=1")
    conn.commit()
    result = cursor.fetchone()
    cursor.execute("""
                         DROP TABLE users
                         """)
    conn.commit()
    assert result is None


