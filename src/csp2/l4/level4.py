from flask import Flask
from flask import request
from flask import render_template, make_response
from flask import send_from_directory

app = Flask(__name__)

def addCSP(response):
    csp = "default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; "
    csp += "style-src 'self'; base-uri 'self'; form-action 'self'"
    responseWithCSP = make_response(response)
    responseWithCSP.headers['Content-Security-Policy'] = csp
    return responseWithCSP

@app.route("/")
def search():
    if not request.args.get('timer'):
        # Show main timer page
        return addCSP(render_template('index.html'))
    else:
        try:
            timer = int(request.args.get('timer'))
        except Exception as e:
            return addCSP(render_template('index.html'))
        return addCSP(render_template('timer.html', timer=timer))

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')