from flask import Flask, render_template, session, request, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Keep it secert keep it safe"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def root():
    return render_template("index.html") 

# We can't use render_template when we use forms. We need to use redirect
# With forms we need 2 routes
@app.route('/users', methods=["POST"])
def users(): 
    # print("Got Post Info")
    # print(request.form)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect("/afterPost")

@app.route('/afterPost')
def from_post():
    # print("hitting the new route")
    return render_template("second.html", name = session["name"], email = session["email"]) 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001)    # Run the app in debug mode.