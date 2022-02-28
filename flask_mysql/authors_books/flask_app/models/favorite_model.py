from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model
from flask_app.models import book_model

class Favorite:
    def __init__(self,data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ======================
# Save Authors Fav
# ======================
    @classmethod
    def save_authors_favs(cls,data):
        query = "INSERT INTO authors_has_books (author_id,book_id) VALUES (%(author_id)s,%(book_id)s)"
        faves = connectToMySQL('books_authors').query_db(query,data)
        return faves

# ======================
# List of books
# ======================
    @classmethod
    def author_fav_books(cls,data):
        query = "SELECT * from books LEFT JOIN authors_has_books ON books.id = authors_has_books.book_id LEFT JOIN authors ON authors_has_books.author_id = authors.id WHERE author_id = %(id)s;"
        results = connectToMySQL('books_authors').query_db(query)
        print(results)
        author_fave_list = []

        for row in results:
            one_book = cls(row)

            author_data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }

            one_book.author = author_model.Author(author_data)
            
            author_fave_list.append(one_book)
            print(row)
        print(author_fave_list)
        return author_fave_list