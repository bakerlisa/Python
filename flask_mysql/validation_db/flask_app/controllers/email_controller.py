from flask_app import app
from flask import render_template,redirect,request,session,flash

from flask_app.models.email_model import Email


# === 1. Remeber to import file on server.py 
# === Note: Controllers pull in classes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email_validate', methods=["POST"])
def email_validate():
    if not Email.validate_email(request.form):
        return redirect('/')
    else:
        data = {
            "email" : request.form["email"]
        } 
        Email.add_new_email(data)
        return redirect('/results')

@app.route('/results')
def results():
    all_emails = Email.get_all_emails()
    return render_template ("results.html", all_emails = all_emails)

@app.route('/delete/<int:id>')
def delete_email(id):
    data = {
        "id" : id
    }
    Email.delete_address(data)
    flash("Your Email has been Deleted")
    return redirect('/results')