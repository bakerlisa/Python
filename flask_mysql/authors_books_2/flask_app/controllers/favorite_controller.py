from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.favorite_model import Favorite

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ====================
# Add AUTHOR to favs 
# ====================
@app.route('/add_to_author_fav', methods=["POST"])
def add_author_fav():
    data = {
        "author_id": request.form["author_id"],
        "book_id": request.form["book_id"]
    }
    book = request.form["book_id"]
    Favorite.new_author_fav(data)
    return redirect(f"/books/{book}")

# ====================
# Add BOOK to favs
# ====================
@app.route('/add_to_book_favorites',methods=["POST"])
def new_author_fav():
    data = {
        "author_id": request.form["author_id"],
        "book_id": request.form["book_id"]
    }
    author = request.form["author_id"]
    Favorite.new_author_fav(data)
    # print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    # print(data.author_id)
    # print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    return redirect(f"/authors/{author}")