from ast import MatchSequence
from nis import match
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
from flask_app.models.address_model import Address
# from flask_app.models.flock_model import Group

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
            session["form"] = data = {"first_name": "", "last_name": "", "phone": "","email": "","gender":"", "password": "", "confirm_password": ""}
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
            "phone" : request.form['phone'],
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
            # all_groups = Flock.select_all_groups()
            # all_messages = Message.get_all_for_message(data)
            return render_template('dashboard.html',user_info=user_info)
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
    return render_template('user-settings.html',user_info=user_info)

# ========================================
# ROUTE: create a flock
# ========================================
@app.route('/create_flock')
def create_flock():
    return render_template('create_flock.html')

# ========================================
# ROUTE: lock
# ========================================
@app.route('/lock')
def lock():
    # session["counter"] = 10
    # return render_template('index.html')
    return render_template('lock.html')

# UPDATE: user settings
@app.route('/update_user_settings',methods=["POST"])
def update_user_settings():
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "phone": request.form["phone"],
        "email": request.form["email"]
    }

    if not User.validate_update_user(request.form):
        return redirect ('/user_settings')
    else:
        flash('Settings have been updated',"info")
        User.update_user_info(data)
        return redirect('/dashboard')

# ========================================
# UPDATE: address
# ========================================
@app.route('/update_address',methods=["POST"])
def update_address():
    data = {
        "address": request.form["address"],
        "city": request.form["city"],
        "state": request.form["state"],
        "zip": request.form["zip"],
        "user_id": request.form["user_id"]
    }
    
    dataTwo = {
        "user_id": request.form["user_id"]
    }
    user_has_address = Address.has_address(dataTwo)

    if not Address.validate_update_address(request.form): 
        return redirect ('/user_settings')
    elif user_has_address == "0":
        flash("Address has been addded to your account","info")
        Address.add_address(data)
    else:
        flash("User info has been updated!","info")
        Address.update_address(data)
    return redirect ('/dashboard')

# ========================================
# UPDATE: password
# ========================================
@app.route('/update_password', methods=["POST"])
def update_password():
    data = {
        "password": request.form['password'],
        "id": request.form['id']
    }
    password_in_db = User.get_by_password(data)

    if not User.validate_password(request.form):
        return redirect('/user_settings')
    elif not bcrypt.check_password_hash(password_in_db.password, request.form['old_password']):
        flash("Old password doesn't match what we have in the system","password")
        return redirect('/user_settings')
    else:
        flash("Password has been updated!","info")
        return redirect('/dashboard')
    

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

