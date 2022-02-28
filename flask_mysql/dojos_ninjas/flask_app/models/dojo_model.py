from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create_new_dojo(cls,data):
        query = "INSERT INTO dojos (created_at, updated_at, name) VALUES ( NOW(), NOW(), %(dojo_name)s );"
        new_dojo_id = connectToMySQL('dojos_ninjas').query_db(query,data)
        return new_dojo_id

    @classmethod
    def get_indv_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        dojo_id = connectToMySQL('dojos_ninjas').query_db(query,data)
        return cls(dojo_id[0])