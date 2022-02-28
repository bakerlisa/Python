from flask import Flask, render_template,redirect,session,request
from flask_app import app

#on/off switch: remener to put your controllers here
# Server imporst entire file 
from flask_app.controllers import author_controller
from flask_app.controllers import book_controller
from flask_app.controllers import favorite_controller


if __name__ == "__main__":
    app.run(debug=True,port=5001)