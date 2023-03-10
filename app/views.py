from app import app
from flask import render_template, request, redirect, jsonify, make_response
import os
from werkzeug.utils import secure_filename



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


@app.route("/profile/<username>")
def profile(username):
    
    user = None
    
    if username in users:
        user = users[username]
        
    return render_template('/public/profile.html', username=username, user=user)


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
    
app.config['IMAGE_UPLOADS'] = '/home/muchirinjeri/app/app/static/img/uploads'
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ["PNG", "JPG","JPEG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 *1024

def allowed_image(filename):
    if not '.' in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1]
    
    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False

def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

@app.route('/upload-image',methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        
        if request.files:
            
            if request.files:
                if not allowed_image_filesize(request.cookies.get('filesize')):
                  print("file exceeds the maximum size ")
                  return redirect(request.url)
                    
            
            image = request.files['image']
            
            if image.filename == ' ':
                print("Image must have a filename")
                return redirect(request.url)
            
            if not allowed_image(image.filename):
                print("That image extension is not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)    
                image.save(os.path.join(app.config['IMAGE_UPLOADS'], filename))
            print('image saved')
            return redirect(request.url)
        
    return render_template("public/upload_image.html")



from flask import send_from_directory, abort

app.config['CLIENT_IMAGES'] = '/home/muchirinjeri/app/app/static/client/img'
app.config['CLIENT_CSV'] = '/home/muchirinjeri/app/app/static/client/csv'
app.config['CLIENT_REPORTS'] = '/home/muchirinjeri/app/app/static/client/reports'
app.config['CLIENT_PDFS'] = '/home/muchirinjeri/app/app/static/client/pdf'



@app.route('/get-image/<image_name>')
def get_image(image_name):
    
    try:
        return send_from_directory(app.config['CLIENT_IMAGES'], path=image_name, as_attachment=False)
        
    except FileNotFoundError:
        abort(404)
        
@app.route('/get-csv/<filename>')
def get_csv(filename):
    
    try:
        return send_from_directory(app.config['CLIENT_CSV'], path=filename, as_attachment=True)
        
    except FileNotFoundError:
        abort(404)

@app.route('/get-report/<path:path>')
def get_reports(path):
    
    try:
        return send_from_directory(app.config['CLIENT_REPORTS'], path=path, as_attachment=True)
        
    except FileNotFoundError:
        abort(404)


@app.route('/get-pdf/<document_name>')
def get_document(document_name):
    
    try:
        return send_from_directory(app.config['CLIENT_PDFS'], path=document_name, as_attachment=False)
        
    except FileNotFoundError:
        abort(404)
        

@app.route('/cookies')
def cookies():
    
    res = make_response('Cookies', 200)
    
    cookies = request.cookies
    Flavor = cookies.get('chocolatechip')
    print(Flavor)
    res.set_cookie(
        "chocolatechip",
        value = "biscuit",
        max_age = 10,
        expires=None,
        path=request.path,
        domain=None,
        secure=False,
        httponly=False,
        samesite=None
        )
    res.set_cookie('egg','baking')
    res.set_cookie('class','studyig')
    
    return res

users = {
    "waithira":{
        "username":"waithira",
        "bio": "Gifted with a green thumb",
        "occupation":"farmer",
        "password":"watash"
    },
    "njerina":{
        "username":"njerina",
        "bio":"Gifted with many skills",
        "occupation":"Software Engineer",
        "password":"njeshkashee"
    },
    "muchiri":{
        "username":"muchiri",
        "bio":"Gemstone investor",
        "occupation":"business enterpreneur",
        "password":"muchirigichuki"
    }
}

from flask import render_template, request, session,redirect, url_for

app.config["SECRET_KEY"] = 'rg-eEwGmTa-830T2JAhxkw'


@app.route('/sign-in', methods=["GET","POST"])
def sign_in():
    if request.method == 'POST':
        
        req = request.form
        
        username = req.get('username')
        password = req.get('password')
        
        if not username in users:
            print("username not found")
            return redirect(request.url)
        else: 
            user = users[username]
            
        if not password == user['password']:
            print('incorrect password')
            return redirect(request.url)
        else:
            session['USERNAME'] = user['username'] 
            print('user added to session')
            return redirect(url_for('profile'))
            
        
    return render_template('public/sign_in.html')



@app.route('/profile')
def profile():
    
    if session.get('USERNAME', None) is not None:
        username = session.get('USERNAME')
        user = users[username]
        return render_template('public/profile.html', user=user)
    else:
        print("Username not found in session")
        return redirect(url_for('sign_in'))
   
   
@app.route('/sign-out')
def sign_out():
    
    session.pop('USERNAME',None)
    
    return redirect(url_for('sign_in'))

