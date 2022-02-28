from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book_model


class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_authors').query_db(query)

        authors = []

        for author in results:
            authors.append( cls(author) )
        return authors
    
    # ====================
    # save new AUTHOR
    # ====================
    @classmethod
    def save_new_author(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        new_author_id = connectToMySQL('books_authors').query_db(query,data)
        return new_author_id

    # ====================
    # Get all the authors who've faved this book
    # ====================
    @classmethod
    def get_all_book_author_fav(cls,data):
        query = "SELECT * FROM authors LEFT JOIN authors_has_books ON authors.id = authors_has_books.author_id LEFT JOIN  books ON authors_has_books.book_id = books.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_authors').query_db(query,data)

        book_authors_faved = []
        for row in results:
            one_author = cls(row)

            book_info = {
                "id" : row["books.id"],
                "name" : row["books.name"],
                "num_pages" : row["num_pages"],
                "created_at" : row["books.created_at"],
                "updated_at" : row["books.updated_at"]
            }

            one_author.book = book_model.Book(book_info)
            book_authors_faved.append(one_author)
        return book_authors_faved

    #Single Author Info
    @classmethod
    def get_single_author_info(cls,data):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        results = connectToMySQL('books_authors').query_db(query,data)
        return cls(results[0])

