from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return "<h1 style='Color: #ffc87c'>About</h1>"