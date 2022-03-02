from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 

class Series:
    def __init__(self,data):
        self.id = data['id']
        self.series_name = data['series_name']
        self.book_id = data['book_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def is_series_unique(cls,data):
        query = "SELECT * FROM book_series WHERE series_name = %(series_name)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

    @classmethod
    def add_new_series(cls,data):
        query = "INSERT INTO book_series (series_name,book_id) VALUES(%(series_name)s,%(book_id)s);"
        results = connectToMySQL('book_club').query_db(query,data)
        return results



