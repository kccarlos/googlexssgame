from flask import Flask
from flask import request
from flask import redirect
from flask import render_template, make_response
from flask import send_from_directory

import base64
import os

app = Flask(__name__)

availableRoutes = ['signup', 'confirm', 'welcome']

# reference: https://csp.withgoogle.com/docs/faq.html
def GetCspNonce():
   """Returns a random nonce."""
   NONCE_LENGTH = 16
   return base64.b64encode(os.urandom(NONCE_LENGTH)).decode()

def addCSP(response, n1):
    cspheader = "script-src 'self' "
    if n1:
        cspheader += "'nonce-%s' ;" % n1
    responseWithCSP = make_response(response)
    responseWithCSP.headers['Content-Security-Policy'] = cspheader
    return responseWithCSP

@app.route("/")
@app.route("/welcome")
def welcome():
    return addCSP(render_template('welcome.html'), False)

@app.route("/signup")
def signup():
    next = request.args.get('next')
    if next in availableRoutes:
        return addCSP(render_template('signup.html', next=next), False)
    else:
        return redirect("/welcome")

@app.route("/confirm")
def confirm():
    n1 = GetCspNonce()
    next = request.args.get('next', 'welcome')
    if next in availableRoutes:
        return addCSP(render_template('confirm.html', next=request.args.get('next', 'welcome'), n1=n1), n1=n1)
    else:
        return redirect("/welcome")

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')