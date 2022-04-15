import flask
import pymysql
import jinja2

import init
import user

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
            return flask.render_template("index.html", user_logged_in = True, username = usr.get_username())
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
def create_post(post_param):
    # TODO: implement this function
    # 1. TODO: get user session ID from cookies <- but how do we append user seeeion id automatically to the data?
    # 1.5 maybe instead of using default form action, we can use js code instead to implement this function?
    # 2. pack the post-title and post-content as a json object
    # 3. add the new post to posts database
    # 4. redirect user to inedx.html (page refresh
    pass

@app.route('/get-post/<page>')
def get_post(page):
    # TODO: implement this function
    # 1. get the latest posts by call posts.get_latest_posts(page*10) <- lets say we make 10 posts a 'page'
    # 2. parse the return value from the function
    # 3. use jinja2 to generate HTML for each post
    # 4. use js to update the on-screen html content
    # the template:
    # <div class="user-post">
    # <div class="post-user-info">{{ post_author }}</div>
    # <div class="post-content">{{ post_content }}</div>
    # <div class="post-like-count">{{ post_like_count }} people liked this.</div>
    # </div>
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
