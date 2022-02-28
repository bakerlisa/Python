from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

# ========================
# Add ninja route button
# ========================
@app.route('/add_ninja')
def add_ninja():
    all_ninjas = Ninja.get_all_ninjas()
    get_all_dojos = Dojo.get_all_dojos()
    return render_template('ninjas.html', all_ninjas = all_ninjas,get_all_dojos = get_all_dojos)

# ========================
# Create New Ninja
# ========================
@app.route('/create_new_ninja', methods=["POST"])
def create_new_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
    }
    
    Ninja.create_new_ninja(data)
    return redirect("/")

# ========================
# Indv Dojo Page / Studnet list page with Dojo ID
# ========================
@app.route('/<int:id>')
def indv_dojo_page(id):
    data = {
        "id":id
    }
    ninjas_in_dojo = Ninja.get_all_dojos_ninjas(data)
    return render_template("dojo.html", ninjas_in_dojo = ninjas_in_dojo)