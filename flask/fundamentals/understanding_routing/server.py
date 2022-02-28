from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def djoj():
    return 'Dojo'  # Return the string 'Hello World!' as a response

@app.route('/say/<name>')          # The "@" decorator associates this route with the function immediately following
def say(name):
    user = name
    return 'Hi ' + user.capitalize() + '!' # Return the string 'Hello World!' as a response

@app.route('/repeat/<int:num>/<string:message>')
def repeat(num,message):
    return f"{message * num}"

@app.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    return 'Sorry! No response. Try again.\n'


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001)    # Run the app in debug mode.

