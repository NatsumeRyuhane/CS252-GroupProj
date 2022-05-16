import flask
import jinja2
import json

import app.init as init
import app.user as user
import app.posts as posts

db_conn = init.init_db()
app = flask.Flask(__name__)


@app.route('/index')
def index():
    sid = flask.request.cookies.get("session-id")

    if sid is None:
        return flask.render_template("index.html")
    else:
        auth_user_uid = user.get_uid_by_sid(sid, db_conn)
        if auth_user_uid:
            usr = user.User(auth_user_uid, db_conn)
            return flask.render_template("index.html", sid=usr.get_session_id(), username=usr.get_username())
        else:
            return flask.render_template("index.html")


# add redirect
app.add_url_rule('/', '/index', index)


@app.route('/login')
def login():
    return flask.render_template("login.html")


@app.route('/user-register')
def register():
    username = flask.request.args.get("username")
    email = flask.request.args.get("email")
    password = flask.request.args.get("password")

    reg_result = user.register_user(username, email, password, db_conn)
    if reg_result == 0:
        response = flask.redirect(location=f"/index", code=302)
        response.set_cookie(key="session-id", value=user.User(user.get_uid_by_username(username, db_conn), db_conn).get_session_id(), path="/")
        return response


@app.route('/user-login-auth')
def user_auth():
    username = flask.request.args.get("username")
    password = flask.request.args.get("password")

    auth_user_uid = user.get_uid_by_username(username, db_conn)
    if auth_user_uid:
        usr = user.User(auth_user_uid, db_conn)
        if password == usr.get_password():
            response = flask.redirect(location=f"/index", code=302)
            response.set_cookie(key="session-id", value=usr.get_session_id(), path="/")
            return response
        else:
            return flask.redirect(location=f"/login?loginfail=True", code=302)
    else:
        return flask.redirect(location=f"/login?loginfail=True", code=302)


@app.route('/account')
def account_page():
    sid = flask.request.cookies.get("session-id")

    if sid is None:
        return flask.render_template("index.html")
    else:
        auth_user_uid = user.get_uid_by_sid(sid, db_conn)
        if auth_user_uid:
            usr = user.User(auth_user_uid, db_conn)
            return flask.render_template("account.html", sid=usr.get_session_id(), username=usr.get_username())
        else:
            return flask.render_template("index.html")


@app.route('/user/<uid>')
def user_page():
    pass


@app.route('/posts/<post_topic_id>')
def topic_post_page(post_topic_id):
    sid = flask.request.cookies.get("session-id")
    auth_user_uid = None
    if sid is not None:
        auth_user_uid = user.get_uid_by_sid(sid, db_conn)

    topic_post = posts.get_topic_post(int(post_topic_id), db_conn)
    topic_create_time = topic_post[3]
    topic_title = json.loads(topic_post[2])['title']
    topic_post_content = json.loads(topic_post[2])['body']
    topic_author = user.User(topic_post[5], db_conn).get_username()

    def get_post_reply(post_id: int):
        # get rendered replies of a post
        template = jinja2.Template("""
        <div class="reply-post">
            <div class="post-header">
                <p class="post-author"><u>{{ post_author }}</u></p>
                <p>@</p>
                <p class="post-creation-time">{{ post_create_time }}</p>
            </div>
    
            <div class="post-contents">
                <div class="post-text-content" id="reply-{{ post_reply_counter }}">{{ post_text }}</div>
                {% if editable %}
                <div class="post-reply-count-editable" onclick="loadPageEditMenu({{ post_reply_counter }})">{{ post_reply_counter }}</div>
                {% else %}
                <div class="post-reply-count">{{ post_reply_counter }}</div>
                {% endif %}
            </div>
        </div>
        """)

        replies = posts.get_topic_replies(post_id, db_conn)
        if replies is not None:
            render_result = ""
            counter = 0

            for i in range(0, len(replies)):
                author = user.User(replies[i][5], db_conn).get_username()
                time = replies[i][3]
                content = json.loads(replies[i][2].replace("\r\n", "\\r\\n"))['body']
                counter += 1

                editable = False
                if auth_user_uid == replies[i][5]: editable = True
                rendering = template.render(post_author=author, post_create_time=time, post_text=content, post_reply_counter=counter, editable = editable)
                render_result += rendering

            return render_result
        else:
            return None


    return flask.render_template("post_detail.html", topic_title=topic_title, topic_author=topic_author,
                                 topic_create_time=topic_create_time, topic_text=topic_post_content, topic_replies=get_post_reply(post_topic_id),
                                 topic_id=post_topic_id, uid=auth_user_uid)

@app.route('/logout')
def logout():
    response = flask.redirect('/index')
    response.delete_cookie("session-id")
    return response


@app.route('/api/create-post')
def create_post():
    title = flask.request.args.get("post-title")
    body = flask.request.args.get("post-body")
    post_content = json.dumps({"title": title, "body": body})

    sid = flask.request.cookies.get("session-id")

    posts.add_topic_post(post_content, user.get_uid_by_sid(sid, db_conn), db_conn)
    return flask.redirect(location=f"/index?sessionid={sid}", code=302)


@app.route('/api/create-reply')
def create_reply():
    topic_id = int(flask.request.args.get("topic-id"))
    body = flask.request.args.get("post-body")
    post_content = json.dumps({"title": "null", "body": body})
    uid = user.get_uid_by_sid(flask.request.cookies.get("session-id"), db_conn)

    posts.add_post_reply(post_content, uid, topic_id, db_conn)
    return flask.redirect(location=f"/posts/{topic_id}", code=302)

@app.route('/api/post-edit')
def edit_post():
    topic_id = int(flask.request.args.get("edit-topic-id"))
    reply_id = int(flask.request.args.get("edit-reply-id"))
    post_content = json.dumps({"title": "null", "body": flask.request.args.get("post-edit-body")})

    posts.edit_post(topic_id, reply_id, post_content, db_conn)
    return flask.redirect(location=f"/posts/{topic_id}", code=302)

@app.route('/api/get-topic-post/<page>')
def get_topic_post(page):
    raw_posts = posts.get_latest_posts(int(page) * 10, db_conn)
    post_html_template = jinja2.Template("""
    <div class="user-post" onclick="window.location.href='/posts/{{ post_topic_id }}'">
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
        topic_id = int(raw_posts[i][2])
        render_result = post_html_template.render(post_title=content['title'], post_body=content['body'], post_author=author, post_topic_id=topic_id)
        rendered_post += render_result

    return rendered_post


@app.route('/api/upload')
def file_upload():
    # the URL used to handle file update
    # TODO
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
