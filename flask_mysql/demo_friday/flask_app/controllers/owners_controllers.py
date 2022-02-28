from flask_app import app
from flask import render_template,redirect,request,session,flash
from file.name import class.name

# === Remeber to add from 
# flask_app.controllers_name import file_name 
# === to server.py  #

@app.route('/')
def index():
    return render_template('index.html')