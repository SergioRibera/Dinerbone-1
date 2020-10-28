import sqlite3
from sqlite3 import Error

sql_create_user_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        last_name text,
                                        email text,
                                        cod_tel integer,
                                        tel integer,
                                        pass text,
                                        c_i integer,
                                        dpto text
                                    ); """

def createConnection():
    try:
        conn = sqlite3.connect('./database.db')
    except Error as e:
        print(e)
    return conn

def createTable(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

