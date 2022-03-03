from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.isbn = data['isbn']
        self.page_num = data['page_num']
        self.link = data['link']
        self.series_num = data['series_num']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def validate_book(book):
        is_valid = True # we assume this is true
        if len(book['title']) < 3:
            flash("Title must be at least 3 characters.","books")
            is_valid = False
        if len(book['first_name']) < 3:
            flash("Author first name must be at least 3 characters.","books")
            is_valid = False
        if len(book['last_name']) < 3:
            flash("Author last name must be at least 3 characters.","books")
            is_valid = False
        if len(book['isbn']) < 10:
            flash(f"ISBN must be 13 characters long. Your's is {len(book['isbn'])}","books")
            is_valid = False
        if len(book['img']) < 3:
            flash("Please add an image URL","books")
            is_valid = False
        if len(book['series_name']) > 1 and len(book['num_series']) == 0:
            flash("You've marked this book in a series. Please input what number in the series it is OR leave blank","books")
            is_valid = False
        return is_valid

# =============================================  
# SELECT: is ISBN unique
# =============================================  
    @classmethod
    def is_isbn_unique(cls,data):
        query = "SELECT * FROM books WHERE isbn = %(isbn)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================  
# INSER: new book
# =============================================   
    @classmethod
    def add_new_book(cls,data):
        query = "INSERT INTO books (title,isbn,img,page_num,link) VALUES (%(title)s, %(isbn)s, %(img)s, %(page_num)s,%(link)s);"
        results = connectToMySQL('book_club').query_db(query,data)
        return results
