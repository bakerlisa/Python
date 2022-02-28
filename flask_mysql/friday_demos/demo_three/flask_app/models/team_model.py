from flask_app.config.mysqlconnection import connectToMySQL

class Team:
    def __init__(self,data):
        self.name = data['name']

    @classmethod
    def get_all_teams(cls,data):
        query = "SELECT * FROM teams;"
        results = connectToMySQL('country_fair').query_db(query)

        teams = []

        for team in results:
            teams.append( cls(team) )
        return teams