import flask
import pymysql
import jinja2

import user_utils

db = pymysql.connect(host="localhost", user="root", password="12345678", database="MGAF")
cursor = db.cursor()

app = flask.Flask(__name__)


@app.route('/index')
def index():
    uid = user_utils.UID(flask.request.args.get("uid"))


    return flask.render_template("index.html", user_logged_in = uid.is_valid(), username = uid.get_username())

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

    return flask.redirect(location = f"/index?username={username}&password={password}", code = 302)

@app.route('/create-post/<post_param>')
def create_post(post_param):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
