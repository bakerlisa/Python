from flask import Flask, render_template,redirect,request
# import the class from friend.py
from users import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all_users()
    return render_template("index.html", users = users)

@app.route("/add_user")
def add_user():
    return render_template("create.html")

@app.route('/new_user', methods=["POST"])
def new_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    new_user = User.save_user(data)
    return redirect("/")

@app.route("/<int:id>")
def profile_page(id):
    data = {
        "id":id
    }
    user_id = User.get_user_by_id(data)
    return render_template("read.html", user_id = user_id)

if __name__ == "__main__":
    app.run(debug=True,port=5001)

