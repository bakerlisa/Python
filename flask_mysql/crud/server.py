from flask_app import app
from flask import Flask,render_template,request,redirect,session,flash

from flask_app.controllers import user_controller

if __name__ == "__main__":
    app.run(debug=True,port=5001)