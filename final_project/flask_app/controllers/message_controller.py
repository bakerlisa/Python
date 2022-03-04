from flask_app import app
from flask import render_template,redirect,request,session,flash

# from flask_app.models.user_model import User
from flask_app.models.message_model import Message
from flask_app.models.flock_model import Flock


# # === 1. Remeber to import file on server.py 
# # === Note: Controllers pull in classes

# ==========================================
# ROUTE: messages
# ==========================================
@app.route('/messages')
def show_all_messages():
    data = { "id": session['id'] }

    get_all_messages = Message.get_messages(data)
    return render_template('/messages.html',get_all_messages = get_all_messages)

# ============================================= 
# Route: after succesfful flock join
# ============================================= 
@app.route('/submit_request')
def request_submitted():
    return render_template('submission.html')

# ============================================= 
# Join: Group
# ============================================= 
@app.route('/submit_join_request',methods=["POST"])
def submit_join_request():
    
    if not request.form["flock_id"]:
        flash("Please pick a flock to join!","message")
        return redirect('/dashboard')
    else:
        # save the message
        flock_id = request.form["flock_id"].split(",")[0]
        data = {
            "message" : request.form["message"],
            "message_type" : "join_request",
            "from_id" : session['id'],
            "flock_id": flock_id
        }
        new_message_id = Message.save_message(data)

        user_id = int(request.form["flock_id"].split(",")[1])

        dataTwo = {
            "user_id" : user_id,
            "message_id" : new_message_id
        }

        Message.save_to_from_info(dataTwo)
        flash("Your request to join the flock has been sent! Keep an eye on your inbox","info")
        return redirect('/flocks_dashboard')

# ============================================= 
# DELETE: message
# ============================================= 
@app.route('/delete_message/<int:mess_id>/<int:user_id>')
def delete_message(mess_id,user_id):
    data = {
        "id": mess_id,
        "user_id": user_id
    }
    Message.delete_message(data)
    Message.delete_user_message(data)
    return redirect('/messages')