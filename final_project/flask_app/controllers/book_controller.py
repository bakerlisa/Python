from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book_model import Book
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

@app.route('/search')
def search():
    return render_template('search.html')