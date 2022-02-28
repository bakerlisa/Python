from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User

@app.route("/")
def root():
    users = User.get_all_users()
    return render_template("index.html", users=users)
        
@app.route("/add_user")
def add_user():
    return render_template("create.html")

@app.route('/new_user',methods=["POST"])
def new_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save_user(data)
    return redirect('/')

@app.route("/update_user/<int:id>",methods=["POST"])
def update_user(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.update_user(data)
    return redirect("/")

@app.route('/<int:id>')
def profile_pic(id):
    data = {
        "id": id
    }
    user_id = User.user_by_id(data)
    return render_template("read.html", user_id=user_id)

@app.route('/edit/<int:id>')
def edit_profile(id):
    data = {
        "id":id
    }
    user_id = User.user_by_id(data)
    return render_template("edit.html",user_id = user_id)

@app.route('/delete/<int:id>')
def delete_profile(id):
    data = {
        "id": id
    }
    User.delete_user(data)
    return redirect("/")