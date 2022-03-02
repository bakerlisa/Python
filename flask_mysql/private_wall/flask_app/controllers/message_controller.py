from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.message_model import Message
from flask_app.models.user_model import User
# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ==========================================
# SEND message
# ==========================================
@app.route('/send_message',methods=["POST"])
def send_message():
    data = {
        "user_id": request.form["user_id"],
        "content": request.form["content"],
        "from_id": request.form.get("from_id")
    }

    if not Message.validate_message(request.form):
        return redirect('/wall')
    else:
        Message.save_message(data)
        User.increment_messge_cout(data = { "id": session['id'] })
        return redirect('/save_message')

@app.route('/save_message')
def save_message():
    return redirect('/wall')

@app.route('/delete_message/<int:id>')
def delete_message(id):
    data = {
        "id": id,
    }
    Message.delete_message(data)
    return redirect('/wall')