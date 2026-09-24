# Jinja2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} -> conditions, for loops
{#...#} -> this is for comments
'''


from flask import Flask, render_template, request, redirect, url_for

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

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f"Hello {name}!"

#     # form.html page in case of get method
#     return render_template('form.html')

# Variable rule
@app.route('/success/<int:score>')
def success(score):
    # if we are passing int then we have to typecast it to make it work
    # return "The marks you got is " + str(score)

    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', results=res)


@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {'score':score, 'res':res}
    return render_template('result1.html', results=exp)

# if condition 26:06
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html', results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results=score)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science)/4
        return redirect(url_for('successres', score=total_score))
    return render_template('getresult.html')

# entry point of .py file
if __name__ == "__main__":
    # debug will automatically restart the server once we save any changes during development
    app.run(debug=True)
