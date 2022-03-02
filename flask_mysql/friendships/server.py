from flask_app import app

#on/off switch: remener to put your controllers here
# Server imporst entire file 
from flask_app.controllers import friend_controller

if __name__ == "__main__":
    app.run(debug=True,port=5001)