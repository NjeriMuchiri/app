from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def index_page():
    return render_template('public/index.html')

@app.route('/about')
def about_page():
    return "<h1 style='Color: #ffc87c'>About</h1>"