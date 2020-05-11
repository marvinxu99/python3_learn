# server.py
from datetime import datetime
from flask import Flask, render_template, escape, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def web_home():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
# @app.route('/index.html')
# def index1():
#     return render_template('index.html')
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
# @app.route('/works.html')
# def works():
#     return render_template('works.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def append_to_txt_file(data):
    with open('database.txt', mode='a') as database:
        dt_now = datetime.now()
        database.write(f'\n\nTIME:{dt_now.strftime("%d-%b-%Y, %H:%M:%S")}')

        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(
            f'\nEMAIL: {email} \nSUBJECT: {subject} \nMESSAGE: {message}')


def append_to_csv_file(data):
    with open('database.csv', mode='a', newline='') as database2:
        time_str = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow((time_str, email, subject, message))


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if data['email'] and data['subject'] and data['message']:
                append_to_txt_file(data)
                append_to_csv_file(data)
                return redirect('/thankyou.html')
            else:
                return redirect('/contact.html')
        except:
            return 'did not save to database.'
    else:
        return 'somethig went wrong, try again!'


@app.route('/blog')
def blog_f():
    return '<h1>Blog is coming!</h1>'


@app.route('/blog/2020/dog')
def blog_f2():
    return '<h1>this is dog!</h1>'


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
