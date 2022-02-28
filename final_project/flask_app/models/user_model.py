from flask_app.config.mysqlconnection import connectToMySQL

import re
from flask import flash 

from flask_app.models import group_model

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone = data['phone']
        self.password = data['password']
        self.profile_image = data['profile_image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2:
            flash("Frist name must be at least 3 characters.","error")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 3 characters.","error")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Last name must be at least 3 characters.","error")
            is_valid = False
        if len(user['password']) < 8:
            flash("password must be at least 8 characters long","error")
            is_valid = False
        if re.search('[0-9]',user['password']) is None:
            flash("Passwords must have a number","error")
            is_valid = False
        if re.search('[A-Z]',user['password']) is None:
            flash("Passwords must have a captial letter","error")
            is_valid = False
        if not user['password'] == user['confirm_password']:
            flash("Passwords must match","error")
            is_valid = False
        return is_valid

# ==========================================
# GET: all users
# ==========================================
    @classmethod
    def get_all_users(cls,data):
        query = "SELECT * FROM users WHERE id != %(id)s ORDER BY first_name;"
        results = connectToMySQL('book_club').query_db(query,data)

        users = []

        for user in results:
            users.append( cls(user) )
        return users

# ========================================
# GET: admin user for goup
# ========================================
    @classmethod
    def user_by_id(data):
        query =  "SELECT * FROM flocks LEFT JOIN groups_users ON flocks.id = groups_users.group_id LEFT JOIN users ON users.id = groups_users.user_id WHERE flocks.id = %(id)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# ========================================
# GET: one user info with group info
# ========================================
    @classmethod
    def get_user_info(cls,data):
        query = "SELECT * FROM users LEFT JOIN groups_users ON users.id = groups_users.user_id  LEFT JOIN flocks ON groups_users.group_id = flocks.id WHERE users.id = %(id)s;"
        results = connectToMySQL('book_club').query_db(query,data)

        all_user_info = []

        for row in results:
            one_user = cls(row)

            group_data = {
                "id" :  row['flocks.id'],
                "name" :  row['name'],
                "city" :  row['city'],
                "state" :  row['state'],
                "privacy_setting" :  row['privacy_setting'],
                "created_at" :  row['flocks.created_at'],
                "updated_at" :  row['flocks.updated_at']
            }

            one_user.group = group_model.Group(group_data)

            all_user_info.append(one_user)
        return cls(results[0])


# ========================================
# CREATE: new user
# ========================================   
    @classmethod
    def create_new_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# ========================================  
# UPDATE: message count
# ========================================  
    @classmethod
    def increment_messge_cout(cls,data):
        query = "UPDATE users SET message_count = message_count + 1 WHERE id = %(id)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# ========================================
# VALIDATION: by uer email
# ========================================
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        if not results:
            return "0"
        else:        
            return cls(results[0])