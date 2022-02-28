from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
from datetime import datetime

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ========================================
# Route: create new recipe page
# ========================================
@app.route('/create')
def create_recipe():
    if not 'id' in session:
        flash("Please Login","info")
        return redirect('/')
    else:
        data = { "id": session['id'] }
        user_id = User.get_user_info(data)
        if not 'dessert' in session: 
            data = { "name" : "", "description" : "", "instruction" : "", "under_30" : "", "made_on" : ""}
            session["dessert"] = data
        return render_template("recipes.html",user_id=user_id)

@app.route('/edit/<int:id>')
def edit_recipe(id):
    if not 'id' in session:
        flash("Please Login","info")
        return redirect('/')
    else:
        data = { "id": session['id'] }
        user_id = User.get_user_info(data)
        recipe = Recipe.single_recipe(data = { "id":id})
        return render_template("edit.html", recipe = recipe, user_id = user_id)

# ========================================
# ADD: new recipe
# ========================================
@app.route('/add_recipe',methods=["POST"])
def add_recipe():
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instruction" : request.form['instruction'],
        "under_30" : request.form.get('under_30'),
        "made_on" : request.form['made_on']
    }
    session["dessert"] = data
    if not Recipe.validate_recipe(request.form):
        return redirect('/create')
    else:    
        session.pop('dessert')
        new_recipe_id = Recipe.add_recipe(data)
        return redirect(f"/recipes/{new_recipe_id}")

# ========================================
# View Page for single recipes
# ========================================
@app.route('/recipes/<int:id>')
def single_reciepe(id):
    if not 'id' in session:
        flash("Please Login","info")
        return redirect('/')
    else:
        recipe_id = Recipe.single_recipe(data = { "id":id})
        user_id = User.get_user_info(data = {"id" : session["id"]})
        return render_template("single_recipe.html",recipe_id = recipe_id,user_id=user_id)

# ========================================
# DELETE: Recipe
# ========================================
@app.route('/delete/<int:id>')
def delete(id):
    data = { "id" : id } 
    Recipe.delete_recipe(data)
    return redirect('/dashboard')


@app.route('/update_recipe',methods=["POST"])
def update_recipe():
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "under_30": request.form.get('under_30'),
        "made_on": request.form['made_on']
    }
    Recipe.update_recipe(data)
    return redirect(f'/recipes/{data["id"]}')