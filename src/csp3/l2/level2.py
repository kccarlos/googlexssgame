from flask import Flask
from flask import render_template
from flask import make_response
from flask import send_from_directory

import base64
import os

app = Flask(__name__)

# reference: https://csp.withgoogle.com/docs/faq.html
def GetCspNonce():
   """Returns a random nonce."""
   NONCE_LENGTH = 16
   return base64.b64encode(os.urandom(NONCE_LENGTH)).decode()


@app.route('/', methods=['GET', 'POST'])
def home():
   n1, n2 = [GetCspNonce() for _ in range(2)]
   responseWithCSP = make_response(render_template('index.html', n1=n1, n2=n2))
   cspheader = "script-src 'self' "
   cspheader += "'nonce-%s' 'nonce-%s' ;" % (n1, n2)
   cspheader += "connect-src 'self'; base-uri 'self'; form-action 'self' "
   responseWithCSP.headers['Content-Security-Policy'] = cspheader
   return responseWithCSP

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')