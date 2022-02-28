from flask import Flask, render_template,redirect,session,request,session,flash
from flask_app import app

from flask_app.controllers import user_controller
from flask_app.controllers import show_controller 
from flask_app.controllers import liked_controller 

#on/off switch: remener to put your controllers here
# Server imporst entire file 

if __name__ == "__main__":
    app.run(debug=True,port=5001)