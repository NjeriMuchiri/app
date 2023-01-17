from app import app
from flask import render_template


@app.route('/')
def index():
    return 'Hello Kashee'

@app.route('/about')
def about():
    return "<h1 style='Color: #ffc87c'>About</h1>"