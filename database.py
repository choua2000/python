from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
# CONNECT DATABASE
dbConnection = "dbname='postgres' user='postgres' host='localhost' password='sml' port='5432'"
# dbConnection = "dbname='biotime' user='postgres' host='202.137.144.138' password='sml' port='5432'"

connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)

@contextmanager
def getcursorTO():
    con = connectionpool.getconn()
    con.autocommit = True
    con.rollback()
    try:
        yield con.cursor()
    finally:
        connectionpool.putconn(con)
import sqlite3
conn = sqlite3.connect('my_database.db', check_same_thread=False)
print("Connected to DB successfully")
