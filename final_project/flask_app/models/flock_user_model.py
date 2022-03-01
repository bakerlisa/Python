from flask_app.config.mysqlconnection import connectToMySQL

import re
from flask import flash 


class Flock_User:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.status = data['status']
        self.flock_id = data['flock_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    