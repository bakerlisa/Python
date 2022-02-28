from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Login:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.gender = data['gender']
        self.password = data['password']
        self.confirm_password = data['confirm_password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # this is the method: change name, change messages
    @staticmethod
    def validate_registration(login):
        is_valid = True # we assume this is true
        if len(login['first_name']) < 2:
            flash("First Name must be at least 2 characters","reg")
            is_valid = False
        if len(login['last_name']) < 2:
            flash("Last Name must be at least 2 characters","reg")
            is_valid = False
        if not EMAIL_REGEX.match(login['email']):
            flash("Please put in a vaild email","reg")
            is_valid = False
        if len(login['password']) < 8:
            flash("Password must be at least 8 characters long","reg")
            is_valid = False
        if re.search('[0-9]',login['password']) is None:
            flash("Make sure your password has a number","reg")
            is_valid = False
        if re.search('[A-Z]',login['password']) is None:
            flash("Make sure your password has a capital letter","reg")
            is_valid = False
        if not login['password'] == login['confirm_password']:
            flash("Passwords do not match","reg")
            is_valid = False
        return is_valid
    
    
    # Get all users
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM login;"
        results = connectToMySQL('login').query_db(query)

        users = []

        for user in results:
            users.append( cls(user) )
        return users
    
    # Create New User
    @classmethod
    def new_registration(cls,data):
        query = "INSERT INTO login (first_name,last_name,email,gender,password,confirm_password) VALUES (%(first_name)s, %(last_name)s,%(email)s,%(gender)s,%(password)s,%(confirm_password)s);"
        results = connectToMySQL('login').query_db(query,data)
        return results

    #Get Singel user info
    @classmethod
    def get_user_info(cls,data):
        query = "SELECT * FROM login WHERE id = %(id)s;"
        results = connectToMySQL('login').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM login WHERE email = %(email)s"
        result = connectToMySQL('login').query_db(query,data)
        if not result:
            return "0"
        else:        
            return cls(result[0])
    
    @classmethod
    def delete_account(cls,data):
        query = "DELETE FROM login WHERE id = %(id)s"
        result = connectToMySQL('login').query_db(query,data)
        return result