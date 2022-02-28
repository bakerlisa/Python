from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book_model import Book

# ==============================
# List ALL books
# ==============================
@app.route('/books')
def books():
    all_books = Book.get_all_books()
    return render_template('book.html',all_books = all_books)

# ==============================
# List INDV book by ID
# ==============================
@app.route('/books/<int:id>')
def indv_book_route(id):
    # Add Class to pull book info
    return render_template("/indv_book.html")

# Add new Book
@app.route('/add_book', methods=["POST"])
def add_new_book():
    data = {
        "name": request.form['name'],
        "num_pages": request.form['num_pages']
    }
    new_book_id = Book.create_new_book(data)
    return render_template("indv_book.html",new_book_id = new_book_id)