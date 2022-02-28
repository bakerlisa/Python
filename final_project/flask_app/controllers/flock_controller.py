# from flask_app import app
# from flask import render_template,redirect,request,session,flash
# from flask_app.models.flock_model import Group
# from flask_app.models.user_model import User


# # =============================================  
# # ROUTE:  group dashboard
# # =============================================  
# @app.route('/group_dashboard')
# def group_dashboard():
#     return render_template('group_dashboard.html')

# # =============================================  
# # ROUTE: join a group
# # =============================================  
# @app.route('/join_group')
# def join_group():
#     data = {
#         "id": session['id']
#     }
#     all_groups = Group.select_all_groups();
#     user_info = User.get_user_info(data)
#     return render_template("join_group.html",all_groups = all_groups,user_info=user_info)

# # =============================================  
# # CREATE: a group
# # =============================================  
# @app.route('/create_group',methods=["POST"])
# def create_group():
#     data = {
#         "name": request.form["name"],
#         "city": request.form["city"],
#         "state": request.form["state"],
#         "privacy_setting": request.form["privacy_setting"]
#     }
#     unqiue_name = Group.unique_grouping_name(data)
#     print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ")
#     print(unqiue_name)

#     if len(unqiue_name):
#         flash("Please pick a unique group name", "groups")
#         return redirect('/create_flock')
#     elif not Group.validate_group(request.form):
#         session["group_form"] = data
#         return redirect('/create_flock')
#     else:
#         new_group_id = Group.save_group(data)
#         dataTwo = {
#             "group_id": new_group_id,
#             "user_id": session['id']
#         }
#         Group.make_creator_admin(dataTwo)
#         return render_template('group_dashboard.html')
