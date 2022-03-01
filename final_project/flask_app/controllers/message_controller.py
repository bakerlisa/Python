from flask_app import app
from flask import render_template,redirect,request,session,flash

# from flask_app.models.user_model import User
from flask_app.models.message_model import Message
from flask_app.models.flock_model import Flock


# # === 1. Remeber to import file on server.py 
# # === Note: Controllers pull in classes

# # ==========================================
# # ROUTE: messages
# # ==========================================
# @app.route('/message')
# def save_message():

#     return redirect('/dashboard')

# ============================================= 
# Join: Group
# ============================================= 
@app.route('/submit_join_request',methods=["POST"])
def join_flock():
    # save the message
    data = {
        "mesage" : request.form["mesage"]
    }
    new_message_id = Message.save_message(data)

    # figure out who's the admin for the site, give them the message
    dataTwo = {
        "flock_id" : request.form["flock_id"]
    }
    get_admin_for_group = Flock.get_admin_id(dataTwo)

    #save all the info in the users_messages_table
    dataThree = {
        "user_id" : get_admin_for_group,
        "from_id" : session['id'],
        "message_id" : new_message_id
    }

    Message.save_to_from_info(dataThree)
    return redirect('/group_dashboard')

# ============================================= 
# Route: after succesfful flock join
# ============================================= 
@app.route('/submit_request')
def request_submitted():
    return render_template('submission.html')