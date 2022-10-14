from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

def addCSP(response):
    csp = "default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; "
    csp += "style-src 'self'; base-uri 'self'; form-action 'self'"
    responseWithCSP = make_response(response)
    responseWithCSP.headers['Content-Security-Policy'] = csp
    return responseWithCSP

@app.get('/')
def home():
   return render_template('index.html')

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')