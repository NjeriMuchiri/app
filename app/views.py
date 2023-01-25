from app import app
from flask import render_template, request, redirect, jsonify, make_response


@app.route('/')
@app.route('/home')
def index_page():
    print(f'Flask_ENV_is_set_to: {app.config["ENV"]}')
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

@app.route('/signup',methods=["GET","POST"])
def signup_page():
    
    if request.method == "POST":
        req = request.form
        username = req["username"]
        email = req.get("email")
        password = request.form["password"]
        print(username,email,password)
        return redirect(request.url)        
    return render_template('public/signup.html')

users = {
    "waithira":{
        "name":"Catherine Wanjiru",
        "bio": "Gifted with a green thumb",
        "occupation":"farmer"
    },
    "njerina":{
        "name":"Njeri Muchiri",
        "bio":"Gifted with many skills",
        "occupation":"Software Engineer"
    },
    "muchiri":{
        "name":"Muchiri Gichuki",
        "bio":"Gemstone investor",
        "occupation":"business enterpreneur"
    }
}

@app.route("/profile/<username>")
def profile(username):
    
    user = None
    
    if username in users:
        user = users[username]
        
    return render_template('/public/profile.html', username=username, user=user)

@app.route('/multiple/<foo>/<bar>/<baz>')
def multiple(foo,bar,baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"


@app.route("/jsoning", methods=["POST"])
def jsoning():
    if request.is_json:
        req = request.get_json()
        response = {
            "message": "JSON received!",
            "name": req.get("name")
        }
        res = make_response(jsonify(response), 200)
        return res
    else:
        res = make_response(jsonify({"message": "No JSON received"}), 400)
        
        return res
    
@app.route('/guestbook')
def guestbook():
    return render_template('public/guestbook.html')

@app.route('/guestbook/create-entry')
def create_entry():
    
    req = request.get_json()
    print(req)
    res = make_response(jsonify(req), 200)
    return res

@app.route('/query')
def query_ting():
    if request.args:
        
        args = request.args
        serialized = ", ".join(f"{k}: {v}" for k, v in args.items())
       
        return f"(Query) {serialized}", 200
    else:
        return "No query received", 200

