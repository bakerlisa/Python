from flask_app.config.mysqlconnection import connectToMySQL

class Name:
    def __init__(self,data):
        self.name = data['name']

    @classmethod
    def name(cls,data):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)

        friends = []

        for friend in results:
            friends.append( cls(friend) )
        return friends
