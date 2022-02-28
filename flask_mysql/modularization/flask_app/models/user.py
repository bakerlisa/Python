from flask_app.config.mysqlconnection import MySQLConnection

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
    def get_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        indv_user = connectToMySQL('users_schema').query_db(query,data)
        return cls(indv_user[0])

    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET id = %(id)s, first_name = %(first_name)s, last_name = %(last_name)s,updated_at = NOW() WHERE id = %(id)s;"
        indv_user = connectToMySQL('users_schema').query_db(query,data)
        return indv_user
    
    @classmethod 
    def new_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,created_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW())"
        new_user = connectToMySQL('users_schema').query_db(query,data)
        return new_user
    
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        del_user = connectToMySQL('users_schema').query_db(query,data)
        return del_user