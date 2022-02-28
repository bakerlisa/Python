from flask import Flask, render_template, request, redirect, session   
app = Flask(__name__)    
app.secret_key = "It's the end of the world as we know it"

@app.route('/')
def root():
    session.clear()
    return render_template("index.html") 

@app.route('/rendering_result', methods=['POST'])
def result():
    session['code_name'] = request.form['code_name']
    session['mission'] = request.form['mission']
    session['talents'] = request.form['talents']
    session['reason'] = request.form['reason']
    session['truth_dare'] = request.form['truth_dare']
    session['pets'] = request.form.getlist('pet')
    return redirect("result") 

@app.route('/result')
def rendering():
    return render_template("result.html") 


@app.route('/<path:path>')
def catch_all(path):
    return render_template("404.html")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001)    # Run the app in debug mode.