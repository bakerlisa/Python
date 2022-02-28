from flask import Flask, render_template,redirect,request
# import the class from friend.py

from friends import Friend
app = Flask(__name__)

@app.route("/")
def root():
    # call the get all classmethod to get all friends
    friends = Friend.get_all_friends()
    return render_template("index.html",friends = friends)

# ==============================
# ADDING A FRIEND     
# ==============================
@app.route("/add_friend")
def add_friend():
    return render_template("add-friend.html")

@app.route("/create_friend", methods=["POST"])

def create_friend():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "occ": request.form["occ"]
    }
    new_friend = Friend.save_friend(data)
    return redirect("/")

# ==============================
# Route each Friend  
# ==============================
@app.route("/<int:id>")
def indv_friend_page(id):
    data = {
        "id" : id
    }
    indv_friend_id = Friend.indv_friend(data)
    return render_template("profile_page.html", indv_friend_id = indv_friend_id)










if __name__ == "__main__":
    app.run(debug=True,port=5001)

