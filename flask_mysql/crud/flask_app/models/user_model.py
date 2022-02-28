# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def save_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,created_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW());"
        new_user = connectToMySQL('users_schema').query_db(query,data)
        return new_user

    @classmethod
    def user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        user_by_id = connectToMySQL('users_schema').query_db(query,data)
        return cls(user_by_id[0])
    
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        delete_user_by_id = connectToMySQL('users_schema').query_db(query,data)
        return delete_user_by_id
    
    @classmethod
    def update_user(cla,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        update_user_id = connectToMySQL('users_schema').query_db(query,data)
        return update_user_id