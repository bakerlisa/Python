from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.flock_model import Flock
from flask_app.models.user_model import User


# =============================================  
# ROUTE:  group dashboard
# =============================================  
@app.route('/flock_dashboard')
def flock_dashboard():
    data = {
        "id": session['id']
    }
    flock_info = Flock.get_all_flocks_info(data)
    return render_template('flock_dashboard.html',flock_info=flock_info)

# =============================================  
# ROUTE: join a flock
# =============================================  
@app.route('/join_flock')
def join_flock():
    data = {
        "id": session['id']
    }
    user_info = User.get_user_info(data)
    all_flocks = Flock.select_all_flocks(data)
    return render_template("join_flock.html",user_info=user_info,all_flocks=all_flocks)

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
    return render_template('flock_dashboard.html')

# ROUTE: flock settings
@app.route('/flock_settings/<int:id>')
def flock_settings(id):
    data = { "id" : id }
    get_all_members = Flock.get_all_members(data)
    return render_template('flock_settings.html',get_all_members=get_all_members)

# =============================================  
# CREATE: a group
# =============================================  
@app.route('/create_new_flock',methods=["POST"])
def create_new_flock():
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

# =============================================  
# DELETE : leave group
# =============================================  
@app.route('/leave_flock', methods=["POST"])
def leave_flock():
    data = {
        "user_id": request.form['user_id'],
        "flock_id": request.form['flock_id']
    }
    Flock.remove_from_flock(data)
    flash("You've been remoed from the flock","info")
    return redirect('/dashboard')