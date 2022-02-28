from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

@app.route('/')
def index():
    if 'form' not in session: 
        session["form"] = data = {"first_name": "", "last_name": "", "email": "","gender":"", "password": "", "confirm_password": ""}
    return render_template('index.html')

# ========================================
# CREATE: new user
# ========================================
@app.route('/new_user', methods=["POST"])
def new_user():
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
# GO: to dashboard if logged in
# ========================================
@app.route('/dashboard')
def render_dashboard():
    if 'id' in session:
        data = { "id": session['id'] }
        user_id = User.get_user_info(data)
        all_recipes = Recipe.list_all_recipes()
        return render_template('dashboard.html', user_id = user_id, all_recipes = all_recipes)
    else:
        flash("Please Loin","info")
        return redirect('/')

# ========================================
# VALIDATION: Login
# ========================================
@app.route('/user_login',methods=["POST"])
def user_login():
    data = { "email" : request.form["email"] } 
    user_in_db = User.get_by_email(data)

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

# ========================================
# LOGOUT: clear all cookies
# ========================================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')