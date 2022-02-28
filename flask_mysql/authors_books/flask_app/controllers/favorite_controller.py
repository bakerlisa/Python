# from flask_app import app
# from flask import render_template,redirect,request,session,flash
# from flask_app.models.favorite_model import Favorite


# # ==============================
# # Save Author's FAVORITES books 
# # ==============================
# @app.route('/save_authors_favs',methods=["POST"])
# def save_authors_favs():
#     data = {
#         "book_id": request.form["fav_id"],
#         "author_id": request.form["author_id"]
#     }
#     save_author_fav = Favorite.save_authors_favs(data)
#     return redirect(f"/authors/{save_author_fav}")


# # ==============================
# # Get indv AUTHOR Info by ID
# # ==============================   
# @app.route('/authors/<int:id>')
# def get_author_info(id):
#     data = {
#         "id" : id
#     }
#     author_favs_list = Favorite.author_fav_books(data)
#     print(author_favs_list)
#     # author = Author.get_inv_author()
#     return render_template("author.html", author_favs_list = author_favs_list)