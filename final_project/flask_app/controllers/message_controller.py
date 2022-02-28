# from flask_app import app
# from flask import render_template,redirect,request,session,flash
# from flask_app.models.message_model import Message
# from flask_app.models.user_model import User
# from flask_app.models.flock_model import Group


# # === 1. Remeber to import file on server.py 
# # === Note: Controllers pull in classes

# # ==========================================
# # ROUTE: messages
# # ==========================================
# @app.route('/message')
# def save_message():

#     return redirect('/dashboard')

# # ============================================= 
# # Join: Group
# # ============================================= 
# @app.route('/submit_join_request',methods=["post"])
# def join_flock():
#     # save the message
#     data = {
#         "mesage" : request.form["mesage"]
#     }
#     new_message_id = Message.save_message(data)

#     # figure out who's the admin for the site
#     dataTwo = {
#         "group_id" : request.form["group_id"]
#     }
#     get_admin_for_group = Group.get_admin_id(dataTwo)

#     #save all the info in the users_messages_table
#     dataThree = {
#         "user_id" : get_admin_for_group,
#         "from_id" : request.form["from_id"],
#         "message_id" : new_message_id
#     }

#     Message.save_to_from_info(dataThree)
#     return redirect('/submit_request')


# @app.route('/submit_request')
# def request_submitted():
#     return render_template('submission.html')