from flask import Flask
from flask import request
from flask import render_template, make_response
from flask import send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
   mainPageResponse = make_response(render_template('index.html'))
   csp = "default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; "
   csp += "style-src 'self'; base-uri 'self'; form-action 'self'"
   mainPageResponse.headers['Content-Security-Policy'] = csp
   return mainPageResponse

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')