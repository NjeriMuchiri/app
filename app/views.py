from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def index_page():
    return render_template('public/index.html')

@app.route('/jinja')
def jinja():
    my_name = "Kashee"
    return render_template('public/jinja.html', my_name=my_name)

@app.route('/about')
def about_page():
    return render_template('public/about.html')