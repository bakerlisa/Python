from flask import Flask, render_template, request, session, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Siiiiiiiiiiiiiilience"

@app.route('/')
def index():
    return render_template("index.html") 

# Cout up
@app.route('/count_cookies')
def count_cookies():
    if 'clicker' not in session:
        session['clicker'] = 0
    else: 
        session['clicker'] += 1
    return redirect("/")

# Cout up
@app.route('/reset')
def clear_cookies():
    session.clear()
    return redirect("/")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001)    # Run the app in debug mode.