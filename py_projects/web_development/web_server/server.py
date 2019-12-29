from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog')
def blog_f():
    return '<h1>Blog is coming!</h1>'


@app.route('/blog/2020/dog')
def blog_f2():
    return '<h1>this is dog!</h1>'


@app.route('/about.html')
def about():
    return render_template('about.html')

# Catch all routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path
