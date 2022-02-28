from flask_app import app
from flask import render_template,redirect,request,session,flash

from flask_app.models.liked_model import Likes

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

# ========================================
# ADD: a like to a show
# ========================================
@app.route('/like/<int:id>')
def like_show(id):
    data = {
        "show_id":id,
        "user_id": session['id']
    }
    Likes.like_show(data)
    return redirect('/dashboard')

# ========================================
# DELETE: show
# ========================================
@app.route('/unlike/<int:id>')
def unlike_show(id):
    data = {
        "show_id":id,
        "user_id": session['id']
    }
    Likes.unlike_show(data)
    return redirect('/dashboard')