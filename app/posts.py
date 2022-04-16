import pymysql
import jinja2

def add_post(content: str, author: int, db: pymysql.connections.Connection):
    cursor = db.cursor()
    if author is None:
        return 2

    res = cursor.execute(
        f"""
        INSERT INTO MGAF.posts(post_content, post_date, post_by, post_likes)
        VALUES ('{content}', now(), {author}, 0);
        """)

    if res == 1: return 0
    else: return 1

def get_latest_posts(count: int, db: pymysql.connections.Connection):
    cursor = db.cursor()

    cursor.execute(
        f"""
        SELECT post_content, post_by
        FROM MGAF.posts
        ORDER BY post_date DESC
        LIMIT {count};
        """)

    result = cursor.fetchall()
    if result == ():
        return None
    else:
        return result