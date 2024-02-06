
import mysql.connector

class Category:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect_to_db(self):
        return mysql.connector.connect(**self.db_config)

    

