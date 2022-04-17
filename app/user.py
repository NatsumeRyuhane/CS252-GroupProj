import pymysql


class User:

    def __init__(self, uid, db: pymysql.connections.Connection):
        self.uid = int(uid)
        self.db_conn = db

    def get_username(self):
        cursor = self.db_conn.cursor()

        cursor.execute(
            f"""
        SELECT user_name
        FROM MGAF.users
        WHERE user_id = {self.uid};
        """)

        result = cursor.fetchall()
        if result == ():
            return None
        else:
            return result[0][0]

    def get_password(self):
        cursor = self.db_conn.cursor()

        cursor.execute(
            f"""
        SELECT user_password
        FROM MGAF.users
        WHERE user_id = '{self.uid}';
        """)

        result = cursor.fetchall()
        if result == ():
            return None
        else:
            return result[0][0]

    def get_session_id(self):
        cursor = self.db_conn.cursor()

        cursor.execute(
            f"""
        SELECT user_session_id
        FROM MGAF.users
        WHERE user_id = '{self.uid}';
        """)

        result = cursor.fetchall()
        if result == ():
            return None
        else:
            return result[0][0]

    def set_new_session_id(self):
        cursor = self.db_conn.cursor()

        cursor.execute(
            f"""
        UPDATE MGAF.users
        SET user_session_id=uuid()
        WHERE user_id = '{self.uid}';
        """)

        cursor.fetchall()

        return self.get_session_id()


def get_uid_by_sid(sid: str, db: pymysql.connections.Connection):
    cursor = db.cursor()

    cursor.execute(
        f"""
    SELECT user_id 
    FROM MGAF.users
    WHERE user_session_id = '{sid}';
    """)

    result = cursor.fetchall()
    if result == ():
        return None
    else:
        return result[0][0]


def get_uid_by_username(username: str, db: pymysql.connections.Connection):
    cursor = db.cursor()

    cursor.execute(
        f"""
    SELECT user_id 
    FROM MGAF.users
    WHERE user_name = '{username}';
    """)

    result = cursor.fetchall()
    if result == ():
        return None
    else:
        return result[0][0]


def register_user(username: str, email: str, password: str, db: pymysql.connections.Connection):
    cursor = db.cursor()

    result = cursor.execute(
        f"""
        INSERT INTO MGAF.users (user_name, user_password, user_email, user_register_date, user_session_id)
        VALUE ('{username}', '{password}', '{email}', now(), uuid());
        """)

    if result == 1:
        return 0
    else:
        return 1
