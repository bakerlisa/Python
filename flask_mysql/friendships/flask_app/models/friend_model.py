from flask_app.config.mysqlconnection import connectToMySQL

# from flask_app import app
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

class Friend:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# =================================
# GET: users/Friends
# =================================
    @classmethod
    def all_people(cls):
        query = "SELECT * FROM friend;"
        results = connectToMySQL('friendships').query_db(query)

        friends = []

        for friend in results:
            friends.append( cls(friend))
        return friends
        

# =================================
# GET: everyone who's not a friend
# =================================
    # @classmethod
    # def not_friends(cls,data):
    #     query = "SELECT * FROM friend LEFT JOIN users ON friend.id = users.user_id WHERE users.user_id != %(id)s UNION SELECT * FROM friend LEFT JOIN users ON friend.id = users.user_id WHERE users.user_id is NULL ORDER BY first_name GROUP BY first_name"
    #     results = connectToMySQL('friendships').query_db(query,data)
    #     return results

# =================================
# GET: Single persons freindshps  
# =================================
    @classmethod
    def get_all_friends(cls,data):
        query = "SELECT friend.id, friend.first_name, friend.last_name, friend2.first_name AS friend_frist, friend2.last_name AS friend_last, friend2.id as friend_id FROM friend  LEFT JOIN users ON friend.id = users.user_id LEFT JOIN friend as friend2 ON friend2.id = users.friend_id WHERE friend.id = %(id)s"
        results = connectToMySQL('friendships').query_db(query,data)
        return results
        
# =================================
# GET: all users
# =================================
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM friend;"
        results = connectToMySQL('friendships').query_db(query)
        return results


# =================================
# GET: all friendship relationships  
# =================================
    @classmethod
    def get_all_friendships(cls):
        query = "SELECT friend.id, friend.first_name, friend.last_name, friend2.first_name AS friend_frist, friend2.last_name AS friend_last, friend2.id as friend_id FROM friend   JOIN users ON friend.id = users.user_id  JOIN friend as friend2 ON friend2.id = users.friend_id ORDER BY first_name;"
        results = connectToMySQL('friendships').query_db(query)
        return results

# =================================
# GET: 1 users data
# =================================
    @classmethod
    def user_info(cls,data):
        query = "SELECT * FROM friend WHERE id = %(id)s;"
        results = connectToMySQL('friendships').query_db(query,data)
        return cls(results[0])

# =================================
# ADD: person
# =================================
    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO friend (first_name,last_name) VALUE (%(first_name)s,%(last_name)s);"
        results = connectToMySQL('friendships').query_db(query,data)
        return results

# =================================
# ADD: friendship
# =================================
    @classmethod
    def add_friendship(cls,data):
        query = "INSERT INTO users (friend_id,user_id) VALUES (%(friend_id)s,%(user_id)s);"
        results = connectToMySQL('friendships').query_db(query,data)
        return results

    