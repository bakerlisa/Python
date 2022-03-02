from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 

class Genre:
    def __init__(self,data):
        self.id = data['id']
        self.genre = data['genre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ==========================================
# SELECT : check to see if gener exsists
# ==========================================
    @classmethod
    def category_exsist(cls,data):
        query = "SELECT * FROM book_genre WHERE genre = %(genre)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results
    
# ==========================================
# INSERT: new gener
# ==========================================
    @classmethod
    def add_new_genre(cls,data):
        query = "INSERT INTO book_genre (genre,book_id) VALUES (%(genre)s,%(book_id)s);"
        results = connectToMySQL('book_club').query_db(query,data)
        return results