from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
from flask_app.models.message_model import Message
from flask_app.models.group_model import Group

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ==========================================
# ROUTE: home page
# ==========================================
@app.route('/')
def index():
    ip_addr = request.remote_addr
    session["ip"] = ip_addr

    if 'id' in session:
        return redirect('/dashboard')
    elif not "counter" in session:
        session["counter"] = 10

    if session["counter"] == 1:
        return redirect("/lock")
    else:
        if 'form' not in session: 
            session["form"] = data = {"first_name": "", "last_name": "", "email": "","gender":"", "password": "", "confirm_password": ""}
        return render_template('index.html')

# ==========================================
# ADD: new user
# ==========================================

@app.route('/new_user', methods=["POST"])
def new_user():
    if session["counter"] == 1:
        return redirect("/lock")
    else:
        data = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "password" : request.form['password'],
            "confirm_password" : request.form['confirm_password']
        }

        if not User.validate_user(request.form):
            session["form"] = data
            return redirect('/')
        else:
            data["password"] = bcrypt.generate_password_hash(request.form['password'])

            new_user_id = User.create_new_user(data)
            session['id'] = new_user_id
            return redirect('/dashboard')

# ========================================
# ROUTE: to dashboard if logged in : go to home (/)
# ========================================
@app.route('/dashboard')
def render_dashboard():
    if session["counter"] == 1:
        return redirect("/lock")
    else:
        if 'id' in session:
            data = { "id": session['id'] }
            user_info = User.get_user_info(data)
            all_groups = Group.select_all_groups()
            # all_messages = Message.get_all_for_message(data)
            return render_template('dashboard.html',user_info=user_info,all_groups=all_groups)
        else:
            flash("Please Loin","info")
            return redirect('/')

# ========================================
# ROUTE: user settings page
# ========================================
@app.route('/user_settings')
def user_settings():
    data = { "id": session['id'] }
    user_info = User.get_user_info(data)
    return render_template('user-settings.html')

# ========================================
# ROUTE: create a flock
# ========================================
@app.route('/create_flock')
def create_flock():
    return render_template('create_flock.html')

# ========================================
# LOGOUT: clear all cookies
# ========================================
@app.route('/logout')
def logout():
    if session["counter"] == 1:
        return redirect("/lock")
    else:
        session.clear()
        return redirect('/')

# ========================================
# VALIDATION: Login
# ========================================
@app.route('/user_login',methods=["POST"])
def user_login():
    if session["counter"] == 1:
        return redirect("/lock")
    else:
        data = { "email" : request.form["email"] } 
        email_in_db = User.get_by_email(data)

        if not request.form["email"]:
            session["counter"] = session["counter"] - 1
            flash(f"Invalid Email/Password {session['counter']} chance(s) left","login")
            return redirect("/")
        else:
            if email_in_db == "0":
                session["counter"] = session["counter"] - 1
                flash(f"Email does not exsist {session['counter']} chance(s) left","login")
                return redirect("/") 
            if not bcrypt.check_password_hash(email_in_db.password, request.form['password']):
                session["counter"] = session["counter"] - 1
                flash("Invalid Email/Password","login")
                return redirect('/')
                
            session['id'] = email_in_db.id
            session["counter"] = 10
            return redirect("/dashboard") 

@app.route('/lock')
def lock():
    # session["counter"] = 10
    # return render_template('index.html')
    return render_template('lock.html')
