from flask_app.config.mysqlconnection import connectToMySQL


class Book:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.num_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_authors').query_db(query)

        books = []

        for book in results:
            books.append( cls(book) )
        return books
    
    @classmethod
    def create_new_book(cls,data):
        query = "INSERT INTO books (name,num_pages) VALUES (%(name)s,%(num_pages)s);"
        results = connectToMySQL('books_authors').query_db(query,data)
        return results