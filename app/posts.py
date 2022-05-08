import pymysql
import app.exceptions as excp


def add_topic_post(content: str, author_UID: int, db: pymysql.connections.Connection):
    cursor = db.cursor()
    if author_UID is None:
        raise excp.InvalidUIDException

    res = cursor.execute(
        f"""
        INSERT INTO MGAF.posts(post_reply_id, post_content, post_date, post_last_update, post_by, post_likes)
        VALUES (0, '{content}', now(), now(), {author_UID}, 0);
        """)

    if res == 1:
        pass
    else:
        raise excp.DatabaseOperationErrorException


def add_post_reply(content: str, author_UID: int, topic_ID: int, db: pymysql.connections.Connection):
    cursor = db.cursor()
    if author_UID is None:
        raise excp.InvalidUIDException

    res = cursor.execute(
        f"""
        INSERT INTO MGAF.posts(post_reply_id, post_content, post_date, post_last_update, post_by, post_likes)
        VALUES (0, '{content}', now(), now(), {author_UID}, 0);
        """)

    if res == 1:
        pass
    else:
        raise excp.DatabaseOperationErrorException


def like(post_id: int, uid: int, db: pymysql.connections.Connection):
    # handles user like posts
    # TODO
    pass


def get_topic_post(topic_id: int, db: pymysql.connections.Connection):
    cursor = db.cursor()

    cursor.execute(
        f"""
               SELECT *
               FROM MGAF.posts
               WHERE post_topic_id = {topic_id} AND post_reply_id = 0
               ORDER BY post_reply_id;
               """)

    result = cursor.fetchall()
    if result == ():
        return None
    else:
        return result[0]


def get_topic_replies(topic_id: int, db: pymysql.connections.Connection):
    cursor = db.cursor()

    cursor.execute(
        f"""
            SELECT *
            FROM MGAF.posts
            WHERE post_topic_id = {topic_id} AND post_reply_id != 0
            ORDER BY post_reply_id;
            """)

    result = cursor.fetchall()
    if result == ():
        return None
    else:
        return result


def get_post_reply_count(topic_ID: int, db: pymysql.connections.Connection):
    cursor = db.cursor()

    res = cursor.execute(
        f"""
           SELECT max(post_reply_id)
           FROM MGAF.posts
           WHERE post_topic_id = {topic_ID}
           """)

    if res == 1:
        return int(cursor.fetchall()[0][0]) + 1
    else:
        raise excp.DatabaseOperationErrorException


def get_latest_posts(count: int, db: pymysql.connections.Connection):
    cursor = db.cursor()

    cursor.execute(
        f"""
        SELECT post_content, post_by, post_topic_id
        FROM MGAF.posts
        WHERE post_reply_id = 0
        ORDER BY post_last_update DESC
        LIMIT {count};
        """)

    result = cursor.fetchall()
    if result == ():
        return None
    else:
        return result
