import mysql
from mysql.connector import errorcode
from aiogram.types import Message

# import config_bot


def conn(password: str, user: str, database='tg_bot', host='127.0.0.1'):
    connection = None
    try:
        connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
        print(f'Database {connection.database} is connected.')
    except mysql.connector.Error as err:
        print(f'Error {err}')

    if connection:
        return connection


def get_execute(connection: mysql.connector.connection, query: str):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print(cursor.fetchall())
        connection.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Что-то не так с логином или паролем...')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Что-то не так с бд...')
        else:
            print(err)
    else:
        connection.close()


def db_start(connection: mysql.connector.connection, message: Message):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO users(FirstName, LastName, UserName, IsBot) VALUES("{message.from_user.first_name}", "{message.from_user.last_name}", "{message.from_user.username}", "{message.from_user.is_bot}")')
        connection.commit()
    except mysql.connector.Error as err:
        print(f'Error {err}')
    finally:
        connection.close()
    return cursor.description

def add_location(connection, message: Message):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO locations(Coordinates, Date, fk_users_locations) VALUES("{message.location.longitude, message.location.latitude}", NOW(), (SELECT id FROM users WHERE FirstName in ("{message.from_user.first_name}")));')
        connection.commit()
    except mysql.connector.Error as err:
        print(f'Error {err}')
