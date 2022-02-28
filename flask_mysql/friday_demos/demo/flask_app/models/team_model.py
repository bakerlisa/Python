from flask_app.config.mysqlconnection import connectToMySQL

class Team:
    def __init__(self,data):
        self.name = data['name']
        self.location = data['location']
        self.sport = data['sport']
        self.champs = data['champs']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_teams(cls):
        query = "SELECT * FROM teams;"
        results = connectToMySQL('country_fair').query_db(query)

        teams = []

        for team in results:
            teams.append( cls(team) )
        return teams