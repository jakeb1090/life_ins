from flask import Flask, render_template, request, redirect, url_for, g, session
import model



app = Flask(__name__)
app.secret_key = "pirates"

username = ''
user = model.check_usernames(username)

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route('/home', methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        areyouuser = requests.form['username']
        pwd = model.check_pwd(username)
        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return redirect(url_for("todo_list"))
        return render_template("index.html", message="login unsuccessful")
    return render_template('index.html', message="Login or ")


@app.route('/todo_list', methods = ['GET', 'POST'])    
def _list():
    if request.method == 'GET':
        data = model.get_tasks()
        return render_template("todo_list.html", data=data)  
    else: 
        task = request.form['task']
        due_date = request.form['due_date']
        add_task = model.add_task(task, due_date)
        message = "new task added"
        return render_template("todo_list.html", message=message)
        if username in session:
            g.user=session['username']
            return render_template("todo_list.html", message="yes")
        return render_template("todo_list.html", message=add_task)  
                    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = "Please sign up"
        return render_template("signup.html", message=message)
    else:
        username = request.form['username']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        if password != password_confirm:
            message = "passwords do not match"
            return render_template("signup.html", message=message)
        else:
            insert = model.add_user(username, password)
            message = "Registration successful!"
            return render_template("signup.html", message=insert)
            

@app.route('/mentorship', methods = ['GET'])
def mentorship():
    return render_template("mentorship.html")

@app.route('/products', methods = ['GET'])
def pdoducts():
    return render_template("products.html")

@app.route('/about', methods = ['GET'])
def about():
    return render_template("about.html")

@app.route('/terms', methods = ['GET'])
def terms():
    return render_template("terms.html", context={"abc":"938"})
    
@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template("privacy.html")

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=8000, debug=True)
