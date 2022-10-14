from flask import Flask
from flask import request
from flask import render_template, make_response
from flask import send_from_directory

import base64
import os

app = Flask(__name__)

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
def search():
    n1 = GetCspNonce()
    if not request.args.get('timer'):
        # Show main timer page
        return addCSP(render_template('index.html'), False)
    else:
        try:
            timer = int(request.args.get('timer'))
        except Exception as e:
            return addCSP(render_template('index.html'), False)
        return addCSP(render_template('timer.html', timer=timer, n1=n1), n1)

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')