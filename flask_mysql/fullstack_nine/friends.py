# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_friends(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('mydb').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @classmethod
    def indv_friend(cls,data):
        query = "SELECT * FROM friends WHERE id = %(id)s"
        indv_friend_id = connectToMySQL('mydb').query_db(query,data)
        return cls(indv_friend_id[0])
    
    @classmethod
    def save_friend(cls, data):
        query = "INSERT INTO friends (first_name,last_name,occupation) VALUES (%(first_name)s, %(last_name)s, %(occ)s);"
        new_friend = connectToMySQL('mydb').query_db(query,data)
        return new_friend
        