from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.num_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ====================
    # return all BOOKS
    # ====================
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_authors').query_db(query)

        books = []

        for book in results:
            books.append( cls(book) )
        return books

    # ====================
    # create new book
    # ====================
    @classmethod
    def add_book(cls,data):
        query = "INSERT INTO books (name, num_pages) VALUES (%(name)s,%(num_pages)s);"
        new_book_id = connectToMySQL('books_authors').query_db(query,data)
        return new_book_id

    @classmethod
    def get_authors_fav_books(cls,data):
        query = "SELECT * FROM books LEFT JOIN authors_has_books ON books.id = authors_has_books.book_id LEFT JOIN  authors ON authors_has_books.author_id = authors.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_authors').query_db(query,data)

        authors_faved_books = []
        for row in results:
            one_book = cls(row)

            author_info = {
                "id" : row['id'],
                "name" : row['name'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }

            one_book.author = author_model.Author(author_info)
            authors_faved_books.append(one_book)
        return authors_faved_books

    @classmethod
    def get_single_book_info(cls,data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        book_id = connectToMySQL('books_authors').query_db(query,data)
        print(cls(book_id[0]))
        return cls(book_id[0])
        

