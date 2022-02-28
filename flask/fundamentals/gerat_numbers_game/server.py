from flask import Flask, render_template, request, redirect, session  
import random, math
# Import Flask to allow us to create our app
app = Flask(__name__) 
app.secret_key = "You shall not pass!!"

@app.route('/')
def root():
    session["number"] = int(random.random() * 100)
    return render_template("index.html") 

@app.route('/guess', methods=["POST"])
def guessing():   
    print(session)   
    if request.form['guess']:
        session["guess"] = int(request.form['guess'])
    else:
        session["guess"] = 0
    return redirect('guessing')

@app.route('/guessing')
def here_we_go():
    return render_template("index.html", sum = session["number"],guess = session["guess"])


@app.route('/<path:path>')
def catch_all(path):
    return render_template("404.html")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001)    # Run the app in debug mode.