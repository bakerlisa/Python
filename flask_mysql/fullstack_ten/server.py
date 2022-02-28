from flask import Flask, render_template,request, redirect,session
# import the class from friend.py
from clients import Client

app = Flask(__name__)
@app.route("/")
def root():
    # call the get all classmethod to get all friends
    clients = Client.get_all_clients()
    return render_template("index.html",clients = clients)


@app.route("/<int:id>")
def show_client_info(id):
    data = {
        "id": id
    }
    client_info = Client.get_client_info(data)
    return render_template("client_page.html", client_info = client_info )

@app.route("/new_client")
def new_client():
    return render_template("new_client.html")

@app.route("/add_new_client",methods=["POST"])
def add_new_client():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    Client.add_client(data)
    return redirect("/")








if __name__ == "__main__":
    app.run(debug=True, port=5001)

