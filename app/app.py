import flask
import pymysql
import jinja2
import json
import uuid

import init
import user
import posts

db_conn = init.init_db()
app = flask.Flask(__name__)


@app.route('/index')
def index():
    sid = flask.request.args.get("sessionid")

    if sid is None:
        return flask.render_template("index.html")
    else:
        auth_user_uid = user.get_uid_by_sid(sid, db_conn)
        if auth_user_uid:
            usr = user.User(auth_user_uid, db_conn)
            return flask.render_template("index.html", sid = usr.get_session_id(), username = usr.get_username())
        else:
            return flask.render_template("index.html")


# add redirect
app.add_url_rule('/', '/index', index)


@app.route('/login')
def login():
    return flask.render_template("login.html")


@app.route('/register')
def register():
    # TODO: implement this function
    # 1. get the form data
    # 2. use templated mysql command to add user to user db
    # 3. automatically get the session id and redirect user to index page in logged in state
    pass

@app.route('/user-login-auth')
def user_auth():
    username = flask.request.args.get("username")
    password = flask.request.args.get("password")

    auth_user_uid = user.get_uid_by_username(username, db_conn)
    if auth_user_uid:
        usr = user.User(auth_user_uid, db_conn)
        if password == usr.get_password():
            return flask.redirect(location = f"/index?sessionid={usr.set_new_session_id()}", code = 302)
        else:
            return flask.redirect(location = f"/login?loginfail=True", code = 302)
    else:
        return flask.redirect(location = f"/login?loginfail=True", code = 302)

@app.route('/create-post')
def create_post():
    title = flask.request.args.get("post-title")
    body = flask.request.args.get("post-body")
    post_content = json.dumps({"title": title, "body": body})

    sid = flask.request.args.get("sessionid")

    posts.add_post(post_content, user.get_uid_by_sid(sid, db_conn), db_conn)
    return flask.redirect(location=f"/index?sessionid={sid}", code=302)


@app.route('/get-post/<page>')
def get_post(page):
    raw_posts = posts.get_latest_posts(int(page)*10, db_conn)
    post_html_template = jinja2.Template("""
    <div class="user-post">
        <div class="post-content">
            <div class="post-title">{{ post_title }}</div>
            <div class="post-body">{{ post_body }}</div>
        </div>
        <div class="post-author">{{ post_author }}</div>
    </div>\n
    """)

    rendered_post = ""

    for i in range(0, len(raw_posts)):
        content = json.loads(raw_posts[i][0])
        author = user.User(raw_posts[i][1], db_conn).get_username()
        render_result = post_html_template.render(post_title = content['title'], post_body = content['body'], post_author = author)
        rendered_post += render_result

    return rendered_post



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
