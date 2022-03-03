from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 

class Book_Genre:
    def __init__(self,data):
        self.id = data['id']
        self.book_id = data['book_id']
        self.genre_id = data['genre_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_new_book_genre(cls,data):
        query = "INSERT INTO books_genres (book_id,genre_id) VALUES (%(book_id)s,%(genre_id)s);"
        results = connectToMySQL('book_club').query_db(query,data)
        return results