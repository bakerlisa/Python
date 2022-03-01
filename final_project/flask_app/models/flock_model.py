from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 

class Flock:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.city = data['city']
        self.state = data['state']
        self.privacy_setting = data['privacy_setting']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def validate_flock(flock):
        is_valid = True # we assume this is true
        if len(flock['title']) < 2:
            flash("Please name your Group. Must be atleast 3 characters.","flocks")
            is_valid = False
        if len(flock['city']) < 2:
            flash("Please select a city","flocks")
            is_valid = False
        if len(flock['state']) < 2:
            flash("Please select a state","flocks")
            is_valid = False
        return is_valid

# =============================================  
# SELECT: all groups with open privacy setting
# =============================================
    @classmethod
    def select_all_groups(cls):
        query = "SELECT * FROM flocks WHERE privacy_setting = 'open';"
        results = connectToMySQL('book_club').query_db(query)

        groups = []

        for group in results:
            groups.append( cls(group) )
        return groups

# =============================================
# SELECT 
# =============================================
    @classmethod
    def get_admin_id(cls,data):
        query = "SELECT * FROM flocks LEFT JOIN groups_users ON flocks.id = groups_users.group_id LEFT JOIN users ON users.id = groups_users.USER_id WHERE flocks.id = %(flock_id)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================  
# SELECT: check if group name is unique
# =============================================
    @classmethod
    def unique_flock_name(cls,data):
        query = "SELECT * FROM flocks WHERE title = %(title)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================  
# CREATE: new flock
# =============================================
    @classmethod
    def save_flock(cls,data):
        query = "INSERT INTO flocks (title, city, state, privacy_setting) VALUES (%(title)s, %(city)s, %(state)s, %(privacy_setting)s);"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================
# INSERT: creator as the admin
# =============================================
    @classmethod
    def make_creator_admin(cls,data):
        query = "INSERT INTO flocks_users (flock_id,user_id,status) VALUES (%(flock_id)s , %(user_id)s,'admin')"
        results = connectToMySQL('book_club').query_db(query,data)
        return results

# =============================================
# DELETE: from group
# =============================================
    @classmethod
    def remove_from_flock(cls,data):
        query = "DELETE FROM flocks_users WHERE  flock_id = %(flock_id)s AND user_id = %(user_id)s;"
        results = connectToMySQL('book_club').query_db(query,data)
        return results