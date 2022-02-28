from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 

from flask_app.models import user_model
from flask_app.models import show_model
class Likes:
    def __init__(self,data):
        self.user_id = data['user_id']
        self.show_id = data['show_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ========================================
# ADD: show | user in liked_shows table
# ========================================
    @classmethod
    def like_show(cls,data):
        query = "INSERT INTO liked_shows (user_id, show_id) VALUES (%(user_id)s,%(show_id)s);"
        results = connectToMySQL('shows').query_db(query,data)
        return results

# ========================================
# DELETE: show | user in liked_shows table
# ========================================
    @classmethod
    def unlike_show(cls,data):
        query = "DELETE FROM liked_shows WHERE user_id =  %(user_id)s and show_id = %(show_id)s;"
        results = connectToMySQL('shows').query_db(query,data)
        return results

# ========================================
# DELETE: show,user,likes data | m:m
# ========================================
    @classmethod
    def get_all_shows_info(cls):
        query = "SELECT * FROM shows LEFT JOIN users ON shows.id = users.id LEFT JOIN liked_shows ON liked_shows.show_id = shows.id;"
        results = connectToMySQL('shows').query_db(query)
        
        all_likes = []

        for row in results:
            one_like = cls(row)

            one_user = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            one_like.user = user_model.User(one_user)

            one_show = {
                "id" : row ["id"],
                "title" : row ["title"],
                "network" : row ["network"],
                "description" : row ["description"],
                "likes" : row ["likes"],
                "release_date" : row ["release_date"],
                "created_at" : row ["created_at"],
                "updated_at" : row ["updated_at"],
                "user_id" : row ["user_id"]
            }
            one_like.show = show_model.Show(one_show)
            
            all_likes.append(one_like)
            print(row)
        return all_likes

# ========================================
# GET : all likes
# ========================================
    @classmethod
    def get_all_likes(cls,data):
        query = "SELECT COUNT(*) AS count FROM liked_shows  LEFT JOIN shows ON shows.id = liked_shows.show_id LEFT JOIN users ON shows.user_id = users.id WHERE liked_shows.show_id = %(id)s;"
        results = connectToMySQL('shows').query_db(query,data)
        return results