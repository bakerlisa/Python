from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ======================
# List all Authors
# ======================
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_authors').query_db(query)

        authors = []

        for author in results:
            authors.append( cls(author) )
        return authors

# ======================
# Add Author
# ======================
    @classmethod
    def create_new_author(cls,data):
        query = "INSERT INTO authors (name,created_at) VALUES(%(name)s, NOW())"
        new_author_id = connectToMySQL('books_authors').query_db(query,data)
        print()
        return new_author_id

# ======================
# Get INDV Author Info
# ======================
    @classmethod
    def get_inv_author(cls,data):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        author_id = connectToMySQL('books_authors').query_db(query,data)
        return author_id
        
