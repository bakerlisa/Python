from flask_app import app
from flask import render_template, request, redirect

# import the class from friend.py
from flask_app.models.friend import Friend


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.all_friends()
    return render_template("index.html", all_friends = friends)

# ====================================
# Show One Friend Route
# ====================================

@app.route("/<int:friend_id>")
def show_friend(friend_id):
    data = {
        "id" : friend_id
    }
    friend = Friend.one_friend(data)
    return render_template("show_one.html", one_friend = friend)

# ====================================
# Add Friend Routes
# ====================================

@app.route("/new_friend")
def new_friend():
    return render_template("new_friend.html")

@app.route("/create_friend", methods=["POST"])
def create_friend():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "occupation" : request.form["occ"]
    }
    friend_id = Friend.save_friend(data)
    return redirect(f"/{friend_id}")