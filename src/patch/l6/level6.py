from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.get('/')
def home():
   return render_template('index.html')

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')