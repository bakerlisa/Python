from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.flock_model import Flock
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

# =============================================  
# ROUTE: create a flock
# =============================================  
@app.route('/create_flock')
def create_flock():
    return render_template('create_flock.html')

# =============================================  
# ROUTE: create a flock
# ============================================= 
@app.route('/new_flock_made')
def new_flock_made():
    return render_template('group_dashboard.html')

# =============================================  
# CREATE: a group
# =============================================  
@app.route('/create_new_flock',methods=["POST"])
def create_new_flock():
    print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ")
    print("HELLLLLLLo")
    data = {
        "title": request.form['title'],
        "city": request.form['city'],
        "state": request.form['state'],
        "privacy_setting": request.form['privacy_setting']
    }

    unqiue_name = Flock.unique_flock_name(data)

    if not Flock.validate_flock(request.form):
        session["group_form"] = data
        return redirect('/create_flock')
    elif len(unqiue_name):
        flash("Please pick a unique group name", "flocks")
        return redirect('/create_flock')
    else:
        new_flock_id = Flock.save_flock(data)
        dataTwo = {
            "flock_id": new_flock_id,
            "user_id": session['id']
        }
        Flock.make_creator_admin(dataTwo)
        return redirect('/new_flock_made')


