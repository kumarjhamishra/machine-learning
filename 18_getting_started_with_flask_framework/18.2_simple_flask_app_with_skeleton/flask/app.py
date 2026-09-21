from flask import Flask

# initialize web app
'''
It creates an instance of the Flask class, which will be your WSGI (web server gateway interface)
application
'''
app = Flask(__name__)

# route of home page
@app.route("/")
def Welcome():
    return "Welcome to this flask course"

@app.route("/index")
def Index():
    return "Welcome to index page"

# entry point of .py file
if __name__ == "__main__":
    # debug will automatically restart the server once we save any changes during development
    app.run(debug=True)
