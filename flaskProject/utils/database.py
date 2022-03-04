import logging
import sqlite3

logging.basicConfig(
    filename='postsApp.log',
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.INFO
)


class DatabaseConnect:
    def __init__(self, db_name):
        self.cursor = None
        self.db_name = db_name

    def __enter__(self):
        self.cnn = sqlite3.connect(self.db_name)
        self.cursor = self.cnn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_type:
            self.cnn.close()
        else:
            self.cnn.commit()
            self.cnn.close()


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def aud(self, qry, tpl=None):
        with DatabaseConnect(self.db_name) as curr:
            if not tpl:
                curr.execute(qry)
            else:
                curr.execute(qry, tpl)

    def fetch(self, qry):
        with DatabaseConnect(self.db_name) as curr:
            curr.execute(qry)
            return curr.fetchall()
