from flask_app.config.mysqlconnection import connectToMySQL

import re
from flask import flash 


class GroupUser:
    def __init__(self,data):
        self.user_id = data['user_id']
        self.group_id = data['group_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def name(cls,data):
    #     query = "SELECT * FROM friends;"
    #     results = connectToMySQL('first_flask').query_db(query)

    #     friends = []

    #     for friend in results:
    #         friends.append( cls(friend) )
    #     return friends