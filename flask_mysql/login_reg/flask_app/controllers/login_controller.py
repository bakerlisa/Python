from flask_app import app
from flask import render_template,redirect,request,session,flash,url_for
from flask_app.models.login_model import Login

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

#=====================
# 404 route
#=====================
@app.route('/<path:path>')
def catch_all(path):
    return render_template("404.html")

#=====================
# Base Route
#=====================
@app.route('/')
def index():
    if 'form' not in session: 
        session["form"] = data = {"first_name": "", "last_name": "", "email": "","gender":"", "password": "", "confirm_password": ""}
    return render_template('index.html')

#=====================
# Login
#=====================
@app.route('/login', methods=["POST"])
def log_user_in():
    data = { "email" : request.form["email"] } 
    user_in_db = Login.get_by_email(data)

    if not request.form["email"]:
        flash("Invalid Email/Password","login")
        return redirect("/")
    else:
        if user_in_db is "0":
            flash("Email does not exsist","login")
            return redirect("/") 
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            flash("Invalid Email/Password","login")
            return redirect('/')
            
        session['id'] = user_in_db.id
        return redirect("/dashboard")

#=====================
#Logout
#=====================
@app.route('/logout')
def log_user_out():
    session.clear()
    return redirect("/")

#=====================
#registration
#=====================
@app.route('/registration', methods=["POST"])
def registration():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "gender": request.form.get('gender'),
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"]
    }
    if not Login.validate_registration(request.form):
        session["form"] = data
        return redirect('/')
    else:
        data["password"] = bcrypt.generate_password_hash(request.form['password'])
        # session.pop("form")
        new_user = Login.new_registration(data)
        session['id'] = new_user
        return redirect('/dashboard')

#=====================
# Login Complete go to dashboard
#=====================
@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        flash("Please Login","reg")
        return redirect('/')
    else:
        data = {
            "id": session['id']
        }
        user_info = Login.get_user_info(data)
        return render_template("dashboard.html", user_info = user_info)

@app.route('/delete')
def delete_account():
    data = {
        "id": session['id']
    }
    Login.delete_account(data)
    return redirect('/')