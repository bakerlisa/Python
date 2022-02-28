from flask_app import app
from flask import Flask, render_template,redirect,session,request

#on/off switch: remener to put your controllers here
from flask_app.controllers import team_controller

@app.route('/<path:path>')
def catch_all(path):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)