from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

# === 1. Remember to import file on server.py 
# === Note: Controllers pull in classes


# ==================
# HOME routes
# ==================
@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def get_authors():
    authors = Author.get_all_authors()
    return render_template('index.html', authors = authors)

# ==================
# add AUTHOR
# ==================
@app.route('/add_author',methods=["POST"])
def add_author():
    data = {
        "name" : request.form["name"]
    }
    new_author = Author.save_new_author(data)
    return redirect(f"/authors/{new_author}")

# ====================
# route in indv book page
# and get all authors from ^^ class
# ====================
@app.route("/books/<int:id>")
def indv_book_info(id):
    data = {
        "id": id
    }
    #Gets all th authors that faved this book
    all_book_author_favs = Author.get_all_book_author_fav(data)
    # returns all authors
    authors = Author.get_all_authors()
    #retrun book info:  was doing on Join call, but then got 0 info back for books that weren't faved 
    book_info = Book.get_single_book_info(data)

    return render_template("indv_book.html", all_book_author_favs = all_book_author_favs, authors = authors, book_info = book_info)

