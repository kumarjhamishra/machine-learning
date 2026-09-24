from flask import Flask, render_template, request

# initialize web app
'''
It creates an instance of the Flask class, which will be your WSGI (web server gateway interface)
application
'''
app = Flask(__name__)

# route of home page
@app.route("/")
def Welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index", methods=['GET'])
def Index():
    return render_template('index.html') # it will look for html folder inside templates folder

@app.route("/about")
def about():
    return render_template('about.html')

# both get and post route for form page
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"

    # form.html page in case of get method
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"

    # form.html page in case of get method
    return render_template('form.html')

# entry point of .py file
if __name__ == "__main__":
    # debug will automatically restart the server once we save any changes during development
    app.run(debug=True)
