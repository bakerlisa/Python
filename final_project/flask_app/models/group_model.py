from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 

class Group:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.city = data['city']
        self.state = data['state']
        self.privacy_setting = data['privacy_setting']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def validate_group(group):
        is_valid = True # we assume this is true
        if len(group['name']) < 2:
            flash("Please name your Group. Must be atleast 3 characters.","groups")
            is_valid = False
        if len(group['city']) < 2:
            flash("Please select a city","groups")
            is_valid = False
        if len(group['state']) < 2:
            flash("Please select a state","groups")
            is_valid = False
        if len(group['privacy_setting']) < 2:
            flash("Please set your privacy settings","groups")
            is_valid = False
        return is_valid

# =============================================  
# SELECT: all groups with open privacy setting
# =============================================
    @classmethod
    def select_all_groups(cls):
        query = "SELECT * FROM groups WHERE privacy_setting = 'open';"
        results = connectToMySQL('book_club').query_db(query)

        groups = []

        for group in results:
            groups.append( cls(group) )
        return groups

# SELECT 
    @classmethod
    def get_admin_id(cls,data):
        query = "SELECT * FROM groups LEFT JOIN groups_users ON groups.id = groups_users.group_id LEFT JOIN users ON users.id = groups_users.USER_id WHERE groups.id = %(group_id)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================  
# CHECK: group name is unique
# =============================================
    @classmethod
    def unique_flocks_name(cls,data):
        query = "SELECT * FROM groups WHERE name = %(name)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================  
# CREATE: new group
# =============================================
    @classmethod
    def save_group(cls,data):
        query = "INSERT INTO groups (name, city, state, privacy_setting) VALUES (%(name)s, %(city)s, %(state)s, %(privacy_setting)s);"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================
# INSERT: creator as the admin
# =============================================
    @classmethod
    def make_creator_admin(cls,data):
        query = "INSERT INTO groups_users (group_id,user_id) VALUES (%(group_id)s , %(user_id)s)"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================
# INSERT: request to join group
# =============================================
    @classmethod
    def submit_request(cls, data):
        queryThree = "INSERT INTO messages (message,from_id) VALUE (%(message)s, %(from_id)s) WHERE user_id = %(user_id)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        flash("Request has been sent!","request")
        return results