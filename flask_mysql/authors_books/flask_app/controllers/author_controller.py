from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author_model import Author
from flask_app.models.favorite_model import Favorite

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ==============================
# home route
# ==============================
@app.route('/')
def index():
    return redirect('/authors')

# ==============================
# Get All Authors
# ==============================
@app.route('/authors')
def authors():
    all_authors = Author.get_all_authors()
    return render_template('index.html', all_authors = all_authors)

@app.route('/authors/<int:id>')
def get_author_info(id):
    # author_favs_list = Favorite.author_fav_books()
    author = Author.get_inv_author()
    return render_template("author.html", author_favs_list = author_favs_list, id=id)

# ==============================
# Add AUTHOR
# ==============================
@app.route('/add_author', methods=["POST"])
def add_author():
    data = {
        "name": request.form["name"]
    }
    new_author_id = Author.create_new_author(data)
    print(new_author_id)
    return redirect(f"/authors/{new_author_id}")


