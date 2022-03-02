from flask_app.config.mysqlconnection import connectToMySQL

import re
from flask import flash 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+[a-zA-Z]+$')

class Book:
    def __init__(self,data):
        self.name = data['name']
