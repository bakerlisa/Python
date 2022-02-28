from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo_model

class Ninja:
    def __init__(self,data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.dojo_id = data['dojo_id']

# =================================
# Get All Ninjas
# =================================  
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_ninjas').query_db(query)

        ninjas = []

        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

# =================================
# Create New Ninja
# =================================  
    @classmethod
    def create_new_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id,created_at) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW());"
        new_ninja_id = connectToMySQL('dojos_ninjas').query_db(query,data)
        return new_ninja_id

# =================================
# Get 1 Ninja
# =================================
    @classmethod
    def get_ninja_students(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        indv_dojo_id = connectToMySQL('dojos_ninjas').query_db(query,data)
        return indv_dojo_id

# =================================
# Get Ninjas and Dojos Info
# =================================
    @classmethod
    def get_all_dojos_ninjas(cls,data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query,data)

        all_dojos_with_ninjas = []

        for row in results:
            one_dojo_ninja = cls(row)

            dojo_data  = {
                "id" : row['dojos.id'],
                "name" : row['name'],
                "created_at" : row['dojos.created_at'],
                "updated_at" : row['dojos.updated_at']
            }
            
            one_dojo_ninja.dojo = dojo_model.Dojo(dojo_data)

            all_dojos_with_ninjas.append(one_dojo_ninja)
        return all_dojos_with_ninjas


