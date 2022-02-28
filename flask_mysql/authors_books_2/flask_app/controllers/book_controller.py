from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ====================
# get ALL book
# ====================
@app.route('/books')
def get_all_books():
    all_books = Book.get_all_books()
    return render_template('book.html', all_books = all_books)

# ====================
# create NEW book
# ====================
@app.route('/add_book', methods=["POST"])
def add_new_book():
    data = {
        "name" : request.form["name"],
        "num_pages" : request.form["num_pages"]
    }
    book_id = Book.add_book(data)
    return redirect(f"/books/{book_id}")

# ==================
# add AUTHOR w/ ID
# ==================
@app.route('/authors/<int:id>')
def authors_fav_books(id):
    data = {
        "id" : id
    }
    authors_favs = Book.get_authors_fav_books(data)
    # List of all books
    all_books = Book.get_all_books()
    # authors info
    author_id = Author.get_single_author_info(data)
    return render_template('author.html', authors_favs = authors_favs, all_books = all_books, author_id=author_id)