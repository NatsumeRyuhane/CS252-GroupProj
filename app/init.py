import pymysql

def init_db():
    try:
        db = pymysql.connect(host="localhost", user="root", password="12345678", database="MGAF")
    except pymysql.err.OperationalError:
        # if error during db connection, try init the db
        sql_init_connection = pymysql.connect(host="localhost", user="root", password="12345678")
        sql_init_cursor = sql_init_connection.cursor()
        sql_init_command_file = open("./static/sql/init.sql")
        sql_init_cursor.execute(sql_init_command_file.read())

        db = pymysql.connect(host="localhost", user="root", password="12345678", database="MGAF")

    return db
