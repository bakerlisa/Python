from flask import Flask, render_template,redirect,session,request
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def root():
    users = User.get_all_users()
    return render_template("index.html", users=users)

@app.route("/<int:id>")
def user_profile(id):
    data = {
        "id": id
    }
    indv_user = User.get_user(data)
    return render_template("users.html", indv_user = indv_user)

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id": id,
    }
    indv_user = User.get_user(data)
    return render_template("edit.html",indv_user = indv_user)

@app.route("/update_user/<int:id>",methods=["POST"])
def update_user(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update_user(data)
    return redirect("/")

@app.route('/add_user')
def add_user():
    return render_template("new_user.html")

@app.route('/new_user',methods=["POST"])
def new_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
    }
    User.new_user(data)
    return redirect("/")
    
@app.route("/delete/<int:id>")
def delete_user(id):
    data = {
        "id": id
    }
    User.delete_user(data)
    return redirect('/')