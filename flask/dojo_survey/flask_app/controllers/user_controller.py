from flask_app import app
from flask import render_template,redirect,request,session,flash

# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

from flask_app.models.user_model import Alien

@app.route('/')
def root():
    return render_template("index.html") 

@app.route('/rendering_result', methods=['POST'])
def result():
    if not Alien.validate_alien(request.form):
        return redirect('/')
    else:
        data = {
            "code_name" : request.form['code_name'],
            "species" : request.form['species'],
            "talents" : request.form['talents'],
            "langauge" : request.form['langauge'],
            "home_planet" : request.form['home_planet'],
            "comment" : request.form['comment'],
        }
        new_alien_id = Alien.save_new_alien(data)
        return redirect(f"result/{new_alien_id}") 


@app.route('/result/<int:id>')
def rendering(id):
    data = {
        "id": id
    }
    alien = Alien.get_alien_by(data)
    return render_template("result.html", alien = alien) 

    