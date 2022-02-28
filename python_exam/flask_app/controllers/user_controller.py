from flask_app import app
from flask import render_template,redirect,request,session,flash

from flask_app.models.user_model import User
from flask_app.models.show_model import Show
from flask_app.models.liked_model import Likes

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# ==============================================
# 404 route
# ==============================================
@app.route('/<path:path>')
def catch_all(path):
    return render_template("404.html")
    
# ==============================================
# ROUTE: home page
# ==============================================
@app.route('/')
def index():
    ip_addr = request.remote_addr
    session["ip"] = ip_addr 

    if 'id' in session:
        return redirect('/dashboard')
    if not "counter" in session:
        session["counter"] = 10
    if 'form' not in session: 
        session["form"] = data = {"first_name": "", "last_name": "", "email": "","password": "", "confirm_password": ""}
    return render_template('index.html')

# ========================================
# ROUTE: if logged to /dashboard in : to (/) 
# ========================================
@app.route('/dashboard')
def render_dashboard():
    if session["counter"] == 0:
        return redirect("/lock")
    else:
        if 'id' in session:
            data = { "id": session['id'] }
            user_info = User.get_user_info(data)
            all_user_shows = Show.get_users_shows(data)
            all_db_shows = Show.get_all_shows()
            
            users_shows_likes = Likes.get_all_shows_info()
            return render_template('dashboard.html', user_info = user_info,all_user_shows = all_user_shows,all_db_shows = all_db_shows,users_shows_likes = users_shows_likes)
        else:
            flash("Please Loin","info")
            return redirect('/')

# ========================================
# ROUTE: logout - clear all cookies
# ========================================
@app.route('/logout')
def logout():
    if session["counter"] == 0:
        return redirect("/lock")
    else:
        session.clear()
        return redirect('/')

# ==========================================
# ADD: new user
# ==========================================
@app.route('/new_user', methods=["POST"])
def new_user():
    if session["counter"] == 0:
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
# VALIDATION: Login
# ========================================
@app.route('/user_login',methods=["POST"])
def user_login():
    if session["counter"] == 0:
        return redirect("/lock")
    else:
        data = { "email" : request.form["email"] } 
        email_in_db = User.get_by_email(data)

        if not request.form["email"]:
            session["counter"] = session["counter"] - 1
            flash(f"Invalid Email/Password {session['counter']} chance(s) left","login")
            flash(f"Invalid Email/Password","login")
            return redirect("/")
        else:
            if email_in_db is "0":
                session["counter"] = session["counter"] - 1
                flash(f"Email does not exsist {session['counter']} chance(s) left","login")
                flash(f"Invalid Email/Password","login")
                return redirect("/") 
            if not bcrypt.check_password_hash(email_in_db.password, request.form['password']):
                session["counter"] = session["counter"] - 1
                flash("Invalid Email/Password","login")
                return redirect('/')
                
            session['id'] = email_in_db.id
            session["counter"] = 10
            return redirect("/dashboard") 

# ========================================
# DELETE: show
# ========================================
@app.route('/delete/<int:id>')
def delete(id):
    if not 'id' in session:
        return redirect('/')
    else:
        data = { "id" : id } 
        Show.delete_show(data)
        return redirect('/dashboard')

# ========================================
# LOCK: where you go if you screw the pooch on your login
# ========================================
@app.route('/lock')
def lock():
    # === in case you get looged out ===
    # session.pop("counter")
    # return render_template('index.html')
    session["counter"] = 10
    return render_template('lock.html')