from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self,data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']

    @classmethod
    def new_author_fav(cls,data):
        query = "INSERT INTO authors_has_books (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        new_fav_id = connectToMySQL('books_authors').query_db(query,data)
        return new_fav_id