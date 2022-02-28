from flask_app.config.mysqlconnection import connectToMySQL

import re
from flask import flash 

from flask_app.models import user_model

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+[a-zA-Z]+$')

class Show:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.description = data['description']
        self.likes = data['likes']
        self.release_date = data['release_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate_show(show):
        is_valid = True # we assume this is true
        if len(show['title']) < 3:
            flash("Title must be at least 3 characters.","show")
            is_valid = False
        if len(show['network']) < 3:
            flash("Network must be at least 3 characters.","show")
            is_valid = False
        if len(show['description']) < 10:
            flash("Description must be at least 10 characters.","show")
            is_valid = False
        if len(show['release_date']) < 2:
            flash("Plase input a valid date","show")
            is_valid = False
        return is_valid

# ========================================
# GET: all shows from single user
# ========================================
    @classmethod
    def get_users_shows(cls,data):
        query = "SELECT * FROM shows LEFT JOIN users ON users.id = shows.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL('shows').query_db(query,data)

        shows = []

        for show in results:
            shows.append( cls(show) )
        return shows

# ========================================
# GET: single show data by users.id
# ======================================== 
    @classmethod
    def one_shows_info(cls,data):
        query = "SELECT * FROM shows LEFT JOIN users ON users.id = shows.user_id WHERE shows.id = %(id)s;"
        results = connectToMySQL('shows').query_db(query,data)
        return cls(results[0])

# ========================================
# GET: single show && single user
# ========================================
    @classmethod
    def single_show_user(cls,data):
        query = "SELECT * FROM shows LEFT JOIN users ON shows.user_id = users.id WHERE shows.id = %(id)s;"
        results = connectToMySQL('shows').query_db(query,data)

        all_shows_users = []

        for row in results:
            one_show = cls(row)

            user_data = {
                "id" : row["id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            one_show.user = user_model.User(user_data)
            
            all_shows_users.append(one_show)
        return all_shows_users[0]
    
# ========================================
# GET: take two : single show && single user
# ========================================   
    @classmethod
    def single_show_user_take_two(cls,data):
        query = "SELECT * FROM liked_shows LEFT JOIN shows ON shows.id = liked_shows.show_id LEFT JOIN users  ON shows.user_id = users.id  WHERE liked_shows.user_id = %(id)s;"
        results = connectToMySQL('shows').query_db(query,data)

        all_shows_users = []

        for row in results:
            one_show = cls(row)

            user_data = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            one_show.user = user_model.User(user_data)

            show_data = {
                "id" : row ['shows.id'],
                "title" : row ['title'],
                "network" : row ['network'],
                "description" : row ['description'],
                "likes" : row ['likes'],
                "release_date" : row ['release_date'],
                "created_at" : row ['shows.created_at'],
                "updated_at" : row ['shows.updated_at'],
                "user_id" : row ['user_id']
            }
            one_show.user = show_model.Show(show_data)
            
            all_shows_users.append(one_show)
        return all_shows_users

# ========================================
# GET: all shows with user info 
# ======================================== 
    @classmethod
    def get_db_shows(cls):
        query = "SELECT * FROM shows LEFT JOIN users ON users.id = shows.user_id;"
        results = connectToMySQL('shows').query_db(query)

        all_shows = []

        for row in results:
            single_show = cls(row)

            user_data = {
                "id" : row["id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "release_date" : row["users.release_date"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            single_show.user = user_model.User(user_data)
            
            all_shows.append(single_show)
        return results

# ========================================
# GET: all shows
# ========================================
    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows"
        results = connectToMySQL('shows').query_db(query)
        return results

# ========================================
# CREATE: new show
# ========================================
    @classmethod
    def add_show(cls,data):
        query = "INSERT INTO shows (title,network,description,release_date,user_id) VALUES (%(title)s,%(network)s,%(description)s,%(release_date)s,%(user_id)s);"
        results = connectToMySQL('shows').query_db(query,data)
        return results

# ========================================
# UPDATE: show
# ========================================
    @classmethod
    def edit_show(cls,data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, description = %(description)s, release_date = %(release_date)s WHERE id = %(id)s;"
        results = connectToMySQL('shows').query_db(query,data)
        return results


# ========================================
# DELETE: show
# ========================================
    @classmethod
    def delete_show(cls,data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        results = connectToMySQL('shows').query_db(query,data)
        return results



