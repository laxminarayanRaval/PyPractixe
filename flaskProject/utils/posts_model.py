import logging

from .database import Database


class PostsModel:
    def __init__(self, db_name):
        self.db = Database(db_name)
        self.__create_table__()

    def __create_table__(self):
        qry = """CREATE TABLE IF NOT EXISTS posts_mst(
        post_id integer primary key, 
        post_title text, 
        post_author text, 
        post_content text, 
        post_date text) """
        self.db.aud(qry)

    def new_post(self, *post_data):  # accepting tuple right now, we can accept **post_data (dictionary) too
        qry = """INSERT INTO posts_mst VALUES(?, ?, ?, ?, ?)"""
        self.db.aud(qry, post_data)
        logging.info("New Data Added to Database.")
        # print(post_data)

    def get_all_posts_data(self):
        qry = "SELECT * FROM posts_mst"
        return self.db.fetch(qry)

    def get_post_data(self, post_id):
        qry = f"SELECT * FROM posts_mst WHERE post_id='{post_id}'"
        return self.db.fetch(qry)

    def get_post_count(self):
        qry = "SELECT COUNT(*) FROM posts_mst"
        return self.db.fetch(qry)
