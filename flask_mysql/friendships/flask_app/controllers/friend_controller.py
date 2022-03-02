from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.friend_model import Friend

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# =================================
# GET: routes
# =================================
@app.route('/')
def index():
    session.clear()		# clears all keys
    return redirect('/friendship')

@app.route('/friendship')
def friendships():
    all_friends = Friend.get_all_friendships()
    return render_template('index.html')

# =================================
# GET: all friennds
# =================================
@app.route('/friendships')
def show_all_friends():
    if 'id' in session:
        data = {"id" : session["id"]}
        user_id = Friend.user_info(data) 
        all_friends = Friend.get_all_friends(data)
        return render_template('friendships.html',user_id = user_id, all_friends = all_friends)
    else:
        return redirect('/')

# =================================
# ADD: User
# =================================
@app.route('/add_user', methods=["POST"])
def add_new_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"]
    }
    new_user_id = Friend.add_user(data)
    session["id"] = new_user_id
    return redirect('/friendships')

# =================================
# ADD: friendship
# =================================
@app.route('/<int:id>')
def add_friendship(id):
    if "id" in session:
        data = {
            "friend_id": id,
            "user_id": session["id"]
        }
        friendship = Friend.add_friendship(data)
        return redirect(f"/friendships")
    else:
        return redirect('/')

# =================================
# ADD: home page -> add relationship
# =================================
@app.route('/create_friendship',methods=["POST"])
def create_friendship():
    data = {
        "friend_id": request.form["friend_id"],
        "user_id": request.form["user_id"]
    }
    friendship = Friend.add_friendship(data)
    session["id"] =  request.form["user_id"]
    return redirect("/friendships")
