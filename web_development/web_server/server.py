from flask import Flask, render_template, escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', name='marvin')


@app.route('/blog')
def blog_f():
    return '<h1>Blog is coming!</h1>'


@app.route('/blog/2020/dog')
def blog_f2():
    return '<h1>this is a dog!</h1>'


@app.route('/about.html')
def about():
    return render_template('about.html')

# Variable rules:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/?highlight=variable%20rule
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User: %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/user/<username>/<int:post_id>')
def show_user_post_id(username, post_id):
    # show the user profile for that user
    return 'User: %s' % escape(username) + '<br> post_id: %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


# Catch all routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path
