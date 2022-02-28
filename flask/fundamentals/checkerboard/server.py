from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/', defaults={'row': 8,'col': 8,'color1':"red",'color2':"black"})
@app.route('/<int:row>/',defaults={'col': 8,'color1':"red",'color2':"black"})
@app.route('/<int:row>/<int:col>/',defaults={'color1':"red",'color2':"black"})
@app.route('/<int:row>/<int:col>/<color1>/',defaults={'color2':"black"})
@app.route('/<int:row>/<int:col>/<color1>/<color2>/')
def index(row,col,color1,color2):
    return render_template("index.html", row=row,col=col,color1=color1,color2=color2)

         # The "@" decorator associates this route with the function immediately following

@app.route('/<path:path>')
def catch_all(path):
    return render_template("404.html")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001)    # Run the app in debug mode.