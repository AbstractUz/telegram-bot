import psycopg2
import psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from Config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT,
                                           connection_factory=psycopg2.extras.DictConnection)
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.init_schema()

    def init_schema(self):
        with open("database/schema/init_schema.sql", 'r') as file:
            sql = file.read()
            self.cursor.execute(sql)
            self.connection.commit()


db = Database()
