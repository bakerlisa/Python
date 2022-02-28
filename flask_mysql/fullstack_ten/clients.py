# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Client:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['email']
    # Now we use class methods to query our database

    @classmethod
    def get_all_clients(cls):
        query = "SELECT * FROM clients;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('lead_gen_business').query_db(query)
        # Create an empty list to append our instances of friends
        clients = []
        # Iterate over the db results and create instances of friends with cls.
        for client in results:
            clients.append( cls(client) )
        return clients
            
    @classmethod
    def get_client_info(cls,data):
        query = "SELECT * FROM clients WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        client_id = connectToMySQL('lead_gen_business').query_db(query,data)
        return cls(client_id[0])

    @classmethod
    def add_client(cls,data):
        query = "INSERT INTO clients (first_name,last_name,email,joined_datetime) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW());"
        new_client = connectToMySQL('lead_gen_business').query_db(query,data)
        return new_client
