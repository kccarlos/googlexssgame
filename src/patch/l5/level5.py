from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

availableRoutes = ['signup', 'confirm', 'welcome']

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route("/signup")
def signup():
    next = request.args.get('next')
    if next in availableRoutes:
        return render_template('signup.html', next=next)
    else:
        return redirect("/welcome")

@app.route("/confirm")
def confirm():
    next = request.args.get('next', 'welcome')
    if next in availableRoutes:
        return render_template('confirm.html', next=request.args.get('next', 'welcome'))
    else:
        return redirect("/welcome")

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')