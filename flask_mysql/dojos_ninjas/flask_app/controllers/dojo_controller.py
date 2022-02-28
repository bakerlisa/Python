from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo_model import Dojo


# ========================
# Landing/Home page Routes
# ========================
@app.route('/')
def root():
    return redirect("/dojos")

@app.route('/dojos')
def index():
    all_dojos = Dojo.get_all_dojos()
    return render_template('index.html',all_dojos = all_dojos)

# ========================
# Display all Dojos
# ========================
@app.route('/new_dojo', methods=["POST"])
def add_new_dojo():
    data = {
        "dojo_name": request.form["dojo_name"]
    }
    Dojo.create_new_dojo(data)
    return redirect("/dojos")