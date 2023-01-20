from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def index_page():
    return render_template('public/index.html')

@app.route('/jinja')
def jinja():
    my_name = "Kashee"
    age = 23
    langs = ['React','Cprograme','Python','Javascript']
    friends = {
        'Kaggy': 20,
        'Kawambo': 30,
        'kashii': 27,
        'Ken': 26, 
    }
    colours = ('Brown', 'Gray')
    
    cool = True
    class GitRepos:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        def pull(self):
            return f'Pulling repos {self.name}'
        def clone(self):
            return f'Cloning into {self.url}'
       
    gitRemote = GitRepos(
        name = "FlaskJinja",
        description="Learning and mastering",
        url = "https://github.com/NjeriMuchiri"
    )   
    def repeat(x,qty):
            return x * qty
    
        
    return render_template('public/jinja.html',
                           my_name=my_name,age=age,langs=langs,friends=friends,colours=colours,cool=cool,GitRepos=GitRepos,gitRemote=gitRemote,repeat=repeat)

@app.route('/about')
def about_page():
    return render_template('public/about.html')