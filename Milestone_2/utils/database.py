import logging
from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a list.
"""
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    filename='booksApp.log',
    level=logging.DEBUG
)
# books = list()
db_name = 'Books.db'


def aud(qry):
    with DatabaseConnection(db_name) as cnn:
        cursor = cnn.cursor()
        cursor.execute(qry)
    # with sqlite3.connect(db_name) as cnn:


def fetch(qry):
    with DatabaseConnection(db_name) as cnn:
        cursor = cnn.cursor()
        cursor.execute(qry)
        return cursor.fetchall()
    # with sqlite3.connect(db_name) as cnn:


def create_table_book():
    qry = "CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)"
    # creating a table
    aud(qry)
    logging.info('Table Created if Not Exists')


def add_book(name, author):
    qry = f"INSERT INTO books VALUES('{name}','{author}',0)"
    # Inserting Data into a table
    aud(qry)
    logging.info('Adding new Book\'s details')


def get_all_books():
    qry = "SELECT * FROM books"
    # Retriving Data from the table
    data = fetch(qry)
    logging.debug("Retriving Data From Table")
    return [{'name': row[0], 'author':row[1], 'read':row[2]} for row in data]


def remove_book(name):
    qry = f"DELETE FROM books WHERE name='{name}'"
    # Deleting Records
    aud(qry)
    logging.critical("Deleteing some records.")


def mark_readed_book(name):
    qry = f"UPDATE books SET read=1 WHERE name='{name}'"
    # Updating Table
    aud(qry)
    logging.warning("Updating Table")
