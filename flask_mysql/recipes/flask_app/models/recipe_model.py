from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash 
# from flask_app import app
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30 = data['under_30']
        self.made_on = data['made_on']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True # we assume this is true
        if len(recipe['name']) < 2:
            flash("Name must be at least 2 characters.","reciepe")
            is_valid = False
        if len(recipe['description']) < 2:
            flash("Description must be at least 2 characters.","reciepe")
            is_valid = False
        if len(recipe['instruction']) < 2:
            flash("Instruction must be at least 2 characters.","reciepe")
            is_valid = False
        if len(recipe['made_on']) < 2:
            flash("Plase input a valid date","reciepe")
            is_valid = False
        return is_valid

# ========================================
# GET: all recipes
# ========================================
    @classmethod
    def list_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes').query_db(query)

        recipes = []

        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

# ========================================
# GET: single recipe data
# ======================================== 
    @classmethod
    def single_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL('recipes').query_db(query,data)
        return cls(results[0])

# ========================================
# CREATE: new reciepe
# ========================================
    @classmethod
    def add_recipe(cls,data):
        query = "INSERT INTO recipes (name,description,instruction,under_30,made_on) VALUES (%(name)s,%(description)s,%(instruction)s,%(under_30)s,%(made_on)s);"
        results = connectToMySQL('recipes').query_db(query,data)
        return results


# ========================================
# DELETE: recipe
# ========================================
    @classmethod
    def delete_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query,data)
        return results

# ========================================
# UPDATE: recipe
# ========================================
    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, under_30 = %(under_30)s, made_on = %(made_on)s WHERE id = %(id)s"
        results = connectToMySQL('recipes').query_db(query,data)
        return results
