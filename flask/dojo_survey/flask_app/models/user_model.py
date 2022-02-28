from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

class Alien:
    def __init__(self,data):
        self.id = data['id']
        self.code_name = data['code_name']
        self.species = data['species']
        self.talents = data['talents']
        self.langauge = data['langauge']
        self.home_planet = data['home_planet']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # this is the method: change name, change messages
    @staticmethod
    def validate_alien(alien):
        is_valid = True # we assume this is true
        if len(['code_name']) < 3:
            flash("Code Name must be at least 3 characters.")
            is_valid = False
        if len(alien['species']) < 3:
            flash("Species be at least 3 characters.")
            is_valid = False
        if len(alien['talents']) < 3:
            flash("Must choose a talent")
            is_valid = False
        if len(alien['langauge']) < 3:
            flash("Must choose a language")
            is_valid = False
        if len(alien['home_planet']) < 3:
            flash("Home Planet must be longer than 3 characters.")
            is_valid = False
        if len(alien['comment']) < 3:
            flash("Comment must be longer than 3 characters.")
            is_valid = False
        return is_valid
        
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('aliens').query_db(query)

        aliens = []

        for alien in results:
            aliens.append( cls(alien) )
        return aliens
    
    @classmethod
    def save_new_alien(cls,data):
        query = "INSERT INTO aliens (code_name,species,talents,langauge,home_planet,comment) VALUES ( %(code_name)s, %(species)s, %(talents)s,%(langauge)s,%(home_planet)s,%(comment)s)"
        results = connectToMySQL('aliens').query_db(query,data)
        return results

    @classmethod
    def get_alien_by(cls,data):
        query = "SELECT * FROM aliens WHERE id = %(id)s"
        results = connectToMySQL('aliens').query_db(query,data)
        return cls(results[0])
