from flask import Flask
from flask import request
from flask import current_app
from flask import send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
   return current_app.send_static_file('index.html')

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')