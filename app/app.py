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
    pass

@app.route('/user-login-auth')
def user_auth():
    username = flask.request.args.get("username")
    password = flask.request.args.get("password")

    auth_user_uid = user.get_uid_by_username(username, db_conn)
    if auth_user_uid:
        usr = user.User(auth_user_uid, db_conn)
        if password == usr.get_password():
            return flask.redirect(location = f"/index?sessionid={usr.get_session_id()}", code = 302)
        else:
            return flask.redirect(location = f"/login?loginfail=True", code = 302)
    else:
        return flask.redirect(location = f"/login?loginfail=True", code = 302)

@app.route('/create-post/<post_param>')
def create_post(post_param):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
