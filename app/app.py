import flask
import os

app = flask.Flask(__name__)


@app.route('/index')
def index():
    return flask.render_template("index.html")


app.add_url_rule('/', '/index', index)


@app.route('/create-post/<post_param>')
def create_post(post_param):
    pass


if __name__ == '__main__':
    print(os.path.dirname(app.root_path))
    app.run(host='0.0.0.0', port=8080, debug=True)
