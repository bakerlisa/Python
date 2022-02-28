# from flask_app.config.mysqlconnection import connectToMySQL

# import re
# from flask import flash 

# from flask_app.models import user_model

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+[a-zA-Z]+$')

# class Message:
#     def __init__(self,data):
#         self.id = data['id']
#         self.content = data['content']
#         self.from_id = data['from_id']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']

#     def validate_message(message):
#         is_valid = True # we assume this is true
#         if len(message['content']) < 10:
#             flash("Message must be longer than 10 characters","message")
#             is_valid = False
#         if message['user_id'] == "0":
#             flash("Must choose a recipient","message")
#             is_valid = False
#         return is_valid

# # ==========================================
# # GET: all messages for a user
# # ==========================================
#     @classmethod
#     def get_all_for_message(cls,data):
#         query = "SELECT messages.id,messages.content,messages.from_id,messages.user_id,users2.id,users2.first_name AS from_first, users2.last_name AS from_last FROM messages LEFT JOIN users ON messages.user_id = users.id  LEFT JOIN users AS users2  ON users2.id = messages.from_id WHERE messages.user_id = %(id)s;"
#         results = connectToMySQL('book_club').query_db(query,data)
#         return results

# # ==========================================
# # INSERT: save message
# # ==========================================
#     @classmethod
#     def save_message(cls,data):
#         query = "INSERT INTO messages (message) VALUES (%(message)s);"
#         results = connectToMySQL('book_club').query_db(query,data)
#         return results

# # ==========================================
# # INSERT: save who it's forrm and who it's for
# # ==========================================
#     @classmethod
#     def save_to_from_info(cls,data):
#         query = "INSERT INTO users_messages (user_id,from_id,message_id) VALUES (%(user_id)s , %(from_id)s , %(message_id)s);"
#         results = connectToMySQL('book_club').query_db(query,data)
#         return results

# # ==========================================
# # DELETE: message
# # ==========================================
#     @classmethod
#     def delete_message(cls,data):
#         query = "DELETE FROM messages WHERE id = %(id)s;"
#         results = connectToMySQL('book_club').query_db(query,data)
#         return results
    