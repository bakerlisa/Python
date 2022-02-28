from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.show_model import Show
from flask_app.models.user_model import User
from flask_app.models.liked_model import Likes
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ========================================
# ROUTE: add show
# ========================================
@app.route('/new')
def new_show():
    if not 'id' in session:
        flash("Please Login","info")
        return redirect('/')
    else:
        data = { "id": session['id'] }
        user_id = User.get_user_info(data)
        if not 'show' in session: 
            data = { "title" : "", "network" : "", "description" : "", "release_date" : "", "user_id" : ""}
            session["show"] = data
        return render_template("new-show.html",user_id=user_id)

# ========================================
# ROUTE: edit show
# ========================================
@app.route('/edit/<int:id>')
def edit_show(id):
    if not 'id' in session:
        flash("Please Login","info")
        return redirect('/')
    else:
        data = { "id": id }
        single_show = Show.one_shows_info(data)
        return render_template("edit.html", single_show = single_show)

# ========================================
# ROUTE : show singlw show info
# ========================================
@app.route('/show/<int:id>')
def show_single_show(id):
    if not 'id' in session:
        flash("Please Login","info")
        return redirect('/')
    else:
        data = { "id":id }
        show_data = Show.single_show_user(data)
        likes = Likes.get_all_likes(data)
        return render_template("show.html",show_data=show_data,likes=likes)

# ========================================
# ADD: new show
# ========================================
@app.route('/add_show',methods=["POST"])
def add_recipe():
    data = {
        "title" : request.form['title'],
        "network" : request.form['network'],
        "description" : request.form['description'],
        "release_date" : request.form['release_date'],
        "user_id" : request.form['user_id'],
    }
    session["show"] = data
    if not Show.validate_show(request.form):
        return redirect('/new')
    else:    
        Show.add_show(data)
        session.pop('show')
        return redirect("/dashboard")

# ========================================
# UPDATE : show
# ========================================
@app.route('/edit_show',methods=["POST"])
def edit_single_show():
    data = {
        "id" : request.form['id'],
        "title" : request.form['title'],
        "network" : request.form['network'],
        "description" : request.form['description'],
        "release_date" : request.form['release_date']
    }
    session["show"] = data

    if not Show.validate_show(request.form):
        return redirect('/new')
    else:    
        Show.edit_show(data)
        session.pop('show')
        return redirect("/dashboard")