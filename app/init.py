import pymysql
import exceptions


def init_db():
    try:
        db = pymysql.connect(host="localhost", user="root", password="12345678", database="MGAF", autocommit=True)
    except pymysql.err.OperationalError:
        # if error during db connection, try init the db
        raise exceptions.DatabaseOperationErrorException("\n [ IMPORTANT NOTE ]\n Please use the database initialization script provided under /tests/utils/ to initialize database, and check the connection configuration in /app/init.py, line 7.")

    return db
