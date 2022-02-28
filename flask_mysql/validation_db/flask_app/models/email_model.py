from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# from flask import flash - put this at the top
# this is the method: change name, change messages
    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        elif len(Email.unique_email(data = {"email": email['email']})) > 3: 
            flash("Your email is not unique")
            is_valid = False
        else:
            flash("Your email has been approved!")
        return is_valid

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('emails').query_db(query)

        emails = []

        for email in results:
            emails.append( cls(email) )
        return emails

    @classmethod
    def add_new_email(cls,data): 
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        results = connectToMySQL('emails').query_db(query,data)
        return results
    
    @classmethod
    def unique_email(cls,data):
        query = "SELECT * FROM emails WHERE email = %(email)s"
        results = connectToMySQL('emails').query_db(query,data)
        return results
    
    @classmethod
    def delete_address(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s"
        results = connectToMySQL('emails').query_db(query,data)
        return results