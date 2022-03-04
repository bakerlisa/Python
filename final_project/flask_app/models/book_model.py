from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 

from flask_app.models import book_author_model
from flask_app.models import author_model

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.isbn = data['isbn']
        self.page_num = data['page_num']
        self.description = data['description']
        self.link = data['link']
        self.img = data['img']
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
# SELECT: all genres
# ============================================= 
    @classmethod
    def get_all_genres(cls,data):
        query = "SELECT genre.genre FROM books_genres LEFT JOIN genre ON genre.id = books_genres.genre_id WHERE books_genres.book_id = %(id)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================  
# SELECT: Single book by ID
# =============================================  
    @classmethod
    def get_book_info(cls,data):
        query = "SELECT * FROM books LEFT JOIN books_authors ON  books_authors.book_id = books.id LEFT JOIN authors ON books_authors.author_id = authors.id WHERE books.id =  %(id)s;"
        results = connectToMySQL('book_club').query_db(query,data)

        book_information = []

        for row in results:
            one_book = cls(row)

            one_book_author = {
                "book_id" : row['book_id'],
                "author_id" : row['author_id'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            one_book.book_author = book_author_model.Book_Author(one_book_author)
            
            one_author = {
                "id": row['authors.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            one_book.author = author_model.Author(one_author)
            
            book_information.append(one_book)
        return book_information


    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books LEFT JOIN books_authors ON books_authors.book_id = books.id LEFT JOIN authors ON authors.id = books_authors.author_id;"
        results = connectToMySQL('book_club').query_db(query)

        all_new_book_information = []

        for row in results:
            one_book = cls(row)

            one_book_author = {
                "book_id" : row['book_id'],
                "author_id" : row['author_id'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            one_book.book_author = book_author_model.Book_Author(one_book_author)
            
            one_author = {
                "id": row['id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            one_book.author = author_model.Author(one_author)
            
            all_new_book_information.append(one_book)
        
        return all_new_book_information

# =============================================  
# INSERT: new book
# =============================================   
    @classmethod
    def add_new_book(cls,data):
        query = "INSERT INTO books (title,isbn,img,page_num,link) VALUES (%(title)s, %(isbn)s, %(img)s, %(page_num)s,%(link)s);"
        results = connectToMySQL('book_club').query_db(query,data)
        return results
    
