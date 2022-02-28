from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "keep it secert kep it safe!"

@app.route('/')         
def root():
    return render_template("index.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

# checkout
@app.route('/checkout', methods=['POST'])         
def checkout():
    amount = (int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple']))
    customer = request.form['first_name']
    print(f"charging customer {customer} for {amount } fruits")
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']

    return redirect("/order")

@app.route('/order')
def submit_order():
    print(request.form)
    return render_template("checkout.html",strawberry = session['strawberry'], raspberry = session['raspberry'], apple = session['apple'], first_name = session['first_name'], last_name = session['last_name'], student_id = session['student_id']) 



if __name__=="__main__":   
    app.run(debug=True,port="5001")    