from flask import Flask
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
    cspheader += "'nonce-%s' ;" % n1
    responseWithCSP = make_response(response)
    responseWithCSP.headers['Content-Security-Policy'] = cspheader
    return responseWithCSP

@app.get('/')
def home():
    n1 = GetCspNonce()
    return addCSP(render_template('index.html', n1=n1), n1)

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')