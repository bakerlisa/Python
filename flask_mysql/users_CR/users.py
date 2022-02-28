# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,created_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW())"
        new_user = connectToMySQL('users_schema').query_db(query,data)
        return new_user
    
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        user_id = connectToMySQL('users_schema').query_db(query,data)
        print(cls(user_id[0]))
        return cls(user_id[0])